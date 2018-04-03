def USwage_bygenderbyrace():

	#dependencies
	import pandas as pd 
	import matplotlib.pyplot as plt 

	#Read CSV
	DF = pd.read_csv('../Clean_Data/Race_Age_Data/Race_DataFrame.csv')
	DF = DF.set_index('Characteristic')

	#Create a list of the years that we will use as our x axis
	years= ['2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017']

	W_M = []
	A_M= []
	BAA_M=[]
	HL_M=[]
	W_W = []
	A_W= []
	BAA_W=[]
	HL_W=[]

	N_W_M = []
	N_A_M= []
	N_BAA_M=[]
	N_HL_M=[]
	N_W_W = []
	N_A_W= []
	N_BAA_W=[]
	N_HL_W=[]

	for year in years:

		 W_M.append(DF.loc['W, Men','{}_median_weekly_earnings'.format(year)])
		 W_W.append(DF.loc['W, Women','{}_median_weekly_earnings'.format(year)])
		 A_M.append(DF.loc['A, Men','{}_median_weekly_earnings'.format(year)])
		 A_W.append(DF.loc['A, Women','{}_median_weekly_earnings'.format(year)])
		 HL_M.append(DF.loc['H/L, Men','{}_median_weekly_earnings'.format(year)])
		 HL_W.append(DF.loc['H/L, Women','{}_median_weekly_earnings'.format(year)])
		 BAA_M.append(DF.loc['B/AA, Men','{}_median_weekly_earnings'.format(year)])
		 BAA_W.append(DF.loc['B/AA, Women','{}_median_weekly_earnings'.format(year)])

		 N_W_M.append(DF.loc['W, Men','{}_workers_in_000\'s'.format(year)])
		 N_W_W.append(DF.loc['W, Women','{}_workers_in_000\'s'.format(year)])
		 N_A_M.append(DF.loc['A, Men','{}_workers_in_000\'s'.format(year)])
		 N_A_W.append(DF.loc['A, Women','{}_workers_in_000\'s'.format(year)])
		 N_HL_M.append(DF.loc['H/L, Men','{}_workers_in_000\'s'.format(year)])
		 N_HL_W.append(DF.loc['H/L, Women','{}_workers_in_000\'s'.format(year)])
		 N_BAA_M.append(DF.loc['B/AA, Men','{}_workers_in_000\'s'.format(year)])
		 N_BAA_W.append(DF.loc['B/AA, Women','{}_workers_in_000\'s'.format(year)])

	df=pd.DataFrame({'Years':years,'White Men Workers':N_W_M,
		'White Women Workers':N_W_W,'Asian Men Workers':N_A_M,
		'Asian Women Workers':N_A_W,'Hispanic or Latino ethnicity Men Workers':N_HL_M,
		'Hispanic or Latino ethnicity Women Workers':N_HL_W,'Black or African American Men Workers':N_BAA_M,'Black or African American Women Workers':N_BAA_W})
  
	years = list(map(int, years))
	

	W_Mplot=plt.scatter(years, W_M, alpha=1, c='skyblue', edgecolors='black', marker='s',s = df["White Men Workers"]/ 200, label="White Men", linewidths=1)
	
	W_Wplot=plt.scatter(years, W_W, alpha=1, c='skyblue', edgecolors='black', marker='o',s = df['White Women Workers']/200, label="White Women", linewidths=1)

	A_Mplot=plt.scatter(years, A_M, alpha=1, c='red', edgecolors='black', marker='s',s = df['Asian Men Workers']/200, label="Asian Men", linewidths=1)

	A_Wplot=plt.scatter(years, A_W, alpha=1, c='red', edgecolors='black', marker='o',s = df['Asian Women Workers']/200, label="Asian Women", linewidths=1)
	
	HL_Mplot=plt.scatter(years, HL_M, alpha=1, c='yellow', edgecolors='black', marker='s',s = df["Hispanic or Latino ethnicity Men Workers"]/ 200, label="Hispanic or Latino Men", linewidths=1)
	
	HL_Wplot=plt.scatter(years, HL_W, alpha=1, c='yellow', edgecolors='black', marker='o',s = df['Hispanic or Latino ethnicity Women Workers']/200, label="Hispanic or Latino Women", linewidths=1)

	BAA_Mplot=plt.scatter(years, BAA_M, alpha=1, c='green', edgecolors='black', marker='s',s = df['Black or African American Men Workers']/200, label="Black or African American Men", linewidths=1)

	BAA_Wplot=plt.scatter(years, BAA_W, alpha=1, c='green', edgecolors='black',marker='o', s = df['Black or African American Women Workers']/200, label="Black or African American Women", linewidths=1)

	#ploting graph

	plt.ylabel('Median weekly earnings', fontsize = 12) 
	plt.xlabel('Years', fontsize = 12)
	plt.title("US wage time series by gender by race", fontsize = 15)
	plt.grid()
	plt.legend(handles=[W_Mplot,W_Wplot,A_Mplot,A_Wplot,BAA_Mplot,BAA_Wplot,HL_Mplot,HL_Wplot], loc="upper left", scatterpoints=1, fontsize=6, markerscale=0.5)
	note = ("Note:\n Marker size correlates with number of workers")
	plt.text(2008,400,note)		
	plt.savefig("USwage_time_series_bygenderbyrace.png")
	plt.show()	

USwage_bygenderbyrace()



