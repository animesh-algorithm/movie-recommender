from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('movie/<str:imdb>', views.get_movie_recommendations, name='get_recommendations')
]