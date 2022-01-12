from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import WatchDetailAV,WatchListAV,StreamPlatformAV,StreamDetailAV,ReviewList,ReviewDetail,ReviewCreate,StreamPlatformVS,UserReview,WatchListGV
# from .views import movie_list,movie_detail
# urlpatterns=[
#     path('list/',movie_list,name = 'movie_list'),
#     path('<int:pk>/',movie_detail,name = 'movie_detail')
# ]
router = DefaultRouter()
router.register('platform',StreamPlatformVS,basename = 'platform')
urlpatterns=[
    path('list/',WatchListAV.as_view(),name = 'movie_list'),
    path('<int:pk>/',WatchDetailAV.as_view(),name = 'movie_detail'),
    path('list2/',WatchListGV.as_view(),name = 'serachwatch'),
    
    path('',include(router.urls)),
    
    # path('platform/<int:pk>/',StreamDetailAV.as_view(),name = 'platform_detail'),
    # path('platform/',StreamPlatformAV.as_view(),name = 'platform'),
    
    # path('review/',ReviewList.as_view(),name = 'review'),
    # path('review/<int:pk>/',ReviewDetail.as_view(),name = 'review_detail'),
    
    
    path('<int:pk>/review/',ReviewList.as_view(),name = 'review'),
    path('<int:pk>/review-create/',ReviewCreate.as_view(),name = 'review-create'),
    path('review/<int:pk>/',ReviewDetail.as_view(),name = 'review_detail'),
    path('reviews/',UserReview.as_view(),name = 'username_review_detail'),
    # path('reviews/<str:username>/',UserReview.as_view(),name = 'username_review_detail'),
]