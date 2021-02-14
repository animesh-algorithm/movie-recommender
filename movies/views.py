from django.shortcuts import render, HttpResponse
from . import scrape
from .recommend import recommender_sigmoid_kernel
import pandas as pd
import pickle
import joblib

df = pd.read_csv('movies_dataset.csv')
sig_scores = joblib.load('sig.sav')

# Create your views here.
def index(request):
    # df = pd.read_csv('https://raw.githubusercontent.com/animesharma3/Movie-Recommendation/main/movies_dataset.csv')
    data = scrape.get_top_movies(df, 10)
    context = {
        'data': data
    }
    return render(request, 'movies/index.html', context=context)

def get_movie_recommendations(request, imdb):
    title = df[df['imdb_id'] == imdb]['title'].values[0]
    movie_indices = pd.Series(df.index, index=df['title'])
    recommendations = recommender_sigmoid_kernel(title, sig_scores, df, movie_indices)
    title, released, runtime, genre, plot, actors, writers, production, boxoffice, imdb_ratings, rotten_tomatoes_ratings, awards, poster, overview, tagline = scrape.get_movie_data(df, imdb)
    context = {
        'title': title,
        'released': released,
        'runtime': runtime,
        'genre': genre,
        'plot': plot,
        'actors': actors,
        'writers': writers,
        'production': production,
        'boxoffice': boxoffice,
        'imdb_ratings': imdb_ratings,
        'rotten_tomatoes_ratings': rotten_tomatoes_ratings,
        'awards': awards,
        'poster': poster,
        'overview': overview,
        'tagline': tagline,
        'recommendations': recommendations
    }
    return render(request, 'movies/recommend.html', context=context)