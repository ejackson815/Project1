import pandas as pd
import matplotlib.pyplot as plt

years = [2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015]

#Read in the datasets for each bucket of ages
twent_thirt = pd.read_csv('25-34.csv')
thirt_forty = pd.read_csv('35-44.csv')
forty_fifty = pd.read_csv('45-54.csv') 
fifty_sixty = pd.read_csv('55-64.csv') 
sixty_over = pd.read_csv('65&Over.csv')



#Make scatter plot with year on the x-axis and median weekly earnings on the y-axis

plt.title('US Wages by Age Group')
plt.ylabel("Median Weekly Earnings ($)")


#Make a different scatter plot for each age bucket and put all scatters on one graph
twenty = plt.scatter(years, twent_thirt['general'])
thirty = plt.scatter(years, thirt_forty['general'])
forty = plt.scatter(years, forty_fifty['general'])
fifty = plt.scatter(years, fifty_sixty['general'])
sixty = plt.scatter(years, sixty_over['general'])
plt.legend((twenty, thirty, forty, fifty, sixty),('25-34','35-44','45-54', '55-64', '65 and over'))


plt.savefig('Wages_by_Age.png')
plt.show()