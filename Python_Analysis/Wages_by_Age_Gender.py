import requests
import json
import pandas as pd
import matplotlib.pyplot as plt

years = [2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015]

#reading in csv's for different age buckets
twent_thirt = pd.read_csv('25-34.csv')
thirt_forty = pd.read_csv('35-44.csv')
forty_fifty = pd.read_csv('45-54.csv') 
fifty_sixty = pd.read_csv('55-64.csv') 
sixty_over = pd.read_csv('65&Over.csv')



#on same graph plot men's and women's wages for each age bucket
plt.title('US Wages by Age Group')
plt.ylabel("Median Weekly Earnings ($)")

twentyM = plt.scatter(years, twent_thirt['men'], color ='blue', marker = 's')
thirtyM = plt.scatter(years, thirt_forty['men'], color ='green', marker = 's')
fortyM = plt.scatter(years, forty_fifty['men'], color ='red', marker = 's')
fiftyM = plt.scatter(years, fifty_sixty['men'], color ='purple', marker = 's')
sixtyM = plt.scatter(years, sixty_over['men'], color ='orange', marker = 's')

twentyW = plt.scatter(years, twent_thirt['women'],color ='blue', edgecolors='black')
thirtyW = plt.scatter(years, thirt_forty['women'], color ='green', edgecolors='black')
fortyW = plt.scatter(years, forty_fifty['women'], color ='red', edgecolors='black')
fiftyW = plt.scatter(years, fifty_sixty['women'], color ='purple', edgecolors='black')
sixtyW = plt.scatter(years, sixty_over['women'], color ='orange',edgecolors='black')

first_legend = plt.legend((twentyM, thirtyM, fortyM, fiftyM, sixtyM),('25-34, Men','35-44, Men','45-54, Men', '55-64, Men', '65 and over, Men'))
ax = plt.gca().add_artist(first_legend)
plt.legend((twentyW, thirtyW, fortyW, fiftyW, sixtyW),('25-34, Women','35-44, Women','45-54, Women', '55-64, Women', '65 and over, Women'), loc =4)

plt.savefig('Wages_by_Age_Gender.png')
plt.show()