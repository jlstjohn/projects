# Objective: Identify highest predictive risk factors of diabetes.
# For this analysis, 'Diabetes' is our target and the other columns are the features used for prediction.

# import libraries
import logging
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_squared_error, classification_report, accuracy_score, precision_score, recall_score, confusion_matrix
from sklearn.metrics import roc_auc_score, roc_curve
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

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
    # read in csv file (from local)
    #df = pd.read_csv('C:/Users/farrj/Documents/Scripts/diabetes_data.csv', names= cols)
    
    # read in csv file (from github)
    url = 'https://github.com/jlstjohn/projects/blob/jlstjohn-patch-1/machineLearning/diabetesDataExploration/data/diabetes_data.csv?raw=true'
    df = pd.read_csv(url, index_col= False, names= cols)
    
    print(df.head())     # can uncomment to see head of dataset

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
    #df.hist(bins= 20, figsize= (14, 10))
    #plt.tight_layout()
    #plt.show()
    #plt.close()

    # create a correlation matrix from the dataset and visualize with a heatmap
    corr_db = df.corr()
    fig = plt.figure(figsize= (12, 10))
    sns.heatmap(corr_db.round(2), cmap= 'PiYG', vmin= -1.0, vmax= 1.0, annot= True)
    #plt.show()
    plt.close()

def clean_data(df, labels):
    '''
    Function cleans dataset by dropping desired columns. 
    '''
    # columns to remove
    removed_cols = labels

    # drop desired columns
    df_cleaned = df.drop(columns= removed_cols)
    
    # optional print to verify
    #print(df_cleaned)

    return df_cleaned
    
def get_top_features(df):
    '''
    Function creates a dataframe of the correlation coefficient information to narrow down top three correlated features.
    '''
    # create correlation matrix of features and target
    corr_db = df.corr()
    corr_db.round(2)
    nrows, ncols = corr_db.shape
    
    corr_df = corr_db.stack().reset_index()
    corr_df.columns = ['var1', 'var2', 'correlation']
    #print(corr_df.head())
    
    # drop duplicates
    corr_df = corr_df[corr_df.var2 > corr_df.var1]
    
    corr_df = corr_df.loc[corr_df.correlation.abs().sort_values(ascending= False).index]
    top_features = corr_df[(corr_df.var1 == 'Diabetes' ) | (corr_df.var2 == 'Diabetes')]
    #print(top_features.head(5))
    three_features = top_features[0:3]
    
    return three_features

