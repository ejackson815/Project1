# This is the code for cleaning the NBA data
#Requires:
  # 1. nba_salaries_1990_to_2018.csv
  # 2. Age_player.csv
# Outputs cleaned data to file
  # 1. "NBA_clean.csv"

import os
import csv
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#====================================================================================================
#=======================Building Dataset for yearly salaries with Player name as Key=================
#====================================================================================================
historic_bball = os.path.join("nba_salaries_1990_to_2018.csv")

# Set empty list variables
Player= []
Salary = []
Season = []

  #Open current NBA CSV to zip important Values into a df
with open(historic_bball, 'r') as csvFile:                    

   csvReader = csv.reader(csvFile, delimiter=',')

   # Skipp headers
   next(csvReader, None)                                      

   for row in csvReader:

       # Append data from the row
       Player.append(row[0])
       Salary.append(row[1])
       Season.append(row[2])
    
# Zip lists together
cleanCSV = list(zip(Player, Salary, Season))
#cleanCSV                        #Returns raw data for processing into dataframe             


df = pd.DataFrame(cleanCSV)              # Creating dataframe for
df.columns=['Player','Salary','Season']  #changing column name
df.head()
#df.count

#====================================================================================================
#==================Building Dataset for Current Players Ages with Player name as Key=================
#====================================================================================================

bball_age = os.path.join("Age_player.csv")

# Set empty list variables
Player= []
Age2018 = []

# Open current NBA CSV to zip important Values into a df
with open(bball_age, 'r') as csvFile:
   csvReader = csv.reader(csvFile, delimiter=',')

   # Skipp headers
   next(csvReader, None)

   for row in csvReader:

       # Append data from the row
       Player.append(row[0])
       Age2018.append(row[1])

       
# Zip lists together
AgeCSV = list(zip(Player, Age2018))
#AgeCSV

playerAge_df = pd.DataFrame(AgeCSV)
playerAge_df.columns=['Player','Age']  #changing column name
#playerAge_df.describe
playerAge_df.head()                    #Returns AGE vs Player name DF      

drop_df= df.drop_duplicates(['Player', 'Season'])    # Needed to drop players with duplicate salaries forthe same season
df=drop_df



#====================================================================================================
#====================Pivot Table used to view dataset================================================
#=====================Not Needed, but I wanted to look at the dataset================================
#====================================================================================================

pivot_df=df.pivot(index="Player", columns="Season", values="Salary")

#NOT NEEDED, BUT WANTED
#=====================================================================================================
unique = df["Season"].unique()                         # Just showing the number years in my raw data
unique
#=====================================================================================================                   
Dwight= df.loc[df["Player"] == "Dwight Howard"]         # I want to check the salary of a player over all the years to verify that my merged dataframes are putting data in the correct location
Jarrett= df.loc[df["Player"] == "Jarrett Jack"]         # I want to check the salary of a player over all the years to verify that my merged dataframes are putting data in the correct location


#===========================================================================================================
#============================The Next few cells created the dataframes for the yearly salaries==============
#===========================================================================================================

df2018= df.loc[df["Season"] == "2018"]
df2018= df2018.iloc[:,[0,1]]
df2017= df.loc[df["Season"] == "2017"]
df2017= df2017.iloc[:,[0,1]]
df2016= df.loc[df["Season"] == "2016"]
df2016= df2016.iloc[:,[0,1]]
df2015= df.loc[df["Season"] == "2015"]
df2015= df2015.iloc[:,[0,1]]
#===========================2014===========================================
#===========================================================================
df2014= df.loc[df["Season"] == "2014"]
df2014= df2014.iloc[:,[0,1]]
#df2014.head()
#===========================2013===========================================
#===========================================================================
df2013= df.loc[df["Season"] == "2013"]
df2013= df2013.iloc[:,[0,1]]
#df2013.head()
#===========================2012===========================================
#===========================================================================
df2012= df.loc[df["Season"] == "2012"]
df2012= df2012.iloc[:,[0,1]]
#df2012.head()
#===========================2011===========================================
#===========================================================================
df2011= df.loc[df["Season"] == "2011"]
df2011= df2011.iloc[:,[0,1]]
#df2011.head()
#===========================2010===========================================
#===========================================================================
df2010= df.loc[df["Season"] == "2010"]
df2010= df2010.iloc[:,[0,1]]
#df2010.head()
#===========================2009===========================================
#===========================================================================
df2009= df.loc[df["Season"] == "2009"]
df2009= df2009.iloc[:,[0,1]]
#df2009.head()
#===========================2008===========================================
#===========================================================================
df2008= df.loc[df["Season"] == "2008"]
df2008= df2008.iloc[:,[0,1]]
#df2008.head()
#===========================2007===========================================
#===========================================================================
df2007= df.loc[df["Season"] == "2007"]
df2007= df2007.iloc[:,[0,1]]
#df2007.head()
#===========================2006===========================================
#===========================================================================
df2006= df.loc[df["Season"] == "2006"]
df2006= df2006.iloc[:,[0,1]]
#df2006.head()
#===========================2005===========================================#
#===========================================================================
df2005= df.loc[df["Season"] == "2005"]
df2005= df2005.iloc[:,[0,1]]
#df2005.head()
#===========================2004===========================================
#===========================================================================
df2004= df.loc[df["Season"] == "2004"]
df2004= df2004.iloc[:,[0,1]]
#df2004.head()
#===========================2003===========================================
#===========================================================================
df2003= df.loc[df["Season"] == "2003"]
df2003= df2003.iloc[:,[0,1]]
#df2003.head()
#===========================2002===========================================
#===========================================================================
df2002= df.loc[df["Season"] == "2002"]
df2002= df2002.iloc[:,[0,1]]
#df2002.head()
#===========================2001===========================================
#===========================================================================
df2001= df.loc[df["Season"] == "2001"]
df2001= df2001.iloc[:,[0,1]]
#df2001.head()
#===========================2000===========================================
#===========================================================================
df2000= df.loc[df["Season"] == "2000"]
df2000= df2000.iloc[:,[0,1]]
#df2000.head()




