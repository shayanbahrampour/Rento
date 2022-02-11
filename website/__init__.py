from sklearn.linear_model import LinearRegression
from flask import Flask
import numpy as np
import random
import pandas as pd
from sklearn.model_selection import train_test_split






def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']='secret key'
    
    from .views import views

    app.register_blueprint(views,url_prefix='/')
    return app



def rento(home):
    
    manhattan=pd.read_csv('./website/static/manhattan.csv')
    queens=pd.read_csv('./website/static/queens.csv')
    brooklyn=pd.read_csv('./website/static/brooklyn.csv')


    if home[3]=="Manhattan":
        x= manhattan[['size_sqft','bedrooms','bathrooms']]
        y = manhattan[['rent']]
    elif home[3]=="Queens":
        x=queens[['size_sqft','bedrooms','bathrooms']]
        y = queens[['rent']]
    elif home[3]=="Brooklyn":
        x=brooklyn[['size_sqft','bedrooms','bathrooms']]
        y = brooklyn[['rent']]
    

        

    
    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.8, test_size = 0.2, random_state=6)

    model=LinearRegression()
    model.fit(x_train,y_train)

    size=home[0]
    bedrooms=home[1]
    bathrooms=home[2]

    home_prediction=[[size,bedrooms,bathrooms]]
    y_prediction=model.predict(home_prediction)

    returns=[]
    returns.append(y_prediction)
    returns.append(model.score(x_train,y_train))
    return returns