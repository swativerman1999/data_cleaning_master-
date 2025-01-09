#Python Project

""""Python Automation Project -- Data Cleaning app

Requirements Please create a python application that can take datasets and clean the data

* It should ask for datasets path and name

* it should check number of duplicats and remove all the duplicates

* it should keep a copy of all the duplicates

* it should check for missing values

* if any column that is numeric it should replace nulls with mean else it should drop that rows

* at end it should save the data as clean data and also return 

* duplicates records, clean_data"""

#importing dependencies

import pandas as pd
import numpy as np
import openpyxl
import time
import xlrd
import os 
import random

# data_path = 'Employee Data.xlsx'
# data_name = 'new_data'

def data_cleaning_master(data_path, data_name):
    print("Thank you for giving the Data! ")

    sec = random.randint(1, 4) #Generating random number 

    #print delay message
    print(f"Please wait for {sec} seconds! Checking file path")
    time.sleep(sec)

    #checking the path is exists
    if not os.path.exists(data_path):
        print("Incorrect Path!, Please try again!")
        return
    else:
        #checing the file type
        if data_path.endswith('.csv'):
            print('Dataset is csv!')
            data = pd.read_csv(data_path, encoding_errors='egnore')

        elif data_path.endswith('.xlsx'):
            print('Dataset is xlsx!')
            data = pd.read_excel(data_path)

        else:
            print('Unknown file type') 
            return   

    sec = random.randint(1, 4)
    #print delay message
    print(f"Please wait for {sec} seconds! Checking total rows and columns")
    time.sleep(sec)

    #showing number of records
    print(f"Total Number of rows: {data.shape[0]} \n Total Columns {data.shape[0]}")

    #cleaning

    sec = random.randint(1, 4)
    #print delay message
    print(f"Please wait for {sec} seconds! checking total duplicates ")
    time.sleep(sec)

    # checking duplicates
    duplicates = data.duplicated()
    total_duplicate = data.duplicated().sum()

    print(f" Datasets has Total Number of duplicate records: {total_duplicate}")

    sec = random.randint(1, 4)
    #print delay message
    print(f"Please wait for {sec} seconds! saving total duplicates rows")
    time.sleep(sec)


    #saving the Duplicates
    if total_duplicate > 0:
        duplicate_recods = data[duplicates]
        duplicate_recods.to_csv(f"{data_name}_duplicates.csv",index=None)

    #Deleting Duplicates

    df = data.drop_duplicates()

    sec = random.randint(1, 4)
    #print delay message
    print(f"Please wait for {sec} seconds! Checking for missing records")
    time.sleep(sec)

    #Find Missing Value

    total_missing_value = df.isnull().sum().sum()
    missing_value_by_column = df.isnull().sum()

    print(f" Dataset has total missing values : {total_missing_value}")
    print(f" Dataset has missing values by each column: {missing_value_by_column}")

    #dealing with missing value
    #filling - int and float
    #dropna - any object 

    sec = random.randint(1, 7)
    #print delay message
    print(f"Please wait for {sec} seconds! Cleaning the datasets")
    time.sleep(sec)

    columns = df.columns

    for col in columns:
        # filling mean for numeric columns all rows
        if df[col].dtype in (float, int):
            df[col] = df[col].fillna(df[col].mean())

        else:
            #dropping all rows with missing records for non number col
            df.dropna(subset=col, inplace=True)

    sec = random.randint(1, 4)
    #print delay message
    print(f"Please wait for {sec} seconds! Exporting Datasets")
    time.sleep(sec)

    # data is cleaned now
    print(f"Congrats! Dataset is cleaned! Number of Rows: {df.shape[0]} Number of columns: {df.shape[1]}")

    
    #saving the clean dataset
    df.to_csv(f"{data_name}_Clean_data.csv", index=None)
    print("Yeah, Dataset is saved!")

if __name__ == "__main__":

    print("Welcome to Data Cleaning Master!")
    #ask path and file name
    data_path = input("Please enter database path:")
    data_name = input("Please enter dataset name:")

    #Calling the function
    data_cleaning_master(data_path, data_name)
    


