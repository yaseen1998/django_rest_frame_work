from watchlist_app.models import Movies
from rest_framework.response import Response
from .serializers import MovieSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.views.decorators.vary import vary_on_cookie, vary_on_headers
# @api_view()
class Movie_list(APIView):
    @method_decorator(cache_page(60*60*2))
    # @method_decorator(vary_on_cookie)
    def get(self,request):
        movies = Movies.objects.all()
        serializer = MovieSerializer(movies,many=True)
        cache.set('my_key', serializer.data, 3000)
        return Response(serializer.data)

@api_view()
def movie_detail(request,pk):
    movie = Movies.objects.get(pk=pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)
    

class ClearCacheing(APIView):
    def get(self,request):
        # cache.clear()
        cache.get('my_key')
        return Response({'clear':cache.get('my_key')})

