import pandas as pd 
import matplotlib.pyplot as plt 

DF = pd.read_csv('../Clean_Data/Race_Age_Data/Race_DataFrame.csv')
DF = DF.set_index('Characteristic')


years= ['2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017']

asianm = []
asianw= []

latinom = []
latinow= []

for year in years:
    
    asianm.append(DF.loc['A, Men','{}_median_weekly_earnings'.format(year)])
    asianw.append(DF.loc['A, Women','{}_median_weekly_earnings'.format(year)])

    latinom.append(DF.loc['H/L, Men','{}_median_weekly_earnings'.format(year)])
    latinow.append(DF.loc['H/L, Women','{}_median_weekly_earnings'.format(year)])

    

    
years = list(map(int, years))
plt.title('Wages - Asian Men / Women')
diffa= pd.Series(asianm) - pd.Series(asianw)

plt.scatter(years, diffa, color = 'pink')
plt.scatter(years, asianm)
plt.scatter(years, asianw)
plt.show()

plt.title('Wages - Latino Men / Women')
diffl= pd.Series(asianm) - pd.Series(asianw)

plt.scatter(years, diffl, color = 'pink')
plt.scatter(years, latinom)
plt.scatter(years, latinow)
plt.show()