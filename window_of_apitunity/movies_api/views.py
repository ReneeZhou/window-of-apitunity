from rest_framework import viewsets
from .models import Movie
from .serializers import MovieSerializer


class MovieView(viewsets.ModelViewSet):
    """
    API endpoint that allows movies to be added and rated. 
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer