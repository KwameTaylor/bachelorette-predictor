import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from math import sqrt

from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.cluster import KMeans
from sklearn.metrics import mean_squared_error, explained_variance_score, mean_absolute_error
from sklearn.linear_model import LinearRegression, TweedieRegressor, LassoLars
from sklearn.feature_selection import RFE
from sklearn.preprocessing import PolynomialFeatures
from sklearn.ensemble import IsolationForest, RandomForestRegressor

def model_1(X, y, X_v, y_v):
    # create the model object
    lm = LinearRegression(normalize=True)

    # fit the model to our training data.
    lm.fit(X, y)

    # predict on train
    lm_pred = lm.predict(X)
    # compute root mean squared error
    lm_rmse = mean_squared_error(y, lm_pred)**1/2

    # predict on validate
    lm_pred_v = lm.predict(X_v)
    # compute root mean squared error
    lm_rmse_v = mean_squared_error(y_v, lm_pred_v)**1/2

    print("RMSE for OLS using LinearRegression\n\nOn train data:\n", round(lm_rmse, 6), '\n\n', 
        "On validate data:\n", round(lm_rmse_v, 6))

    return lm_pred, lm_rmse, lm_pred_v, lm_rmse_v

def model_2(X, y, X_v, y_v):
    # create the model object
    lars = LassoLars(alpha=1.0)

    # fit the model to our training data. We must specify the column in y_train, 
    # since we have converted it to a dataframe from a series! 
    lars.fit(X, y)

    # predict train
    pred_lars = lars.predict(X)

    # evaluate: rmse
    rmse_train = mean_squared_error(y, pred_lars)**1/2

    # predict validate
    pred_lars_v = lars.predict(X_v)

    # evaluate: rmse
    rmse_validate = mean_squared_error(y_v, pred_lars_v)**1/2

    print("RMSE for Lasso + Lars\n\nOn train data:\n", round(rmse_train, 6), '\n\n', 
            "On validate data:\n", round(rmse_validate , 6))

    return pred_lars, rmse_train, pred_lars_v, rmse_validate

def model_3(X, y, X_v, y_v):
    # create the model object
    lm = LinearRegression(normalize=True)

    # fit the model to our training data
    lm.fit(X, y)

    # predict on train
    lm_pred = lm.predict(X)
    # compute root mean squared error
    lm_rmse = mean_squared_error(y, lm_pred)**1/2

    # predict on validate
    lm_pred_v = lm.predict(X_v)
    # compute root mean squared error
    lm_rmse_v = mean_squared_error(y_v, lm_pred_v)**1/2

    print("RMSE for OLS using LinearRegression\n\nOn train data:\n", round(lm_rmse, 6), '\n\n', 
        "On validate data:\n", round(lm_rmse_v, 6))

    return lm_pred, lm_rmse, lm_pred_v, lm_rmse_v

def model_4(X, y, X_v, y_v):
    # create the model object
    forest = RandomForestRegressor()

    # fit the model to our training data
    forest.fit(X, y)

    # predict on train
    forest_pred = forest.predict(X)
    # compute root mean squared error
    forest_rmse = mean_squared_error(y, forest_pred)**1/2

    # predict on validate
    forest_pred_v = forest.predict(X_v)
    # compute root mean squared error
    forest_rmse_v = mean_squared_error(y_v, forest_pred_v)**1/2

    print("RMSE for RandomForestRegressor\n\nOn train data:\n", round(forest_rmse, 6), '\n\n', 
    "On validate data:\n", round(forest_rmse_v, 6))

    return forest_pred, forest_rmse, forest_pred_v, forest_rmse_v

def model_5(X, y, X_v, y_v):
    # create the model object
    forest = RandomForestRegressor()

    # fit the model to our training data
    forest.fit(X, y)

    # predict on train
    forest_pred = forest.predict(X)
    # compute root mean squared error
    forest_rmse = mean_squared_error(y, forest_pred)**1/2

    # predict on validate
    forest_pred_v = forest.predict(X_v)
    # compute root mean squared error
    forest_rmse_v = mean_squared_error(y_v, forest_pred_v)**1/2

    print("RMSE for RandomForestRegressor\n\nOn train data:\n", round(forest_rmse, 6), '\n\n', 
    "On validate data:\n", round(forest_rmse_v, 6))

    return forest_pred, forest_rmse, forest_pred_v, forest_rmse_v

def model_1_test(X, y):
    # create the model object
    lm = LinearRegression(normalize=True)

    # fit the model to our training data.
    lm.fit(X, y)

    # predict on test
    lm_pred = lm.predict(X)
    # compute root mean squared error
    lm_rmse = mean_squared_error(y, lm_pred)**1/2

    print("RMSE for OLS using LinearRegression\n\nOn test data:\n", round(lm_rmse, 6))

    return lm_pred, lm_rmse

def model_4_test(X, y):
    # create the model object
    forest = RandomForestRegressor()

    # fit the model to our training data
    forest.fit(X, y)

    # predict on test
    forest_pred = forest.predict(X)
    # compute root mean squared error
    forest_rmse = mean_squared_error(y, forest_pred)**1/2

    print("RMSE for RandomForestRegressor\n\nOn test data:\n", round(forest_rmse, 6))

    return forest_pred, forest_rmse

def evaluate_baseline(baseline, y_train, y_validate):
    baseline_rmse_train = round(mean_squared_error(y_train, np.full(len(y_train), baseline))**1/2, 6)
    print('RMSE (Root Mean Square Error) of Baseline on train data:\n', baseline_rmse_train)
    baseline_rmse_validate = round(mean_squared_error(y_validate, np.full(len(y_validate), baseline))**1/2, 6)
    print('RMSE (Root Mean Square Error) of Baseline on validate data:\n', baseline_rmse_validate)