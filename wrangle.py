import numpy as np
import pandas as pd
import re

def acquire_data():
    '''
    This functions acquire both datasets needed for this project via .csv files.
    '''
    df = pd.read_csv('bachelorette-contestants.csv')
    join = pd.read_csv('bachelorette_edit-to-join.csv')
    return df, join

def join_dfs(df, join):
    '''
    This functions joins two Bachelorette datasets together,
    first by making the contestant names compatiable to join on.
    '''
    # Get last initials
    df['last_initial'] = df['Name'].str.extract(r'( \w{1})')
    df.last_initial = df.last_initial.fillna('X')
    # Truncate last names / get first names
    df['first_name'] = df.Name.replace(to_replace = '( )\w+.', value = '', regex = True)
    # concat newly formatted first and last names with a '_' in between
    df['CONTESTANT'] = df['first_name'].str.upper() + '_' + df['last_initial'].str.upper()
    # take out white spaces
    df.CONTESTANT = df.CONTESTANT.str.replace(" ", "")
    # add season number to front of each contestant name
    df['CONTESTANT'] = df['Season'].map(str) + '_' + df['CONTESTANT']

    # I need to take the '0's out of join.CONTESTANT to make both dataframes match before I join them.
    # replace the matching strings 
    join.CONTESTANT = join.CONTESTANT.replace(to_replace ='^0', value = '', regex = True)

    # now join the two dataframes together
    new_df = df.join(join.set_index('CONTESTANT'), on='CONTESTANT', how='inner')
    # drop unneeded features
    new_df = new_df.drop(columns=['last_initial', 'first_name', 'SEASON'])
    # set the index
    new_df = new_df.set_index('CONTESTANT')

    return new_df

def drop_extra_cols(df):
    '''
    This function drops unneeded columns/features in
    a Bachelorette data df, and returns a df.
    '''
    df = df.drop(columns=['ELIMINATION-1', 'ELIMINATION-2', 'ELIMINATION-3', 'ELIMINATION-4',
       'ELIMINATION-5', 'ELIMINATION-6', 'ELIMINATION-7', 'ELIMINATION-8',
       'ELIMINATION-9', 'ELIMINATION-10', 'Occupation', 'Name', 'DATES-1'])
    return df