def main():
    # TODO::::
    # CREATE USER INPUT FUNCTIONALITY FOR INTERACTING WITH EDA FUNCTIONS
    # ADD DEBUG FILE AND TRY/CATCH ERRORS/TEST FILES

    # load in data set
    logging.info('loading diabetes dataset')
    diabetes_df = load_data()
    print(f'{len(diabetes_df)} data points loaded\n')

    # perform EDA
    logging.info('performing EDA steps')
    #eda(diabetes_df)
    # rework this part for user input

    print('Key takeaways from initial (1st) EDA:')
    print('* No null values')
    print('* Age is by group, not by actual year')
    print('* Dataset Notebook is important for really understanding features\n')
    # add more info here as to why data is cleaned? or user option to view detailed info on why data was cleaned?
    '''
    After initial EDA and reading of the codebook which can be found here: https://www.cdc.gov/brfss/annual_data/2015/pdf/codebook15_llcp.pdf.

    The following columns will be removed from our dataset prior to modeling:
    - PhysHlth: Values only indicative of individuals self-reported opinion of health within the last 30 days. We have better physical health indicators already included in other features.
    - MentHlth: Values only indicative of individuals self-reported opinion of mental health within the last 30 days.
    - BMI: Due to its biased origin (it was designed as a metric for European males), we are going to remove it from this model. An ideal situation would be to replace it with actual measurements
        for individuals.
    '''

    logging.info('cleaning data')
    remove_feats = ['PhysHlth', 'MentHlth', 'BMI']
    diabetes_clnd = clean_data(diabetes_df, remove_feats)
    
    # optional EDA (change up for user question?)
    #logging.info('performing 2nd EDA on cleand_data')
    #eda(diabetes_clnd)
    # observations here (tied with user input) about correlation matrix: a few that are slightly higher
    # correlated than others, but nothing that jumps out 
    # general health and diffwalk moderately correlated: remove at least one
    # income and education moderately correlated: remove one
    # gen health is moderately correlated with a few other features and when it comes to being a predictor, is not very informative, so we will remove both
    # income higher corrlation with target, keep this
    print('Key takeaways from 2nd EDA:')
    print('* A few moderately correlated variables with target, no highly correlated variables')
    print('* Some features are correlated with each other, select some to remove')
    
    # remove other columns and perform eda again
    logging.info('cleaning data, second time')  # maybe change function name to drop columns?
    remove_feats = ['DiffWalk', 'Education', 'GenHlth']
    diabetes_final = clean_data(diabetes_clnd, remove_feats)
    #logging.info('performing 3rd EDA on diabetes_final')
    eda(diabetes_final)
    print(diabetes_final.info())
    
    logging.info('prepping data for obtaining top 3 features')
    top_feats = get_top_features(diabetes_final)
    print(top_feats)
    print(diabetes_final.columns)
    #print(diabetes_final.Income.value_counts())
    
    # pick single feature for logistic regression
    # create a data frame with just that feature and split target ('Diabetes') into separate dataframe
    logging.info('prepping dataframes for Logistic Regression Model')
    logging.info('using feature HighBP as target (Diabetes) predictor')
    X_HighBP = pd.get_dummies(diabetes_final, columns= ['HighBP'], drop_first= True, dtype= float)
    Y_Target = np.ravel(diabetes_final[['Diabetes']])
    # (move this comment)convert datatype for HighBP to categorical
    
    pipe = make_pipeline(StandardScaler(), LogisticRegression())
    
    
    x_train_logreg, x_test_logreg, y_train_logreg, y_test_logreg = train_test_split(X_HighBP, Y_Target, test_size= 0.20, random_state= 247)
    print(x_train_logreg.shape, x_test_logreg.shape)
    print(y_train_logreg.shape, y_test_logreg.shape)
    print(x_train_logreg.head())
    
    
    logging.info('instantiating/fitting LogReg Model')
    logreg_model = pipe.fit(x_train_logreg, y_train_logreg)
    
    #logging.info('fitting LogReg Model')
    #logreg_model.fit(x_train_logreg, y_train_logreg)
    
    logging.info('calculating predictions')
    #logreg_preds = logreg_model.predict(x_train_logreg)
    logreg_preds = cross_val_predict(estimator= logreg_model, X= x_train_logreg, y= y_train_logreg, method= 'predict_proba')
    
    print('*** Logistic Regression ***')
    print('\nConfusion Matrix:')
    print(confusion_matrix(y_true= y_train_logreg, y_pred= logreg_preds[:, 1] >= 0.5))
    print('\nClassification Report:')
    print(classification_report(y_true= y_train_logreg, y_pred= logreg_preds[:, 1] >= 0.5))
    print('\nROC-AUC Score:')
    print(roc_auc_score(y_true= y_train_logreg, y_score= logreg_preds[:, 1]))
    print('\n')
    fpr, tpr, thresh = roc_curve(y_true= y_train_logreg, y_score= logreg_preds[:, 1])
    plt.figure(figsize= (8, 8), num= 1)
    plt.plot(fpr, tpr, linewidth= 2)
    plt.plot([(0, 0), (1, 1)], 'k--')
    plt.title('Logistic Regression ROC Curve')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.show()
    print('\n')
    
    
    # fit DecisionTree
    # fit RandomForest
    
    

main()