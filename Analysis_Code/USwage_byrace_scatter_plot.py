
def USwage_byrace():
	#dependencies
	import pandas as pd 
	import matplotlib.pyplot as plt 
	#Read CSV
	DF = pd.read_csv('../Clean_Data/Race_Age_Data/Race_DataFrame.csv')
	DF = DF.set_index('Characteristic')
	
    #Create a list of the years that we will use as our x axis
	years= ['2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017']

	W_earning = []
	A_earning= []
	BAA_earning=[]
	HL_earning=[]
	W_workers = []
	A_workers= []
	BAA_workers=[]
	HL_workers=[]

	for year in years:

    	 W_earning.append(DF.loc["White",'{}_median_weekly_earnings'.format(year)])
    	 A_earning.append(DF.loc["Asian",'{}_median_weekly_earnings'.format(year)])
    	 BAA_earning.append(DF.loc["Black or African American",'{}_median_weekly_earnings'.format(year)])
    	 HL_earning.append(DF.loc["Hispanic or Latino ethnicity",'{}_median_weekly_earnings'.format(year)])
    	 
    	 W_workers.append(DF.loc["White",'{}_workers_in_000\'s'.format(year)])
    	 A_workers.append(DF.loc["Asian",'{}_workers_in_000\'s'.format(year)])
    	 BAA_workers.append(DF.loc["Black or African American",'{}_workers_in_000\'s'.format(year)])
    	 HL_workers.append(DF.loc["Hispanic or Latino ethnicity",'{}_workers_in_000\'s'.format(year)])

	df=pd.DataFrame({'Years':years,'White Earnings':W_earning,
		'Asian Earnings':A_earning,'Black or African American Earnings':BAA_earning,
		'Hispanic or Latino ethnicity Earnings':HL_earning,'White Workers':W_workers,
		'Asian Workers':A_workers,'Black or African American Workers':BAA_workers,'Hispanic or Latino ethnicity Workers':HL_workers})
                    

	years=['02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17']
	#test = df['White Workers']
  
	W_plot=plt.scatter(years, W_earning, alpha=1, c='coral', edgecolors='black', s = df["White Workers"]/ 200, label="White", linewidths=1)
	
	A_plot=plt.scatter(years, A_earning, alpha=1, c='skyblue', edgecolors='black', s = df['Asian Workers']/200, label="Asian", linewidths=1)

	BAA_plot=plt.scatter(years, BAA_earning, alpha=1, c='gold', edgecolors='black', s = df['Black or African American Workers']/200, label="Black or African American", linewidths=1)

	HL_plot=plt.scatter(years, HL_earning, alpha=1, c='green', edgecolors='black', s = df['Hispanic or Latino ethnicity Workers']/200, label="Hispanic or Latino ethnicity", linewidths=1)

	#ploting graph

	plt.ylabel('Median weekly earnings', fontsize = 12) 
	plt.xlabel('Years', fontsize = 12)
	plt.title("US wage time series by race", fontsize = 15)
	plt.grid()
	plt.legend(handles=[W_plot,A_plot,BAA_plot,HL_plot], loc="upper left", scatterpoints=1, fontsize=10, markerscale=0.5)
	note = ("Note:\n Circle size correlates with number of workers")
	plt.text(6,400,note)		
	plt.savefig("USwage_time_series_byrace.png")
	plt.show()	
USwage_byrace()






