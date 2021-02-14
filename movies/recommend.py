import pandas as pd
import requests

def recommender_sigmoid_kernel(title, sig, df, movie_indices):
    result = []
    idx = movie_indices[title]
    sig_scores = list(enumerate(sig[idx]))
    sig_scores = sorted(sig_scores, key=lambda x: x[1], reverse=True)
    sig_scores = sig_scores[1: 11]
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