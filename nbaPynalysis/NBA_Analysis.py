#Code for NBA Data Analysis

#!!!!!!!!!!!!!!!!!!!!!
#Needs to read in File:
    #1.NBA_Clean.csv
#Ouputs
    #1. NBA Salary Vs Age.Png 
    #2. NBA Yearly Salary Analysis

#!!!!!!!!!!!!!!!!!!!!!!!

#-----------------CODE STARTS HERE-----------------------
import os
import csv
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


file_one = "NBA_Clean.csv"
Compiled_df = pd.read_csv(file_one)


Compiled_df[Compiled_df==0]=np.nan            #In order for the zeros not to ruin my mean calculations, I will turn thing into 'nan' and use numppy to filter out

#utilizing the data frames that give me age and player names
#playerAge_df.head()
#playerAge_df.columns=['Player','Age'] 

#===================================================================================================
# The follow will show Weekly Income Aves per Year
#===================================================================================================

Compiled_df["2018"] = pd.to_numeric(Compiled_df["2018"])
Compiled_df["2017"] = pd.to_numeric(Compiled_df["2017"])
Compiled_df["2016"] = pd.to_numeric(Compiled_df["2016"])
Compiled_df["2015"] = pd.to_numeric(Compiled_df["2015"])
Compiled_df["2014"] = pd.to_numeric(Compiled_df["2014"])
Compiled_df["2013"] = pd.to_numeric(Compiled_df["2013"])
Compiled_df["2012"] = pd.to_numeric(Compiled_df["2012"])
Compiled_df["2011"] = pd.to_numeric(Compiled_df["2011"])
Compiled_df["2010"] = pd.to_numeric(Compiled_df["2010"])
Compiled_df["2009"] = pd.to_numeric(Compiled_df["2009"])
Compiled_df["2008"] = pd.to_numeric(Compiled_df["2008"])
Compiled_df["2007"] = pd.to_numeric(Compiled_df["2007"])
Compiled_df["2006"] = pd.to_numeric(Compiled_df["2006"])
Compiled_df["2005"] = pd.to_numeric(Compiled_df["2005"])
Compiled_df["2004"] = pd.to_numeric(Compiled_df["2004"])
Compiled_df["2003"] = pd.to_numeric(Compiled_df["2003"])
Compiled_df["2002"] = pd.to_numeric(Compiled_df["2002"])
Compiled_df["2001"] = pd.to_numeric(Compiled_df["2001"])

#===================================================================================================
# Taking means
#===================================================================================================


Ave_2018 = Compiled_df['2018'].mean()
Ave_2017 = Compiled_df['2017'].mean()
Ave_2016 = Compiled_df['2016'].mean()
Ave_2015 = Compiled_df['2015'].mean()
Ave_2014 = Compiled_df['2014'].mean()
Ave_2013 = Compiled_df['2013'].mean()
Ave_2012 = Compiled_df['2012'].mean()
Ave_2011 = Compiled_df['2011'].mean()
Ave_2010 = Compiled_df['2010'].mean()
Ave_2009 = Compiled_df['2009'].mean()
Ave_2008 = Compiled_df['2008'].mean()
Ave_2007 = Compiled_df['2007'].mean()
Ave_2006 = Compiled_df['2006'].mean()
Ave_2005 = Compiled_df['2005'].mean()
Ave_2004 = Compiled_df['2004'].mean()
Ave_2003 = Compiled_df['2003'].mean()
Ave_2002 = Compiled_df['2002'].mean()
Ave_2001 = Compiled_df['2001'].mean()

max_2001 = Compiled_df['2001'].max()
#max_2001
in_2001=Compiled_df['2001'].mean()
#in_2001

#===================================================================================================
# Charting Prework
#===================================================================================================



Year=[2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 
      2010, 2009, 2008, 2007, 2006, 2005, 2004, 2003, 2002, 2001]
       

Ave_income =[Ave_2018, Ave_2017,Ave_2016,Ave_2015,Ave_2014,Ave_2013,Ave_2012,Ave_2011,Ave_2010,Ave_2009,
             Ave_2008,Ave_2007,Ave_2006,Ave_2005,Ave_2004,Ave_2003, Ave_2002,Ave_2001]

