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
    overview = str(df[df['imdb_id'] == imdb]['overview'].values[0])
    tagline = str(df[df['imdb_id'] == imdb]['tagline'].values[0])
    title = str(data['Title'])
    released = str(data['Released'])
    runtime = str(data['Runtime'])
    genre = str(data['Genre'])
    plot = str(data['Plot'])
    actors = str(data['Actors'])
    writers = str(data['Writer'])
    production = str(data['Production'])
    boxoffice = str(data['BoxOffice'])
    imdb_ratings = str(data['imdbRating'])
    try:
        rotten_tomatoes_ratings = str(data['Ratings'][1]['Value'])
    except Exception as e:
        rotten_tomatoes_ratings = 'NA'
    awards = str(data['Awards'])
    poster = str(data['Poster']    )
    return [title, released, runtime, genre, plot, actors, writers, production, boxoffice, imdb_ratings, rotten_tomatoes_ratings, awards, poster, overview, tagline]
