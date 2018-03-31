'''
Defining DataFrame Functions for ipython notebooks
'''
import pandas as pd 
import csv
import numpy as np


def Gender_Age_2017(): 
    Data_2017 = pd.read_csv("../Raw_Data/Gender_Age_Data/DataFrames/Profession_Age_Gender_2017.csv")
    Gender_Age_2017_DF = pd.DataFrame(Data_2017)
    return Gender_Age_2017_DF

def Gender_Age_2016(): 
    Data_2016 = pd.read_csv("../Raw_Data/Gender_Age_Data/DataFrames/Profession_Age_Gender_2016.csv")
    Gender_Age_2016_DF = pd.DataFrame(Data_2016)
    return Gender_Age_2016_DF

def Gender_Age_2015(): 
    Data_2015 = pd.read_csv("../Raw_Data/Gender_Age_Data/DataFrames/Profession_Age_Gender_2015.csv")
    Gender_Age_2015_DF = pd.DataFrame(Data_2015)
    return Gender_Age_2015_DF

def Gender_Age_2014(): 
    Data_2014 = pd.read_csv("../Raw_Data/Gender_Age_Data/DataFrames/Profession_Age_Gender_2014.csv")
    Gender_Age_2014_DF = pd.DataFrame(Data_2014)
    return Gender_Age_2014_DF

def Gender_Age_2013(): 
    Data_2013 = pd.read_csv("../Raw_Data/Gender_Age_Data/DataFrames/Profession_Age_Gender_2013.csv")
    Gender_Age_2013_DF = pd.DataFrame(Data_2013)
    return Gender_Age_2013_DF

def Gender_Age_2012(): 
    Data_2012 = pd.read_csv("../Raw_Data/Gender_Age_Data/DataFrames/Profession_Age_Gender_2012.csv")
    Gender_Age_2012_DF = pd.DataFrame(Data_2012)
    return Gender_Age_2012_DF

def Gender_Age_2011(): 
    Data_2011 = pd.read_csv("../Raw_Data/Gender_Age_Data/DataFrames/Profession_Age_Gender_2011.csv")
    Gender_Age_2011_DF = pd.DataFrame(Data_2011)
    return Gender_Age_2011_DF


