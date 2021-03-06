
from pyrecsys.models.als import ALS
import pandas as pd
import numpy as np

def test_als():
    #Read File
    file_path = 'ratings_small.csv'
    df = pd.read_csv(file_path, dtype='unicode')

    #Change type of data
    df.userId = df.userId.astype(int)
    df.movieId = df.movieId.astype(int)
    df.rating = df.rating.astype(float)

    #Sort Values
    df.sort_values(by=['userId','movieId'],ascending=True)

    X = df[['userId','movieId']].values
    y = df.rating.values

    #Create model instance
    model = ALS()

    #Train model
    model.fit(X,y)

    # get a prediction for specific users and items.
    uid = 1
    N = 10
    rec = model.recommend(uid,N)
    assert rec.shape[0] == N
    print("the movie_id recommend for the user_id " + str(uid) + " are ", rec)