#=============================MERGING OF THE DATASETS JUST CREATED FOR SALARY VS YEARS===============
#====================================================================================================

Compiled_df = df2018.merge(df2017, how='left', left_on="Player", right_on='Player',suffixes=('_2018','_2017')).fillna(0)   #Left Merge Command. Left merges does not delete data
Compiled_df = Compiled_df.merge(df2016, how='left', left_on="Player", right_on='Player',suffixes=('','_2016')).fillna(0)   #Left Merge Command. Left merges does not delete data
Compiled_df = Compiled_df.merge(df2015, how='left', left_on="Player", right_on='Player',suffixes=('','_2015')).fillna(0)
Compiled_df = Compiled_df.merge(df2014, how='left', left_on="Player", right_on='Player',suffixes=('','_2014')).fillna(0)
Compiled_df = Compiled_df.merge(df2013, how='left', left_on="Player", right_on='Player',suffixes=('','_2013')).fillna(0)
Compiled_df = Compiled_df.merge(df2012, how='left', left_on="Player", right_on='Player',suffixes=('','_2012')).fillna(0)
Compiled_df = Compiled_df.merge(df2011, how='left', left_on="Player", right_on='Player',suffixes=('','_2011')).fillna(0)
Compiled_df = Compiled_df.merge(df2010, how='left', left_on="Player", right_on='Player',suffixes=('','_2010')).fillna(0)
Compiled_df = Compiled_df.merge(df2009, how='left', left_on="Player", right_on='Player',suffixes=('','_2009')).fillna(0)
Compiled_df = Compiled_df.merge(df2008, how='left', left_on="Player", right_on='Player',suffixes=('','_2008')).fillna(0)
Compiled_df = Compiled_df.merge(df2007, how='left', left_on="Player", right_on='Player',suffixes=('','_2007')).fillna(0)
Compiled_df = Compiled_df.merge(df2006, how='left', left_on="Player", right_on='Player',suffixes=('','_2006')).fillna(0)
Compiled_df = Compiled_df.merge(df2005, how='left', left_on="Player", right_on='Player',suffixes=('','_2005')).fillna(0)
Compiled_df = Compiled_df.merge(df2004, how='left', left_on="Player", right_on='Player',suffixes=('','_2004')).fillna(0)
Compiled_df = Compiled_df.merge(df2003, how='left', left_on="Player", right_on='Player',suffixes=('','_2003')).fillna(0)
Compiled_df = Compiled_df.merge(df2002, how='left', left_on="Player", right_on='Player',suffixes=('','_2002')).fillna(0)
Compiled_df = Compiled_df.merge(df2001, how='left', left_on="Player", right_on='Player',suffixes=('','_2001')).fillna(0)
Compiled_df = Compiled_df.merge(df2000, how='left', left_on="Player", right_on='Player',suffixes=('','_2000')).fillna(0)


new_col=['Player','2018', '2017', '2016', '2015', '2014', '2013', '2012',
        '2011', '2010', '2009', '2008', '2007', '2006', '2005', 
        '2004', '2003', '2002', '2001', '2000']
                                 
Compiled_df.columns = new_col
#Compiled_df


#====================================================================================================
#==================Creating final Dataframe with a Merge Function====================================
#=====Function conveniently deletes rows with index values that are not shared by both dataframes====
#====================================================================================================


Compiled_df = pd.merge(playerAge_df, Compiled_df, on="Player")
drop2_df= Compiled_df.drop_duplicates(['Player', 'Age']) # Needed to drop players with duplicate salaries forthe same season
Compiled_df=drop2_df                                      #Moving final dataframe into global function

# Push the remade DataFrame to a new CSV file
Compiled_df.to_csv("NBA_clean.csv", encoding="utf-8", index=False, header=True)

print("NBA Data Cleaning ran successfully")
#END===============:)