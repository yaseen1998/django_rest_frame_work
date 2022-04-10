from django.urls import path,include
from .views import Movie_list,movie_detail,ClearCacheing
urlpatterns=[
    path('list/',Movie_list.as_view(),name = 'movie_list'),
    path('<int:pk>/',movie_detail,name = 'movie_detail'),
    path('clear/',ClearCacheing.as_view(),name = 'movie_detail'),
]