from pyrecsys.models.svd import SVD

import pandas as pd

def test_svd():
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
    model = SVD()

    #Train model
    model.fit(X,y)

    # get a prediction for specific users and items.
    #pred = model.predict(X)

    # get N recommendations for user
    uid = 1
    N = 10
    result = model.recommend(uid,N)
    assert result.shape[0] == N