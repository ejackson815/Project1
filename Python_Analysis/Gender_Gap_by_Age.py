import requests
import json
import pandas as pd
import matplotlib.pyplot as plt

years = [2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015]

#reading in csv files for different age buckets

twent_thirt = pd.read_csv('25-34.csv')
thirt_forty = pd.read_csv('35-44.csv')
forty_fifty = pd.read_csv('45-54.csv') 
fifty_sixty = pd.read_csv('55-64.csv') 
sixty_over = pd.read_csv('65&Over.csv')

#dividing the wages for women by the wages for men to get\
#women wages as a % of men's wages

twenty = twent_thirt['women']/twent_thirt['men']
thirty = thirt_forty['women']/thirt_forty['men']
forty = forty_fifty['women']/forty_fifty['men']
fifty = fifty_sixty['women']/fifty_sixty['men']
sixty = sixty_over['women']/sixty_over['men']


#plot wage gaps over the years
twenty_gap = plt.plot(years, twenty,color ='blue', label = '25-34')
thirty_gap = plt.plot(years, thirty, color ='green',label = '35-44' )
forty_gap = plt.plot(years, forty, color ='red',label = '45-54')
fifty_gap = plt.plot(years, fifty, color ='purple',label = '55-64')
sixty_gap = plt.plot(years, sixty, color ='orange',label = '65 and over')

plt.legend(loc=2)


plt.title('US Female Wages as a % of US Male Wages')
plt.ylabel("F Wages as % of M Wages")

plt.savefig('Gender_Gap_by_Age.png')
plt.show()