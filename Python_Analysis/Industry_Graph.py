#Declaring Dependacies
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from Gender_Age_DF import Gender_Age_2017
from Gender_Age_DF import Gender_Age_2016
from Gender_Age_DF import Gender_Age_2015
from Gender_Age_DF import Gender_Age_2014
from Gender_Age_DF import Gender_Age_2013
from Gender_Age_DF import Gender_Age_2012
from Gender_Age_DF import Gender_Age_2011

#Creating Global Variables to pull DataFrame into Notebook
Gender_Age_2017_DF = Gender_Age_2017()
Gender_Age_2016_DF = Gender_Age_2016()
Gender_Age_2015_DF = Gender_Age_2015()
Gender_Age_2014_DF = Gender_Age_2014()
Gender_Age_2013_DF = Gender_Age_2013()
Gender_Age_2012_DF = Gender_Age_2012()
Gender_Age_2011_DF = Gender_Age_2011()

#Gender_Age_2017_DF
Comp2017 = Gender_Age_2017_DF.loc[(Gender_Age_2017_DF["Industry_x"]=="Computer and Math")]
Eng2017 = Gender_Age_2017_DF.loc[(Gender_Age_2017_DF["Industry_x"]=="Engineering")]
Ent2017 = Gender_Age_2017_DF.loc[(Gender_Age_2017_DF["Industry_x"]=="Entertainmnet")]
HC2017 = Gender_Age_2017_DF.loc[(Gender_Age_2017_DF["Industry_x"]=="Healthcare")]
Serv2017 = Gender_Age_2017_DF.loc[(Gender_Age_2017_DF["Industry_x"]=="Service")]

#Gender_Age_2016_DF
Comp2016 = Gender_Age_2016_DF.loc[(Gender_Age_2016_DF["Industry_x"]=="Computer and Math")]
Eng2016= Gender_Age_2016_DF.loc[(Gender_Age_2016_DF["Industry_x"]=="Engineering")]
Ent2016 = Gender_Age_2016_DF.loc[(Gender_Age_2016_DF["Industry_x"]=="Entertainmnet")]
HC2016 = Gender_Age_2016_DF.loc[(Gender_Age_2016_DF["Industry_x"]=="Healthcare")]
Serv2016 = Gender_Age_2016_DF.loc[(Gender_Age_2016_DF["Industry_x"]=="Service")]

#Gender_Age_2015_DF
Comp2015 = Gender_Age_2015_DF.loc[(Gender_Age_2015_DF["Industry_x"]=="Computer and Math")]
Eng2015 = Gender_Age_2015_DF.loc[(Gender_Age_2015_DF["Industry_x"]=="Engineering")]
Ent2015 = Gender_Age_2015_DF.loc[(Gender_Age_2015_DF["Industry_x"]=="Entertainmnet")]
HC2015 = Gender_Age_2015_DF.loc[(Gender_Age_2015_DF["Industry_x"]=="Healthcare")]
Serv2015 = Gender_Age_2015_DF.loc[(Gender_Age_2015_DF["Industry_x"]=="Service")]

#Gender_Age_2014_DF
Comp2014 = Gender_Age_2014_DF.loc[(Gender_Age_2014_DF["Industry_x"]=="Computer and Math")]
Eng2014 = Gender_Age_2014_DF.loc[(Gender_Age_2014_DF["Industry_x"]=="Engineering")]
Ent2014 = Gender_Age_2014_DF.loc[(Gender_Age_2014_DF["Industry_x"]=="Entertainmnet")]
HC2014 = Gender_Age_2014_DF.loc[(Gender_Age_2014_DF["Industry_x"]=="Healthcare")]
Serv2014 = Gender_Age_2014_DF.loc[(Gender_Age_2014_DF["Industry_x"]=="Service")]

#Gender_Age_2013_DF
Comp2013 = Gender_Age_2013_DF.loc[(Gender_Age_2013_DF["Industry_x"]=="Computer and Math")]
Eng2013 = Gender_Age_2013_DF.loc[(Gender_Age_2013_DF["Industry_x"]=="Engineering")]
Ent2013 = Gender_Age_2013_DF.loc[(Gender_Age_2013_DF["Industry_x"]=="Entertainmnet")]
HC2013 = Gender_Age_2013_DF.loc[(Gender_Age_2013_DF["Industry_x"]=="Healthcare")]
Serv2013 = Gender_Age_2013_DF.loc[(Gender_Age_2013_DF["Industry_x"]=="Service")]

#Gender_Age_2012_DF
Comp2012 = Gender_Age_2012_DF.loc[(Gender_Age_2012_DF["Industry_x"]=="Computer and Math")]
Eng2012 = Gender_Age_2012_DF.loc[(Gender_Age_2012_DF["Industry_x"]=="Engineering")]
Ent2012 = Gender_Age_2012_DF.loc[(Gender_Age_2012_DF["Industry_x"]=="Entertainmnet")]
HC2012 = Gender_Age_2012_DF.loc[(Gender_Age_2012_DF["Industry_x"]=="Healthcare")]
Serv2012 = Gender_Age_2012_DF.loc[(Gender_Age_2012_DF["Industry_x"]=="Service")]

