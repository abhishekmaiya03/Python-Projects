#!/usr/bin/env python
# coding: utf-8

# # Python Automation Project -- Data Cleaning App

# ## This is a Data Cleaning Application

# """
# Please create a python application that can take datasets and clean the data
# - It should ask for datasets path and name
# - it should check number of duplicats and remove all the duplicates 
# - it should keep a copy of all the duplicates
# - it should check for missing values 
# - if any column that is numeric it should replace nulls with mean else it should drop that rows
# - at end it should save the data as clean data and also return 
# - duplicates records, clean_data 
# """

# In[9]:


import pandas as pd
import numpy as np
import time
import openpyxl
import xlrd
import os
import random


# In[48]:


#data_path ='sales.xlsx'
#data_name ='jan_sales'


def data_cleaning_master(path, data_name):
    
    print("Thank you for giving the details!")
    sec=random.randint(1,4) #generating random number

    #print delay message
    print(f"Please wait for {sec} seconds! Checking file path")
    time.sleep(sec)

    
    # checking if path exists
    if not os.path.exists(data_path):
        print("Incorrect path! Try again with correct path")
        return
    else:
        # Checking the file type
        if data_path.endswith('.csv'):
            print("Dataset is CSV!")
            data=pd.read_csv(data_path, encoding_errors='ignore')
    
        
        elif data_path.endswith('.xlsx'):
            print("Dataset is excel file!")
            data=pd.read_excel(data_path)
        else:
            print("Unknown File time")
            return
    
    #print delay message
    sec=random.randint(1,4)
    print(f"Please wait for {sec} seconds! Checking total rows and columns")
    time.sleep(sec)
     
    #showing number of records
    print(f"Dataset contains total rows: {data.shape[0]}\n Total Columns: {data.shape[1]}")
    
    # start cleaning
    
    #print delay message
    sec=random.randint(1,4)
    print(f"Please wait for {sec} seconds! Checking total Duplicates")
    time.sleep(sec)
    
    #checking duplicates
    duplicates = data.duplicated()
    total_duplicate = data.duplicated().sum()
    print(f'dataset has total duplicates records: {total_duplicate}')

    #print delay message
    sec=random.randint(1,4)
    print(f"Please wait for {sec} seconds! saving total duplicate rows")
    time.sleep(sec)
    
    #saving the duplicates
    if total_duplicate>0:
        duplicate_records = data[duplicates]
        duplicate_records.to_csv(f'{data_name}_duplicates.csv', index=None)
    
    #deleting duplicates
    df = data.drop_duplicates()
    
    #print delay message
    sec=random.randint(1,10)
    print(f"Please wait for {sec} seconds! Checking for missing values")
    time.sleep(sec)
    
    # find missing values
    total_missing_value =  df.isnull().sum().sum()
    missing_values_by_columns = df.isnull().sum()
    
    print(f'Dataset have total missing value: {total_missing_value}')
    print(f'Dataset contains missing value by columns \n {missing_values_by_columns}')
    
    #dealing with missing values
    #fillna -- int/float
    #dropna -- any object type

    #print delay message
    sec=random.randint(1,4)
    print(f"Please wait for {sec} seconds! Cleaning the datasets")
    time.sleep(sec)
    
    columns=df.columns
    
    for col in columns:
        # filling mean for numeric columns all rows
        if df[col].dtype in (int, float):
            df[col]=df[col].fillna(df[col].mean())
        else:
            #dropping all rows with missing records for nonnumber col
            df.dropna(subset=col, inplace =True)
    
    
    #print delay message
    sec=random.randint(1,4)
    print(f"Please wait for {sec} seconds! Exporting datasets")
    time.sleep(sec)
    
    # dats is cleaned
    print(f"Congrats! Datasetis cleaned! Number of rows: {df.shape[0]} Number of columns: {df.shape[1]}")
    
    #saving the cleaned dataset
    df.to_csv(f'{data_name}_Clean_data.csv', index=None)
    print("Dataset is  Saved!")



# In[46]:


if __name__=="__main__":

    print("Welcoming to data cleaning master")
    # ask the path and file name
    data_path = input("Please enter dataset path: ")
    data_name = input("Please enter dataset name: ")

    #calling functions
    data_cleaning_master(data_path, data_name)
 


# In[7]:


get_ipython().system('jupyter nbconvert --to script main.ipynb')


# In[ ]:




