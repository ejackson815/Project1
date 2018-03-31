def race_plotting(race):

	#dependencies
	import pandas as pd 
	import matplotlib.pyplot as plt 

	#Read CSV
	DF = pd.read_csv('../Clean_Data/Race_Age_Data/Race_DataFrame.csv')
	DF = DF.set_index('Characteristic')

    #Create a list of the years that we will use as our x axis
	years= ['2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017']

	race_M = []
	race_W= []


	for year in years:

    	 race_M.append(DF.loc['{}, Men'.format(race),'{}_median_weekly_earnings'.format(year)])
    	 race_W.append(DF.loc['{}, Women'.format(race),'{}_median_weekly_earnings'.format(year)])
    
	years = list(map(int, years))
    
	if (race=="A"):
		Race="Asian"
	elif(race=="W"):
		Race="White"
	elif(race=="H/L"):
		Race="Hispanic or Latino ethnicity"
	else:
		Race="Black or African American"

	raceM=plt.scatter(years, race_M,label="{},Men".format(Race))
	raceW=plt.scatter(years, race_W,label="{},Women".format(Race))

	
	plt.title(Race + "'s median weekly earnings from 2002 to 2017")
	plt.xlabel("Years")
	plt.ylabel("median weekly earnings")
	# Create a legend for our chart
	plt.legend(handles=[raceW, raceM], loc="best")
	# Save an image of the chart and print to screen
	plt.savefig("{}'s median weekly earnings.png.".format(Race))
	plt.show()
	plt.close

#call race_plotting function to plot 
race_plotting("A")
race_plotting("B/AA")
race_plotting("W")
race_plotting("H/L")

