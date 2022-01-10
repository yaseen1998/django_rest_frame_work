from django.urls import path,include
from .views import MovieListAV,MovieDetail
# from .views import movie_list,movie_detail
# urlpatterns=[
#     path('list/',movie_list,name = 'movie_list'),
#     path('<int:pk>/',movie_detail,name = 'movie_detail')
# ]
urlpatterns=[
    path('list/',MovieListAV.as_view(),name = 'movie_list'),
    path('<int:pk>/',MovieDetail.as_view(),name = 'movie_detail')
]