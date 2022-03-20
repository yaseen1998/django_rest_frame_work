from django.urls import path,include
from .views import movie_list,movie_detail,index
urlpatterns=[
    path('list/',movie_list,name = 'movie_list'),
    path('<int:pk>/',movie_detail,name = 'movie_detail'),
    path("", index, name="index"),
]