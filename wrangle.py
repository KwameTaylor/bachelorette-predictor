import numpy as np
import pandas as pd
import re

def acquire_data():
    df = pd.read_csv('bachelorette-contestants.csv')
    join = pd.read_csv('bachelorette_edit-to-join.csv')
    return df, join

def clean_names(df, join):
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