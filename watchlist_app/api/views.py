from watchlist_app.models import WatchList,StreamPlatform,Review
from rest_framework.response import Response
from .serializers import WatchListSerializer,StreamPlatformSerializer,ReviewSerailizer
from rest_framework.decorators import api_view
from rest_framework import status,mixins,generics,viewsets
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly
from .permissions import AdminOrReadOnly,ReviewUserOrReadOnly
from .throttling import ReviewCreateTh,ReviewListTh
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .pagination import WatchListPagination,WatchListLimit,WatchListCursor

class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerailizer
    throttle_classes=[ReviewCreateTh]
    
    def get_queryset(self):
        return Review.objects.all()
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        watchlist = WatchList.objects.get(pk=pk)
        review_user = self.request.user
        review_queryset = Review.objects.filter(watchlist_app=watchlist,review_user=review_user)
        if review_queryset.exists():
            raise ValidationError('you have already reviewed this movie')
        
        if watchlist.number_ratings==0:
            watchlist.avg_ratings = serializer.validated_data['rating']
        else:
            watchlist.avg_ratings = (serializer.validated_data['rating']+watchlist.avg_ratings)/2
            
        watchlist.number_ratings +=1
        watchlist.save()
        
        serializer.save(watchlist_app = watchlist,review_user=review_user)
        
        
class UserReview(generics.ListAPIView):
    serializer_class = ReviewSerailizer
    
    
    # def get_queryset(self):
    #     username = self.kwargs['username']
    #     return Review.objects.filter(review_user__username=username)
    
    def get_queryset(self):
        username = self.request.query_params.get('username')
        return Review.objects.filter(review_user__username=username)
class ReviewList(generics.ListCreateAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerailizer
    # permission_classes = [IsAuthenticated]
    # throttle_classes=[ReviewListTh]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['review_user__username', 'active']

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist_app=pk)

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerailizer
    # permission_classes = [AdminOrReadOnly]
    permission_classes = [ReviewUserOrReadOnly]
       
# class ReviewDetail(mixins.RetrieveModelMixin,generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerailizer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)


# class ReviewList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
    
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerailizer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

class StreamPlatformVS(viewsets.ModelViewSet): ## ReadOnlyModelViewSet
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer
# class StreamPlatformVS(viewsets.ViewSet):
#     """
#     A simple ViewSet for listing or retrieving users.
#     """
#     def list(self, request):
#         queryset = StreamPlatform.objects.all()
#         serializer = StreamPlatformSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = StreamPlatform.objects.all()
#         watchlist = get_object_or_404(queryset, pk=pk)
#         serializer = StreamPlatformSerializer(watchlist)
#         return Response(serializer.data)
    
#     def create(self,request):
#         serializer = StreamPlatformSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
        
#     def destroy(self, request, pk=None):
#         movie = StreamPlatform.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
class StreamPlatformAV(APIView):
    
    def get(self, request):
        platform= StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platform,many=True,context={'request': request})# context use with HyperlinkedIdentityField in serializer
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    
class StreamDetailAV(APIView):
    def get(self, request,pk):
        try:
            movie = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'error':'watch list not found'},status = status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformSerializer(movie,context={'request': request})
        return Response(serializer.data)
    
    def put(self,request,pk):
        movie = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        movie = StreamPlatform.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class WatchListAV(APIView):
    def get(self,request):
        movies = WatchList.objects.all()        
        serializer = WatchListSerializer(movies,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
   
        return Response(status=status.HTTP_204_NO_CONTENT)
class WatchListGV(generics.ListAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer
    # pagination_class = WatchListLimit
    pagination_class = WatchListCursor ## must remove filter because order by create
    # pagination_class = WatchListPagination
    # filter_backends = [filters.SearchFilter]
    # filter_backends = [filters.OrderingFilter]
    # search_fields  = ['title', 'platform__name']
    # ordering_fields  = ['avg_ratings']
   
class WatchDetailAV(APIView):
    def get(self, request,pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'error':'watch list not found'},status = status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(movie)
        return Response(serializer.data)
    
    def put(self,request,pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
             
    
    
    
# @api_view(['GET',"POST"])
# def movie_list(request):
#     if request.method =='GET':
#         movies = Movies.objects.all()
#         serializer = MovieSerializer(movies,many=True)
#         return Response(serializer.data)
    
#     if request.method =='POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
        
# @api_view(['GET',"PUT","DELETE"])
# def movie_detail(request,pk):
#     if request.method =='GET':
#         try:
#             movie = Movies.objects.get(pk=pk)
#         except Movies.DoesNotExist:
#             return Response({'error':'movie not found'},status = status.HTTP_404_NOT_FOUND)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
    
#     if request.method =='PUT':
#         movie = Movies.objects.get(pk=pk)
#         serializer = MovieSerializer(movie,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     if request.method =='DELETE':
#         movie = Movies.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
        
    
    