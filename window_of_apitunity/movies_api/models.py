from django.db import models


class Movie(models.Model):
    title = models.CharField(name = 'title', max_length = 150)
    average_rating = models.FloatField(name = 'average_rating')
    num_votes = models.IntegerField(name = 'num_votes')
    genres  = models.CharField(name = 'genres', max_length = 50)
    runtime_minutes = models.IntegerField(name = 'runtime_minutes')