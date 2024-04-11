# Objective: Identify highest predictive risk factors of diabetes.
# For this analysis, 'Diabetes' is our target and the other columns are the features used for prediction.

# import libraries
import logging
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# set logging configurations
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

sh = logging.StreamHandler()
sh.setLevel(logging.INFO)
logger.addHandler(sh)

# load data into pandas dataframe
def load_data():
    '''
    Function to load in desired dataset and set column names.
    '''
    # set column names
    cols = ['Diabetes', 'HighBP', 'HighChol', 'CholCheck', 'BMI', 'Smoker', 'Stroke', 'HeartDiseaseorAttack', 'PhysActivity', 'Fruits', 'Veggies', 'HvyAlcoholConsump', 'AnyHealthcare', 'NoDocbcCost',
        'GenHlth', 'MentHlth', 'PhysHlth', 'DiffWalk', 'Sex', 'Age', 'Education', 'Income']
    #read in csv file
    df = pd.read_csv('C:/Users/farrj/Documents/Scripts/diabetes_data.csv', names= cols)
    
    #print(df.head())     # can uncomment to see head of dataset

    return df

def eda(df):
    '''
    Function to perform Exploratory Data Analysis (EDA).

    Can comment/uncomment sections as desired.
    '''
    # shows general desriptive statistics of dataset (mean, max, etc)
    #print(df.describe().T)

    # create a heatmap to look for missing values
    #sns.heatmap(df.isnull(), cmap= 'viridis')
    #plt.show()
    #plt.close()

    # plot histograms of each feature to view distributions
    df.hist(bins= 20, figsize= (14, 10))
    plt.tight_layout()
    plt.show()
    plt.close()

    # create a correlation matrix from the dataset and visualize with a heatmap
    #corr_db = df.corr()
    #fig = plt.figure(figsize= (12, 10))
    #sns.heatmap(corr_db.round(2), vmin= -1.0, vmax= 1.0, annot= True)
    #plt.show()
    #plt.close()

def clean_data(df):
    '''
    Function cleans/drops columns in dataset after initial EDA and reading of the codebook which can be found here: https://www.cdc.gov/brfss/annual_data/2015/pdf/codebook15_llcp.pdf.

    The following columns will be removed from our dataset prior to modeling:
    - PhysHlth: Values only indicative of individuals self-reported opinion of health within the last 30 days. We have better physical health indicators already included in other features.
    - MentHlth: Values only indicative of individuals self-reported opinion of mental health within the last 30 days.
    - BMI: Due to its biased origin (it was designed as a metric for European males), we are going to remove it from this model. An ideal situation would be to replace it with actual measurements
        for individuals.
    '''
    # columns to remove
    removed_cols = ['PhysHlth', 'MentHlth', 'BMI']

    # drop desired columns
    df_cleaned = df.drop(removed_cols, axis= 1)

    return df_cleaned

def main():

    # load in data set
    logging.info('loading diabetes dataset')
    diabetes_df = load_data()
    print(f'{len(diabetes_df)} data points loaded\n')

    # perform EDA
    logging.info('performing EDA steps')
    eda(diabetes_df)

    print(f'Key takeaways from EDA:')
    print('* No null values')
    print('* Age is by group, not by actual year')
    print('* Dataset Notebook is important for really understanding features\n')

    logging.info('cleaning data')
    diabetes_clnd = clean_data(diabetes_df)

main()