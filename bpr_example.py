from models.bpr import LightFM_BPR
from model_selection.cross_validation import cross_validation
#from model_selection.grid_search_cv import grid_search_cv
import pandas as pd
import numpy as np

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
y = df.rating

#Create model instance
model = LightFM_BPR()

#Train model
model.fit(X,y)

# get a prediction for specific users and items.
uid = 1
iid = 31
pred = model.predict(uid, iid)
print("the prediction for the user " + str(uid) + " and the item " + str(iid) + " is " + str(pred))

#Run 5-fold Cross-Validation
X = X.copy(order='C')
#print(X.flags)
#print(y.values.flags)
cross_validation(model,X,y,cv=5)
#grid_search_cv(model,X,y,)