#===================================================================================================
# This code give me Average income per week using a for statement
    #through my average yearly income df
#===================================================================================================
   
TotWeeks=52
Ave_W_Income=[]
for x in Ave_income:
    Ave_W_Income.append(x/TotWeeks)
Ave_income=Ave_W_Income

#===================================================================================================
#Plotting
#===================================================================================================

plt.plot(Year, Ave_income, color='blue', label="NBA Ave")
plt.title("NBA Avg. Weekly Income")
plt.xlabel("Seasonr")
plt.ylabel("Weekly Salary") 
#plt.figure(figsize=(10,6))
plt.legend(loc="center left", bbox_to_anchor=(1, 0.5))
plt.savefig("NBA Yearly Salary Analysis")
#plt.show()
#===================================================================================================
#Age vs income chart code follows
#===================================================================================================

Compiled_df["Age"] = pd.to_numeric(Compiled_df["Age"], errors='coerce').fillna(0).astype(np.int64) #Age came in as an object and i need it in a numerical format
#Compiled_df.head()

#===================================================================================================
#================The following was used to verifying that my df arithmetic was correct==============
#===================================================================================================

Age_Track_df = Compiled_df["Age"]
Aged_Track_df= pd.DataFrame(Age_Track_df)  
Aged_Track_df.columns=['2018']
Aged_Track_df.head()
Aged_Track_df['2017']=Aged_Track_df.apply(lambda x: x-1)
Aged_Track_df['2016']=Aged_Track_df['2017'].apply(lambda x: x-1)
Aged_Track_df['2015']=Aged_Track_df['2016'].apply(lambda x: x-1)
Aged_Track_df['2014']=Aged_Track_df['2015'].apply(lambda x: x-1)
Aged_Track_df['2013']=Aged_Track_df['2014'].apply(lambda x: x-1)
Aged_Track_df['2012']=Aged_Track_df['2013'].apply(lambda x: x-1)
Aged_Track_df['2011']=Aged_Track_df['2012'].apply(lambda x: x-1)
Aged_Track_df['2010']=Aged_Track_df['2011'].apply(lambda x: x-1)
Aged_Track_df['2009']=Aged_Track_df['2010'].apply(lambda x: x-1)
Aged_Track_df['2008']=Aged_Track_df['2009'].apply(lambda x: x-1)
Aged_Track_df['2007']=Aged_Track_df['2008'].apply(lambda x: x-1)
Aged_Track_df['2006']=Aged_Track_df['2007'].apply(lambda x: x-1)
Aged_Track_df['2005']=Aged_Track_df['2006'].apply(lambda x: x-1)
Aged_Track_df['2004']=Aged_Track_df['2005'].apply(lambda x: x-1)
Aged_Track_df['2003']=Aged_Track_df['2004'].apply(lambda x: x-1)
Aged_Track_df['2002']=Aged_Track_df['2003'].apply(lambda x: x-1)
Aged_Track_df['2001']=Aged_Track_df['2002'].apply(lambda x: x-1)
Aged_Track_df['2000']=Aged_Track_df['2001'].apply(lambda x: x-1)
#Aged_Track_df.head()

bins = [17, 24, 34 , 44, 55]                                                           # Create the bins in which Data will be held 
group_names = ['Ages 18-24', 'Ages 25-34', 'Ages 34-44', '45+ Years']                 # Create the names for the for bins  #

Compiled_df["Age Groups"] = pd.cut(Compiled_df["Age"], bins, labels=group_names)      #Cut chart into bens#
NCompiled_df=Compiled_df                                                              # I neeed t preseved my Compiled_df
NCompiled_df.drop('Player', axis=1, inplace=True)                                      #Drop unnecessary column
#NCompiled_df

#=====================================================================================================================
#returns only the lines i need and most importantly used a lambda function to calculate age of players that season===
#====================================================================================================================

AvI2018= NCompiled_df.iloc[:,[0,1]]

