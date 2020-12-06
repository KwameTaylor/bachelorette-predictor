import numpy as np
import pandas as pd

import sklearn.preprocessing
from sklearn.preprocessing import MinMaxScaler, PolynomialFeatures
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LassoLars, TweedieRegressor

def remove_Ds(df, col):
    '''
    This functions removes the 'D' at the
    beginning of the DATES columns' strings.
    '''
    df[col] = df[col].replace(to_replace = r'D', value = '', regex = True)
    return df

def calculate_dates(df, col, new_col_name):
    '''
    This function takes in a df, a DATES column name,
    and the name of a new column (such as 'Dates2-Calculated').
    It returns a df with the calculated value of
    a contestant's date per episode in the new columns.

    Value of a date is equal to:
    1 divided by the number of people on the date.
    '''
    try:
        df[new_col_name] = 1 / df[col]
    except ZeroDivisionError:
        df[new_col_name] = 0
    return df

def calculate_score(df):
    '''
    This function calculates the One-on-One Score for each contestant.
    '''
    df['One-on-One_Score'] = (df['Dates2-Calculated'] + df['Dates3-Calculated'] + df['Dates4-Calculated'] + df['Dates5-Calculated'] + df['Dates6-Calculated'] + df['Dates7-Calculated'] + df['Dates8-Calculated'] + df['Dates9-Calculated'] + df['Dates10-Calculated']) / (df['ElimWeek'] + 1.0)
    return df

def get_first_date(df):
    '''
    This functions add the feature FirstDate.
    1 represents that the contestant had a date with the
    bachelorette in week 2, which is the first week available
    for having dates.
    0 means no date on week 2.
    '''
    df.loc[df['DATES-2'] > 0.0, 'FirstDate'] = 1.0
    df = df.fillna(0)
    return df

def handle_dates_and_elims(df):
    '''
    This function takes in a Bachelorette df
    and returns a df with the DATES and ELIMINATION
    features handled and engineered.
    '''
    # NaN represents that that contestant won that season.
    # I will encode this as 11.0, representing that the
    # contestants lasted to the end of their season of the show.
    df.ElimWeek = df[['ElimWeek']].fillna(11.0)

    # remove Ds from beginning of DATES strings
    # so it can be turned into a float for calculation
    df = remove_Ds(df, 'DATES-2')
    df = remove_Ds(df, 'DATES-3')
    df = remove_Ds(df, 'DATES-4')
    df = remove_Ds(df, 'DATES-5')
    df = remove_Ds(df, 'DATES-6')
    df = remove_Ds(df, 'DATES-7')
    df = remove_Ds(df, 'DATES-8')
    df = remove_Ds(df, 'DATES-9')
    df = remove_Ds(df, 'DATES-10')

    # convert DATES strings to floats
    df["DATES-2"] = pd.to_numeric(df["DATES-2"], downcast="float")
    df["DATES-3"] = pd.to_numeric(df["DATES-3"], downcast="float")
    df["DATES-4"] = pd.to_numeric(df["DATES-4"], downcast="float")
    df["DATES-5"] = pd.to_numeric(df["DATES-5"], downcast="float")
    df["DATES-6"] = pd.to_numeric(df["DATES-6"], downcast="float")
    df["DATES-7"] = pd.to_numeric(df["DATES-7"], downcast="float")
    df["DATES-8"] = pd.to_numeric(df["DATES-8"], downcast="float")
    df["DATES-9"] = pd.to_numeric(df["DATES-9"], downcast="float")
    df["DATES-10"] = pd.to_numeric(df["DATES-10"], downcast="float")

    # Now I'll fill the rest of the NaNs (just present in the dates features) with 0.
    df = df.fillna(0)

    # calcuate the contestant's date scores per episode and add that feature
    df = calculate_dates(df, 'DATES-2', 'Dates2-Calculated')
    df = calculate_dates(df, 'DATES-3', 'Dates3-Calculated')
    df = calculate_dates(df, 'DATES-4', 'Dates4-Calculated')
    df = calculate_dates(df, 'DATES-5', 'Dates5-Calculated')
    df = calculate_dates(df, 'DATES-6', 'Dates6-Calculated')
    df = calculate_dates(df, 'DATES-7', 'Dates7-Calculated')
    df = calculate_dates(df, 'DATES-8', 'Dates8-Calculated')
    df = calculate_dates(df, 'DATES-9', 'Dates9-Calculated')
    df = calculate_dates(df, 'DATES-10', 'Dates10-Calculated')

    # Replace any inf values with NaN
    # where the try and except did not catch the division by zero error
    df = df.replace([np.inf, -np.inf], np.nan)

    # Then replace those NaNs with 0
    df = df.fillna(0)

    # Get one-on-one score feature
    df = calculate_score(df)

    # Get firstdate feature
    df = get_first_date(df)

    # Drop the features that are unneeded now that we have our newly engineered features
    df = df.drop(columns=['DATES-2', 'DATES-3', 'DATES-4', 'DATES-5',
       'DATES-6', 'DATES-7', 'DATES-8', 'DATES-9', 'DATES-10',
       'Dates2-Calculated', 'Dates3-Calculated', 'Dates4-Calculated',
       'Dates5-Calculated', 'Dates6-Calculated', 'Dates7-Calculated',
       'Dates8-Calculated', 'Dates9-Calculated', 'Dates10-Calculated'])

    return df

