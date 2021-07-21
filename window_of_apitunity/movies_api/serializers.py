from rest_framework import serializers
from .models import  Movie


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Movie
        fields = (
            'imdb_id',
            'title', 
            'year', 
            'genres', 
            'runtime_minutes',
            'average_rating',
            'num_votes',
        )