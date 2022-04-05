from watchlist_app.models import Movies
from rest_framework.response import Response
from .serializers import MovieSerializer
from rest_framework.decorators import api_view

@api_view()
def movie_list(request):
    movies = Movies.objects.all()
    serializer = MovieSerializer(movies,many=True)
    return Response(serializer.data)

@api_view()
def movie_detail(request,pk):
    movie = Movies.objects.get(pk=pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)
    
