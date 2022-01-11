from django.urls import path,include
from .views import WatchDetailAV,WatchListAV,StreamPlatformAV,StreamDetailAV,ReviewList,ReviewDetail,ReviewCreate
# from .views import movie_list,movie_detail
# urlpatterns=[
#     path('list/',movie_list,name = 'movie_list'),
#     path('<int:pk>/',movie_detail,name = 'movie_detail')
# ]
urlpatterns=[
    path('list/',WatchListAV.as_view(),name = 'movie_list'),
    path('<int:pk>/',WatchDetailAV.as_view(),name = 'movie_detail'),
    
    path('platform/<int:pk>/',StreamDetailAV.as_view(),name = 'platform_detail'),
    path('platform/',StreamPlatformAV.as_view(),name = 'platform'),
    
    # path('review/',ReviewList.as_view(),name = 'review'),
    # path('review/<int:pk>/',ReviewDetail.as_view(),name = 'review_detail'),
    
    
    path('platform/<int:pk>/review/',ReviewList.as_view(),name = 'review'),
    path('platform/<int:pk>/review-create/',ReviewCreate.as_view(),name = 'review-create'),
    path('platform/review/<int:pk>/',ReviewDetail.as_view(),name = 'review_detail'),
]