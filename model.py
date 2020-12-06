import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from math import sqrt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import mean_squared_error, explained_variance_score, mean_absolute_error
from sklearn.linear_model import LinearRegression, TweedieRegressor, LassoLars
from sklearn.feature_selection import RFE
from sklearn.preprocessing import PolynomialFeatures
from sklearn.ensemble import IsolationForest

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

def evaluate_baseline(baseline, y_train, y_validate):
    baseline_rmse_train = round(mean_squared_error(y_train, np.full(len(y_train), baseline))**1/2, 6)
    print('RMSE (Root Mean Square Error) of Baseline on train data:\n', baseline_rmse_train)
    baseline_rmse_validate = round(mean_squared_error(y_validate, np.full(len(y_validate), baseline))**1/2, 6)
    print('RMSE (Root Mean Square Error) of Baseline on validate data:\n', baseline_rmse_validate)