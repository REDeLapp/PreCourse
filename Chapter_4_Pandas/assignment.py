'''
Chapter 5 Assignment: Write a pandas query to answer the following questions.

Choose a nursing home ("Facility"), and subset the data by that nursing home. Answer the following using Pandas.
'''
import pandas as pd
df = pd.read_csv('beds.tsv', delimiter='\t')
subset = df.loc[df['Facility.ID'] == 17 ]

def question_zero():
    '''
    Write a pandas query that returns the highest Facility ID.

    Example:
    return df['Facility.ID'].max()

    '''
    return subset['Facility.ID'].max()


def question_one():
    '''
    Write a pandas query that returns count of how many censuses were reported.
    '''
    return len(subset['Bed.Census.Date'].unique())

def question_two():
    '''
    Write a pandas query that returns the earliest census date
    '''
    return pd.to_datetime(subset['Bed.Census.Date']).min()


def question_three():
    '''
    Write a pandas query that returns the latest census date
    '''
    return pd.to_datetime(subset['Bed.Census.Date']).max()


def question_four():
    '''
    Write a pandas query that returns  the ten census dates with the highest number of available beds for that nursing home
    '''
    top_ten subset.sort('Available.Residential.Beds', ascending = False)
    return top_ten['Bed.Census.Date'].ix[0:10]



def question_five():
    '''
    Write a pandas query that returns the ten census dates with the lowest number of available beds for that nursing home
    '''
    return None
