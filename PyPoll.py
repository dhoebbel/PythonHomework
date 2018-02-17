#import modules
import pandas as pd
import numpy as np

#save file path as variable
election1 = "Resources/election_data_1.csv"
election2 = "Resources/election_data_2.csv"

#read in first file
election1_df = pd.read_csv(election1)
election1_df.head()

#read in second file
election2_df = pd.read_csv(election2)
election2_df.head()

#stack csv files together to create new DataFrame
allData = pd.concat([election1_df, election2_df])
allData.head()

#Calculate total votes placed
totalVotes = allData["Voter ID"].count()
totalVotes

#Calculate the number of candidates
totalCandidates = allData["Candidate"].nunique()
totalCandidates

#List of candidates
listCandidates = []
listCandidates = allData["Candidate"].unique()
listCandidates

#assigns a true or false condition to each vote for each candidate
vestal = allData["Candidate"] == "Vestal"
torres = allData["Candidate"] == "Torres"
seth = allData["Candidate"] == "Seth"
cordin = allData["Candidate"] == "Cordin"
khan = allData["Candidate"] == "Khan"
correy = allData["Candidate"] == "Correy"
li = allData["Candidate"] == "Li"
tooley = allData["Candidate"] == "O'Tooley"


#turns true/false into 1 or 0
allData["Vestal"]=vestal.astype(int)
allData["Torres"]=torres.astype(int)
allData["Seth"]=seth.astype(int)
allData["Cordin"]=cordin.astype(int)
allData["Khan"]=khan.astype(int)
allData["Correy"]=correy.astype(int)
allData["Li"]=li.astype(int)
allData["O'Tooley"]=tooley.astype(int)
allData.head()

#count yes votes
vestalVotes = allData['Vestal'].sum()
torresVotes = allData['Torres'].sum()
sethVotes = allData['Seth'].sum()
cordinVotes = allData['Cordin'].sum()
khanVotes = allData['Khan'].sum()
correyVotes = allData['Correy'].sum()
liVotes = allData['Li'].sum()
tooleyVotes = allData["O'Tooley"].sum()

#each candidates votes and percentage
totalVotes
vestalPercent = vestalVotes / totalVotes
torresPercent = torresVotes / totalVotes
sethPercent = sethVotes / totalVotes
cordinPercent = cordinVotes / totalVotes
khanPercent = khanVotes / totalVotes
correyPercent = correyVotes / totalVotes
liPercent = liVotes / totalVotes
tooleyPercent = tooleyVotes / totalVotes

#output
print("Election Results")
print("----------------------------------------")
print("Total Votes: " + str(totalVotes))
print("Vestal:  "+"{:.2%}".format(vestalPercent), "(", vestalVotes,")")
print("Torres: "+"{:.2%}".format(torresPercent), "(", torresVotes,")")
print("Seth: "+"{:.2%}".format(sethPercent), "(", sethVotes,")")
print("Cordin: "+"{:.2%}".format(cordinPercent), "(", cordinVotes,")")
print("Khan: "+"{:.2%}".format(khanPercent), "(", khanVotes,")")
print("Correy: "+"{:.2%}".format(correyPercent), "(", correyVotes,")")
print("Li: "+"{:.2%}".format(liPercent), "(", liVotes,")")
print("O'Tooley: "+"{:.2%}".format(tooleyPercent), "(", tooleyVotes,")")
print("----------------------------------------")
print("Winner: Khan")
print("----------------------------------------")
