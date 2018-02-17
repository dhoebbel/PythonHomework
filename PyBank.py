#import modules
import pandas as pd
import numpy as np

#save file path as variable
budget1 = "budget_data_1.csv"
budget2 = "budget_data_2.csv"

#read in first file
budget1_df = pd.read_csv(budget1)
budget1_df.head()

#read in second file
budget2_df = pd.read_csv(budget2)
budget2_df.head()

#stack csv files together to create new DataFrame
allData = pd.concat([budget1_df, budget2_df])
allData.head()

#Count total months and sum revenue
TotalMonths = allData["Date"].count()
TotalRevenue = allData["Revenue"].sum()

#Calculate monthly change in revenue
returns = allData["Revenue"] - allData["Revenue"].shift(1)
returns.head()

#Add in monthly change column
allData["Monthly Change"] = returns
allData.head()

#calculate average revenue change, greatest change and greatest decline
avgChange = allData["Monthly Change"].mean()
maxChange = allData["Monthly Change"].max()
minChange = allData["Monthly Change"].min()

#final output
print ("    Financial Analysis")
print ("----------------------------")
print("Total Months: " + str(TotalMonths))
print("Total Revenue: " + str(TotalRevenue))
print("Average Revenue Change: " + str(avgChange))
print("Greatest Increase in Revenue: " + str(maxChange))
print("Greatest Decrease in Revenue: " + str(minChange))

#trying to consolidate the months/dates so that I can accurately calculate the monthly changes, etc.
#allData.set_index("Date", inplace=True)
#allData["Date"] = pd.to_datetime(allData["Date"])
#allData["Date"].groupby(pd.TimeGrouper(freq='M'))
#allData.head()



