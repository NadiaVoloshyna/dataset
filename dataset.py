"""
Program: dataset.py
Author: Nadiia Voloshyna
1. Inputs
   set of data
2. Computations
   frequency for non-numeric values
   mean for numeric values 
3. Outputs
   the resultant data in a tabular format
"""

import pandas as pd

heroes = pd.read_csv("C:\ABERTAY\Voloshyna_Week5-assignment\SuperHeroes.csv", sep=';')
df = heroes.copy()
dfLength = len(heroes)

# Group by the column
grouped = df.groupby(df.Alignment)
df_bad = grouped.get_group("bad")
df_good = grouped.get_group("good")
df_neutral = grouped.get_group("neutral")
df_unknown = grouped.get_group("unknown")

# Check the created dataframes
df_badLength = len(df_bad)
df_goodLength = len(df_good)
df_neutralLength = len(df_neutral)
df_unknownLength = len(df_unknown)

if df_badLength + df_goodLength != dfLength - df_neutralLength - df_unknownLength:
    print("Error: the data set was split incorrectly!")

def handleDataframe(dataFrame):
  tabName = dataFrame["Alignment"].value_counts().idxmax()
  res = []
  header = dataFrame.columns.values
  for item in header:
    if item == 'Gender' or item == 'Eye color' or item == 'Race' or item == 'Hair color' or item == 'Publisher' or item == 'Skin color':
        res.append(dataFrame[item].value_counts().idxmax())
    elif item == 'Height' or item == 'Weight':
        res.append(round(dataFrame[item].describe().loc['mean'], 2))

  print("An average", tabName, "guy portrait:")

  # Display the header and values for the table
  items = ["Gender: ", "Eye color: ", "Race: ", "Hair color: ", "Height: ", "Publisher: ", "Skin color: ", "Weight: "]
  for item, name in zip(items, res):
        if type(name) == 'float': 
         print("%-12s%20d" % (item, name))
        else:
         print("%-12s%20s" % (item, name))

print("-----------------------------------")
handleDataframe(df_bad)
print("-----------------------------------")
handleDataframe(df_good)
print("-----------------------------------")


