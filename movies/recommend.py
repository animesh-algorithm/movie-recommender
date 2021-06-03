import pandas as pd
import requests
import pickle
import warnings
warnings.filterwarnings('ignore')

def recommender_sigmoid_kernel(title, sig, df, movie_indices):
    result = []
    idx = movie_indices[title]
    sig_scores = list(enumerate(sig[idx]))
    sig_scores = sorted(sig_scores, key=lambda x: x[1], reverse=True)
    sig_scores = sig_scores[1: 21]
    indices = [i[0] for i in sig_scores]
    for i in indices:
        title = df.iloc[i]['title']
        imdb_id = df.iloc[i]['imdb_id']
        url = 'https://www.omdbapi.com/?apikey=69de4384&i={}'.format(imdb_id) # Import data from API
        response = requests.get(url)
        data = response.json()
        # print(data.keys())
        genre = data['Genre']
        poster_img = data['Poster']
        result.append([title, genre, poster_img, imdb_id])
    return result

def recommender_nearest_neighbors(title, df):
    result = []
    file = open('nneighbors_model', 'rb')
    model = pickle.load(file)
    features = ['budget', 'popularity', 'revenue', 'runtime', 'status', 'vote_average', 'vote_count', 'title']
    final_df = df[features].copy()
    final_df.dropna(inplace=True)
    final_df = pd.get_dummies(final_df, columns=['status'])
    data = final_df[final_df['title'] == title][['budget', 'popularity', 'revenue', 'runtime', 'vote_average', 'vote_count','status_In Production', 'status_Planned', 'status_Post Production', 'status_Released', 'status_Rumored']].values
    ind = model.kneighbors(data, return_distance=False)
    for i in ind[0]:
        title = df.iloc[i]['title']
        imdb_id = df.iloc[i]['imdb_id']
        url = 'https://www.omdbapi.com/?apikey=69de4384&i={}'.format(imdb_id) # Import data from API
        response = requests.get(url)
        data = response.json()
        # print(data.keys())
        genre = data['Genre']
        poster_img = data['Poster']
        result.append([title, genre, poster_img, imdb_id])
    return result
