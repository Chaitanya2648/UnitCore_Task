# importing pandas libraries 
import pandas as pd

# to peform use of series
ser = pd.Series(["Chaitanya", "Shub", "Ketan","Chaitanya_K"])
print(ser)

# to perform use of dataframe
df = pd.DataFrame({
   "name": ["Mitchell Starc", "Steve Smith", "Ricky Pointing", "Shaun Tait"],
   "role" : ["Bolwer", "Batsman", "Batsman", "Bolwer"]
})
print(df)

# to perform row and column section
print(df.iloc[2, 0])
print(df.loc[0, "name"])

# to read a csv file
df = pd.read_csv("customers-100.csv")
print(df.head())

# to perform head,tail and info keywords
print(df.head(1)) # to print first n rows in table
print(df.tail(1)) # to print last n rows in table 
print(df.info()) # to print the summary of the table

# using filtering and sort of list and dictionaries
df = pd.DataFrame({
   "name": ["Chaitu","ketan", "Shub", "Kudalkar", "Siddhant"],
   "marks": [90, 89, 70, 88, 86]
})
print(df)
print(df[df["marks"] > 80]) # to filter rows condition
print(df.sort_values("marks")) # to sort the data from data frame

