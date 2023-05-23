# importing relevant libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

from sklearn.model_selection import train_test_split,cross_val_score,GridSearchCV
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OrdinalEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,roc_auc_score,ConfusionMatrixDisplay,classification_report
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.feature_selection import RFECV
from sklearn.ensemble import GradientBoostingClassifier
import joblib




def explore(data_frame):
    """
    Prints the Shape, Summary information and Column names of a given DataFrame.

    Parameters:
    - data_frame (pandas.DataFrame): The DataFrame to be explored.

    Returns:
    - None
    """
    print(data_frame.shape)
    print('================================================================')
    print(data_frame.info())
    print('================================================================')
    print(data_frame.columns)




def hist_plot(data_frame, column):
    """
    Creates a countplot to visualize the distribution of values in a categorical column of a DataFrame.

    Parameters:
        data_frame (pandas.DataFrame): The DataFrame containing the data.
        column (str): The name of the column from the DataFrame to plot.

    Returns:
        None
    """
    sns.set_style("whitegrid") 
    plt.figure(figsize=(5, 3))
    sns.countplot(data=data_frame, y=data_frame[column])
    plt.title(f'{(column)} Countplot')
    plt.show();