from django.db import models


class Movie(models.Model):
    imdb_id = models.CharField(name = 'imdb_id', max_length = 15)
    title = models.CharField(name = 'title', max_length = 150)
    year = models.SmallIntegerField(name = 'year')
    genres  = models.CharField(name = 'genres', max_length = 50)
    runtime_minutes = models.IntegerField(name = 'runtime_minutes')
    average_rating = models.FloatField(name = 'average_rating')
    num_votes = models.IntegerField(name = 'num_votes')