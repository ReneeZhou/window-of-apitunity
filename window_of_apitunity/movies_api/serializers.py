from rest_framework import serializers
from .models import  Movie


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Movie
        fields = (
            'title', 
            'average_rating',
            'num_votes',
            'genres', 
            'runtime_minutes'
        )