def train_validate_test_auto(df, target):
    '''
    This function takes in a dataframe and splits it into test (20%), validate (24%), and train (56%). 
    It also splits test, validate, and train into X and y dataframes.
    '''
    # split df into test (20%) and train_validate (80%)
    train_validate, test = train_test_split(df, stratify=df[target], test_size=.2, random_state=666)

    # split train_validate off into train (70% of 80% = 56%) and validate (30% of 80% = 24%)
    train, validate = train_test_split(train_validate, test_size=.3, random_state=666)
        
    # split train into X & y
    X_train = train.drop(columns=[target])
    y_train = train[target]
    
    # split validate into X & y
    X_validate = validate.drop(columns=[target])
    y_validate = validate[target]
    
    # split test into X & y
    X_test = test.drop(columns=[target])
    y_test = test[target]
    
    print('Shape of train:', X_train.shape, '| Shape of validate:', X_validate.shape, '| Shape of test:', X_test.shape)

    return X_train, y_train, X_validate, y_validate, X_test, y_test, train, validate, test

def train_validate_test_manual(df, target):
    '''
    This function manually splits the df into
    train (63.636%), validate (18.182%), and test (18.182%),
    splitting down ElimWeek values chronologically.
    '''
    # split df into train, validate, and test
    train = df[df['ElimWeek'] <= 7.0]
    validate = df.loc[(df.ElimWeek == 8.0) | (df.ElimWeek == 9.0)]
    test = df.loc[(df.ElimWeek == 10.0) | (df.ElimWeek == 11.0)]
        
    # split train into X & y
    X_train = train.drop(columns=[target])
    y_train = train[target]
    
    # split validate into X & y
    X_validate = validate.drop(columns=[target])
    y_validate = validate[target]
    
    # split test into X & y
    X_test = test.drop(columns=[target])
    y_test = test[target]
    
    print('Shape of train:', X_train.shape, '| Shape of validate:', X_validate.shape, '| Shape of test:', X_test.shape)

    return X_train, y_train, X_validate, y_validate, X_test, y_test, train, validate, test

def train_validate_test(df, target):
    '''
    This function manually splits the df into
    train (66.67%), validate (16.667%), and test (16.667%),
    splitting down Seasons.
    '''
    # split df into train, validate, and test
    train = df[df['Season'] <= 8]
    validate = df.loc[(df.Season == 9) | (df.Season == 10)]
    test = df.loc[(df.Season == 11) | (df.Season == 12)]
        
    # split train into X & y
    X_train = train.drop(columns=[target])
    y_train = train[target]
    
    # split validate into X & y
    X_validate = validate.drop(columns=[target])
    y_validate = validate[target]
    
    # split test into X & y
    X_test = test.drop(columns=[target])
    y_test = test[target]
    
    print('Shape of train:', X_train.shape, '| Shape of validate:', X_validate.shape, '| Shape of test:', X_test.shape)

    return X_train, y_train, X_validate, y_validate, X_test, y_test, train, validate, test