#Gender_Age_2011_DF
Comp2011 = Gender_Age_2011_DF.loc[(Gender_Age_2011_DF["Industry_x"]=="Computer and Math")]
Eng2011 = Gender_Age_2011_DF.loc[(Gender_Age_2011_DF["Industry_x"]=="Engineering")]
Ent2011 = Gender_Age_2011_DF.loc[(Gender_Age_2011_DF["Industry_x"]=="Entertainmnet")]
HC2011 = Gender_Age_2011_DF.loc[(Gender_Age_2011_DF["Industry_x"]=="Healthcare")]
Serv2011 = Gender_Age_2011_DF.loc[(Gender_Age_2011_DF["Industry_x"]=="Service")]


#Line Graph for Total # of Workers by Industry per Year
#Storing total employee values

Total_Emp = []

#HealtheCare Total
HCTotal2017 = HC2017['Total Number of workers'].sum()
HCTotal2016 = HC2016['Total Number of workers'].sum()
HCTotal2015 = HC2015['Total Number of workers'].sum()
HCTotal2014 = HC2014['Total Number of workers'].sum()
HCTotal2013 = HC2013['Total Number of workers'].sum()
HCTotal2012 = HC2012['Total Number of workers'].sum()
HCTotal2011 = HC2011['Total Number of workers'].sum()

#Entertainment Total
EntTotal2017 = Ent2017['Total Number of workers'].sum()
EntTotal2016 = Ent2016['Total Number of workers'].sum()
EntTotal2015 = Ent2015['Total Number of workers'].sum()
EntTotal2014 = Ent2014['Total Number of workers'].sum()
EntTotal2013 = Ent2013['Total Number of workers'].sum()
EntTotal2012 = Ent2012['Total Number of workers'].sum()
EntTotal2011 = Ent2011['Total Number of workers'].sum()

#Service Total
ServTotal2017 = Serv2017['Total Number of workers'].sum()
ServTotal2016 = Serv2016['Total Number of workers'].sum()
ServTotal2015 = Serv2015['Total Number of workers'].sum()
ServTotal2014 = Serv2014['Total Number of workers'].sum()
ServTotal2013 = Serv2013['Total Number of workers'].sum()
ServTotal2012 = Serv2012['Total Number of workers'].sum()
ServTotal2011 = Serv2011['Total Number of workers'].sum()

#Computer & Math Total
Comptotal2017 = Comp2017['Total Number of workers'].sum()
Comptotal2016 = Comp2016['Total Number of workers'].sum()
Comptotal2015 = Comp2015['Total Number of workers'].sum()
Comptotal2014 = Comp2014['Total Number of workers'].sum()
Comptotal2013 = Comp2013['Total Number of workers'].sum()
Comptotal2012 = Comp2012['Total Number of workers'].sum()
Comptotal2011 = Comp2011['Total Number of workers'].sum()

#Engineering Total
Engtotal2017 = Eng2017['Total Number of workers'].sum()
Engtotal2016 = Eng2016['Total Number of workers'].sum()
Engtotal2015 = Eng2015['Total Number of workers'].sum()
Engtotal2014 = Eng2014['Total Number of workers'].sum()
Engtotal2013 = Eng2013['Total Number of workers'].sum()
Engtotal2012 = Eng2012['Total Number of workers'].sum()
Engtotal2011 = Eng2011['Total Number of workers'].sum()

year = [2011, 2012, 2013, 2014, 2015, 2016, 2017]
HC= [HCTotal2011, HCTotal2012, HCTotal2013, HCTotal2014, HCTotal2015, HCTotal2016, HCTotal2017]
Comp= [Comptotal2011, Comptotal2012, Comptotal2013, Comptotal2014, Comptotal2015, Comptotal2016, Comptotal2017]
Eng= [Engtotal2011, Engtotal2012, Engtotal2013, Engtotal2014, Engtotal2015, Engtotal2016, Engtotal2017]
Serv= [ServTotal2011, ServTotal2012, ServTotal2013, ServTotal2014, ServTotal2015, ServTotal2016, ServTotal2017]
Ent= [EntTotal2011, EntTotal2012, EntTotal2013, EntTotal2014, EntTotal2015, EntTotal2016, EntTotal2017]

#assinging values to line graph
plt.plot(year, HC, color='blue', label="Healthcare")
plt.plot(year, Comp, color='red', label="Computer & Math")
plt.plot(year, Eng, color='green', label="Engineering")
plt.plot(year, Serv, color='yellow', label="Service")
plt.plot(year, Ent, color='purple', label="Entertainment")

plt.title("Total Employees per Industry by Year")
plt.xlabel("Year")
plt.ylabel("Toal Employees") 
plt.legend(loc="center left", bbox_to_anchor=(1, 0.5))
plt.savefig("Industry Analysis")
