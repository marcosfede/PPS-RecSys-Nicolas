# Base class Surprise for all Metods of Surprise

from surprise import SVD as surprise_svd
from surprise import dataset
from surprise import Reader
import pandas as pd

from .base import PredictionModel

class MyDataset(dataset.DatasetAutoFolds):

    def __init__(self, df, reader):

        self.raw_ratings = [(uid, iid, r, None) for (uid, iid, r) in
                            zip(df[df.columns.values[0]], df[df.columns.values[1]], df[df.columns.values[2]])]
        self.reader=reader

class SurpriseWrapper(PredictionModel):
    def __init__(self, model):
        self.model = model()
        self.trainset = None

    def fit(self,X,y):
        data = {'userId': X[:,0], 'itemId': X[:,1], 'rating': y.values}
        #Convert data to Surprise trainset using Pandas
        df = pd.DataFrame.from_dict(data)
        reader = Reader(line_format='user item rating', rating_scale=(1, 5))
        data = MyDataset(df, reader)
        trainset_for_surprise = data.build_full_trainset()
        self.trainset = trainset_for_surprise #save trainset
        self.model.fit(trainset_for_surprise) #fit model
    
    def predict(self,user_id,item_id):
        #inner_uid = self.trainset.to_inner_uid(user_id)
        #inner_iid = self.trainset.to_inner_iid(item_id)
        #return self.model.predict(inner_uid,inner_iid).est
        return self.model.predict(user_id,item_id).est
        #print("Users: ",self.model.trainset.n_users)
        #print("Items: ",self.model.trainset.n_items)
        #print("Ratings: ",self.model.trainset.n_ratings)
        #print(self.trainset._raw2inner_id_users)

    def recommend(self,user_id):
        return None