def parse_hometowns(df):
    '''
    This function takes in a df and returns a df
    with Homestate abbrevations as a new feature,
    and HomeRegion as a new feature.
    '''
    states_regions = {
            'AK': 'O',
            'AL': 'S',
            'AR': 'S',
            'AS': 'O',
            'AZ': 'W',
            'CA': 'W',
            'CO': 'W',
            'CT': 'N',
            'DC': 'N',
            'DE': 'N',
            'FL': 'S',
            'GA': 'S',
            'GU': 'O',
            'HI': 'O',
            'IA': 'M',
            'ID': 'W',
            'IL': 'M',
            'IN': 'M',
            'KS': 'M',
            'KY': 'S',
            'LA': 'S',
            'MA': 'N',
            'MD': 'N',
            'ME': 'N',
            'MI': 'W',
            'MN': 'M',
            'MO': 'M',
            'MP': 'O',
            'MS': 'S',
            'MT': 'W',
            'NA': 'O',
            'NC': 'S',
            'ND': 'M',
            'NE': 'W',
            'NH': 'N',
            'NJ': 'N',
            'NM': 'W',
            'NV': 'W',
            'NY': 'N',
            'OH': 'M',
            'OK': 'S',
            'OR': 'W',
            'PA': 'N',
            'PR': 'O',
            'RI': 'N',
            'SC': 'S',
            'SD': 'M',
            'TN': 'S',
            'TX': 'S',
            'UT': 'W',
            'VA': 'S',
            'VI': 'O',
            'VT': 'N',
            'WA': 'W',
            'WI': 'M',
            'WV': 'S',
            'WY': 'W'
    }

    us_state_abbrev = {
        'Alabama': 'AL',
        'Alaska': 'AK',
        'American Samoa': 'AS',
        'Arizona': 'AZ',
        'Arkansas': 'AR',
        'California': 'CA',
        'Colorado': 'CO',
        'Connecticut': 'CT',
        'Delaware': 'DE',
        'District of Columbia': 'DC',
        'Florida': 'FL',
        'Georgia': 'GA',
        'Guam': 'GU',
        'Hawaii': 'HI',
        'Idaho': 'ID',
        'Illinois': 'IL',
        'Indiana': 'IN',
        'Iowa': 'IA',
        'Kansas': 'KS',
        'Kentucky': 'KY',
        'Louisiana': 'LA',
        'Maine': 'ME',
        'Maryland': 'MD',
        'Massachusetts': 'MA',
        'Michigan': 'MI',
        'Minnesota': 'MN',
        'Mississippi': 'MS',
        'Missouri': 'MO',
        'Montana': 'MT',
        'Nebraska': 'NE',
        'Nevada': 'NV',
        'New Hampshire': 'NH',
        'New Jersey': 'NJ',
        'New Mexico': 'NM',
        'New York': 'NY',
        'North Carolina': 'NC',
        'North Dakota': 'ND',
        'Northern Mariana Islands':'MP',
        'Ohio': 'OH',
        'Oklahoma': 'OK',
        'Oregon': 'OR',
        'Pennsylvania': 'PA',
        'Puerto Rico': 'PR',
        'Rhode Island': 'RI',
        'South Carolina': 'SC',
        'South Dakota': 'SD',
        'Tennessee': 'TN',
        'Texas': 'TX',
        'Utah': 'UT',
        'Vermont': 'VT',
        'Virgin Islands': 'VI',
        'Virginia': 'VA',
        'Washington': 'WA',
        'West Virginia': 'WV',
        'Wisconsin': 'WI',
        'Wyoming': 'WY'
    }

    for key in us_state_abbrev:
        df.loc[df['Homestate'].str.contains(key), 'HomestateAbbr'] = us_state_abbrev[key]

    for key in states_regions:
        df.loc[df['HomestateAbbr'].str.contains(key), 'HomeRegion'] = states_regions[key]

    return df