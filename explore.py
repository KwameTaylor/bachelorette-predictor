import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
#plt.style.use('ggplot')
import matplotlib as mpl

from cycler import cycler
import seaborn as sns

# default viz size settings
plt.rc('figure', figsize=(12, 8))
plt.rc('font', size=15)
mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.linestyle'] = '--'
mpl.rcParams['axes.prop_cycle'] = cycler(color=['deepskyblue', 'firebrick', 'darkseagreen', 'violet'])

from math import sqrt
from scipy import stats

from wrangle import acquire_data, join_dfs, drop_extra_cols
from preprocessing import handle_dates_and_elims, train_validate_test

def make_heatmap(train):
    heatmap1_data = pd.pivot_table(train, values='ElimWeek', 
                     index=pd.cut(train['Age'], bins=5, precision=0), 
                     columns='Season')
    heatmap1_data.sort_index(inplace=True, ascending=False)
    sns.heatmap(heatmap1_data, cmap="RdPu", square=True)
    plt.title('Which contestants lasted more weeks, by season and age?')
    plt.show()

def firstdate_swarmplot(train):
    sns.swarmplot(x="FirstDate", y="One-on-One_Score", hue="Season", data=train, size=13)
    plt.show()

def swarmplot_by_season(train):
    sns.catplot(x="FirstDate", y="One-on-One_Score",
            col="Season", data=train, kind="swarm",
            height=4, aspect=.8, col_wrap=4)
    plt.show()

def pearsons_test(train, x, y, alpha):
    r, p = stats.pearsonr(x, y)
    print('r =', r)
    print('p =', p)
    print('\n')

    null_hypothesis = "there is no linear correlation between a contestant's One-on-One Score and a contestant's Elimination Week."

    if p < alpha:
        print("We reject the hypothesis that", null_hypothesis)
    else:
        print("We fail to reject the null hypothesis.")
