import pandas as pd
import requests
import ast

def get_top_movies(df, n):
    result  = []
    for i in range(len(df[:n+1])):
        title = df.iloc[i]['title']
        imdb_id = df.iloc[i]['imdb_id']
        url = 'https://www.omdbapi.com/?apikey=69de4384&i={}'.format(imdb_id) # Import data from API
        response = requests.get(url)
        data = response.json()
        # print(data.keys())
        genre = data['Genre']
        poster_img = data['Poster']
        result.append([title, genre, poster_img, imdb_id]) # Combine both the data
    return result

def filter_movies_by_genre(name, df, N):
    count = 0
    result = []
    for i in range(len(df)):
        genres = df.iloc[i].genres
        genres = ast.literal_eval(genres)
        for genre in genres:
            if genre['name'] == name:
                title = df.iloc[i]['title']
                imdb_id = df.iloc[i]['imdb_id']
                url = 'https://www.omdbapi.com/?apikey=69de4384&i={}'.format(imdb_id) # Import data from API
                response = requests.get(url)
                data = response.json()
                # print(data.keys())
                genre = data['Genre']
                poster_img = data['Poster']
                result.append([title, genre, poster_img, imdb_id]) 
                count += 1
                # print(title, result)
                continue
            if count == N:
                return result

def get_movie_data(df, imdb):
    url = 'https://www.omdbapi.com/?apikey=69de4384&i={}'.format(imdb) 
    response = requests.get(url)
    data = response.json()
    # print(data.keys())
    overview = df[df['imdb_id'] == imdb]['overview'].values[0]
    tagline = df[df['imdb_id'] == imdb]['tagline'].values[0]
    title = data['Title']
    released = data['Released']
    runtime = data['Runtime']
    genre = data['Genre']
    plot = data['Plot']
    actors = data['Actors']
    writers = data['Writer']
    production = data['Production']
    boxoffice = data['BoxOffice']
    imdb_ratings = data['imdbRating']
    rotten_tomatoes_ratings = data['Ratings'][1]['Value']
    awards = data['Awards']
    poster = data['Poster']    
    return [title, released, runtime, genre, plot, actors, writers, production, boxoffice, imdb_ratings, rotten_tomatoes_ratings, awards, poster, overview, tagline]
