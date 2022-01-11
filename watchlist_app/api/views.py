from watchlist_app.models import WatchList,StreamPlatform,Review
from rest_framework.response import Response
from .serializers import WatchListSerializer,StreamPlatformSerializer,ReviewSerailizer
from rest_framework.decorators import api_view
from rest_framework import status,mixins,generics
from rest_framework.views import APIView



class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerailizer
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        watchlist = WatchList.objects.get(pk=pk)
        serializer.save(watchlist_app = watchlist)
class ReviewList(generics.ListCreateAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerailizer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist_app=pk)

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerailizer
       
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
        
    
    