AvI2017= NCompiled_df.iloc[:,[0,2]]
AvI2017=AvI2017.apply(lambda x: x-1) #Calculaes age by subtracting from their 2018 age. Note: 2018 Matrix doesn't require modification
AvI2016= NCompiled_df.iloc[:,[0,3]]
AvI2016=AvI2016.apply(lambda x: x-2)
AvI2015= NCompiled_df.iloc[:,[0,4]]
AvI2015=AvI2015.apply(lambda x: x-3)
AvI2014= NCompiled_df.iloc[:,[0,5]]
AvI2014=AvI2014.apply(lambda x: x-4)
AvI2013=NCompiled_df.iloc[:,[0,6]]
AvI2013=AvI2013.apply(lambda x: x-5)
AvI2012= NCompiled_df.iloc[:,[0,7]]
AvI2012=AvI2012.apply(lambda x: x-6)
AvI2011= NCompiled_df.iloc[:,[0,8]]
AvI2011=AvI2011.apply(lambda x: x-7)
AvI2010= NCompiled_df.iloc[:,[0,9]]
AvI2010=AvI2010.apply(lambda x: x-8)
AvI2009= NCompiled_df.iloc[:,[0,10]]
AvI2009=AvI2009.apply(lambda x: x-9)
AvI2008= NCompiled_df.iloc[:,[0,11]]
AvI2008=AvI2018.apply(lambda x: x-10)
AvI2007= NCompiled_df.iloc[:,[0,12]]
AvI2007=AvI2007.apply(lambda x: x-11)
AvI2006= NCompiled_df.iloc[:,[0,13]]
AvI2006=AvI2006.apply(lambda x: x-12)
AvI2005= NCompiled_df.iloc[:,[0,14]]
AvI2005=AvI2005.apply(lambda x: x-13)
AvI2004= NCompiled_df.iloc[:,[0,15]]
AvI2004=AvI2004.apply(lambda x: x-14)
AvI2003= NCompiled_df.iloc[:,[0,16]]
AvI2003=AvI2003.apply(lambda x: x-15)
AvI2002= NCompiled_df.iloc[:,[0,17]]
AvI2002=AvI2002.apply(lambda x: x-16)

#AvI2017.head()

#===================================================================================================
#================Binning==========================================================================
#===================================================================================================

bins = [17, 24, 34 , 44, 55]                                            # Create the bins in which Data will be held 
group_names = ['Ages 18-24', 'Ages 25-34', 'Ages 35-44', '45+ Years']  # Create the names for the for bins  

AvI2018["Age Groups"] = pd.cut(AvI2018["Age"], bins, labels=group_names) #Cut chart into bens

AvI2017["Age Groups"] = pd.cut(AvI2017["Age"], bins, labels=group_names) #Cut chart into bens

AvI2016["Age Groups"] = pd.cut(AvI2016["Age"], bins, labels=group_names) #Cut chart into bens
AvI2015["Age Groups"] = pd.cut(AvI2015["Age"], bins, labels=group_names) #Cut chart into bens
AvI2014["Age Groups"] = pd.cut(AvI2014["Age"], bins, labels=group_names) #Cut chart into bens

AvI2013["Age Groups"] = pd.cut(AvI2013["Age"], bins, labels=group_names) #Cut chart into bens
AvI2012["Age Groups"] = pd.cut(AvI2012["Age"], bins, labels=group_names) #Cut chart into bens
AvI2011["Age Groups"] = pd.cut(AvI2011["Age"], bins, labels=group_names) #Cut chart into bens
AvI2010["Age Groups"] = pd.cut(AvI2010["Age"], bins, labels=group_names) #Cut chart into bens
AvI2009["Age Groups"] = pd.cut(AvI2009["Age"], bins, labels=group_names) #Cut chart into bens
AvI2008["Age Groups"] = pd.cut(AvI2008["Age"], bins, labels=group_names) #Cut chart into bens

