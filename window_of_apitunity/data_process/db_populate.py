import pandas as pd
import gc
from movies_api.models import Movie


basics = pd.read_csv(
    'title.basics.tsv', 
    sep = '\t',
    usecols = ['tconst', 'titleType', 'primaryTitle', 'startYear', 'runtimeMinutes', 'genres'],
    na_filter = True,
    na_values = '\\N',
)
ratings = pd.read_csv(
    'title.ratings.tsv',
    sep = '\t',
)


movies = basics[basics.titleType == 'movie'][['tconst', 'primaryTitle', 'startYear', 'genres', 'runtimeMinutes']]
movies = movies.merge(ratings, on = 'tconst', how = 'left')
movies = movies.rename(columns = {
    'tconst': 'imdb_id',
    'primaryTitle': 'title',
    'startYear': 'year',
    'runtimeMinutes': 'runtime_minutes',
    'averageRating': 'average_rating', 
    'numVotes': 'num_votes'
})
movies = movies.fillna(-1)
movies.to_csv('movies.csv', index = False)
del basics, ratings
gc.collect()


movie_generator = movies.iterrows()
Movie.objects.bulk_create([Movie(**m[1]) for m in movie_generator])