#===================================================================================================
#The following seperates the take the mean of my data sets prior to me building a final large dataset
#===================================================================================================
Tw_18= AvI2018.groupby("Age Groups").mean()
Tw_18= Tw_18.reset_index()
Tw_17= AvI2017.groupby("Age Groups").mean()
Tw_17= Tw_17.reset_index()
Tw_16= AvI2016.groupby("Age Groups").mean()
Tw_16= Tw_16.reset_index()
Tw_15= AvI2015.groupby("Age Groups").mean()
Tw_15= Tw_15.reset_index()
Tw_14= AvI2014.groupby("Age Groups").mean()
Tw_14= Tw_14.reset_index()
Tw_13= AvI2013.groupby("Age Groups").mean()
Tw_13= Tw_13.reset_index()
Tw_12= AvI2012.groupby("Age Groups").mean()
Tw_12= Tw_12.reset_index()
Tw_11= AvI2011.groupby("Age Groups").mean()
Tw_11= Tw_11.reset_index()
Tw_10= AvI2010.groupby("Age Groups").mean()
Tw_10= Tw_10.reset_index()
Tw_09= AvI2009.groupby("Age Groups").mean()
Tw_09= Tw_09.reset_index()
Tw_08= AvI2008.groupby("Age Groups").mean()#["{0:,}".format]
Tw_08= Tw_08.reset_index()
#Tw_08

#===================================================================================================
# Building ave vs salary Chart df
#===================================================================================================

chart = Tw_18.merge(Tw_17, how='left', on="Age Groups")#, right_on='Player',suffixes=('_2018','_2017')).fillna(0)
chart = chart.merge(Tw_16, how='left', on="Age Groups")#, right_on='Player',suffixes=('_2018','_2017')).fillna(0)
chart = chart.merge(Tw_15, how='left', on="Age Groups")#, right_on='Player',suffixes=('_2018','_2017')).fillna(0)
chart = chart.merge(Tw_14, how='left', on="Age Groups")#, right_on='Player',suffixes=('_2018','_2017')).fillna(0)
chart = chart.merge(Tw_13, how='left', on="Age Groups")#, right_on='Player',suffixes=('_2018','_2017')).fillna(0)
chart = chart.merge(Tw_12, how='left', on="Age Groups")#, right_on='Player',suffixes=('_2018','_2017')).fillna(0)
chart = chart.merge(Tw_11, how='left', on="Age Groups")#, right_on='Player',suffixes=('_2018','_2017')).fillna(0)
chart = chart.merge(Tw_10, how='left', on="Age Groups")#, right_on='Player',suffixes=('_2018','_2017')).fillna(0)
chart = chart.merge(Tw_09, how='left', on="Age Groups")#, right_on='Player',suffixes=('_2018','_2017')).fillna(0)
chart = chart.merge(Tw_08, how='left', on="Age Groups")#, right_on='Player',suffixes=('_2018','_2017')).fillna(0)
chart=chart.rename(columns={'2018_x':'2018'})
chart=chart.iloc[:,[0,2,4,6,8,10,12,14,16,18,20]]

chart1=chart.transpose() # the chart format needed to be changed
chart1.columns = chart1.iloc[0]  #Copy what i want as my index value to index
chart1.reset_index()
chart1['Years']= chart1.index #I need to make a new index but save the value that the chart is currently indexed by
chart1.index = range(11)         #Setting Index
chart1=chart1.drop(chart1.index[0]) #Removing the line i used to make my index
chart1= chart1.sort_values(["Years"], ascending=True)

#The Following is a scatterplot for age vs Avg salary

a=plt.scatter(chart1["Years"], chart1["Ages 18-24"], c='gold', edgecolor="black")
b=plt.scatter(chart1["Years"], chart1["Ages 25-34"], c='lightcoral', edgecolor="black")
c=plt.scatter(chart1["Years"], chart1["Ages 35-44"], c='lightskyblue', edgecolor="black")


plt.title("Basketball Salarys vs Player Age over the last 10 Seasons")
plt.xlabel("Season")
plt.ylabel("Salary")
plt.text(1, .025, r'Orignal Df can only used current players')
#ax.set_ylim(0,10000000)                                                # I want to redefine limits

plt.legend((a, b, c), ('Ages 18-24', 'Ages 25-34', 'Ages 35-44'), scatterpoints=1,
            loc='center left',
            bbox_to_anchor=(1, 0.5),
            ncol=3,
            fontsize=8)


plt.grid(b=True, which = 'major', color ='gray', linestyle='-')
plt.savefig("NBA Salary Vs Age")
#plt.show()

print("NBA Anlaysis completed successfully! :D")

