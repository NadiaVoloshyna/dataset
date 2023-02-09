"""
Program: dataset.py
Author: Nadiia Voloshyna
"""
import pandas as pd
import math

hero = input("Enter the hero's name: ")
heroes = pd.read_csv("C:\ABERTAY\Voloshyna_Week5-assignment\SuperHeroes.csv", sep=';')
df = heroes.copy()
print(len(df))

# Check if the hero's name exists and get the hero's data
names = df.groupby(df.Name)
try:
   heroProfile = names.get_group(hero)
   heroAlignment = heroProfile["Alignment"].values[0]
except KeyError:
   heroProfile = pd.DataFrame()
   print("Error: the hero with this name does not exist!")

# Get dataFrames with good and bad heroes
grouped = df.groupby(df.Alignment)
df_bad = grouped.get_group("bad")
df_good = grouped.get_group("good")
df_neutral = grouped.get_group("neutral")
df_unknown = grouped.get_group("unknown")

# Check the created dataframes
dfLength, df_badLength, df_goodLength, df_neutralLength, df_unknownLength = len(heroes), len(df_bad), len(df_good), len(df_neutral), len(df_unknown)
if df_badLength + df_goodLength != dfLength - df_neutralLength - df_unknownLength:
    print("Error: the data set was split incorrectly!")

# Calculate frequency for non-numeric values and a mean for numeric values. Make a list of characteristics
def handleDataframe(dataFrame):
  res = []
  header = dataFrame.columns.values
  for item in header:
    if item == 'Gender' or item == 'Eye color' or item == 'Race' or item == 'Hair color' or item == 'Publisher' or item == 'Skin color':
        res.append(dataFrame[item].value_counts().idxmax())
    elif item == 'Height' or item == 'Weight':
      value = round(dataFrame[item].describe().loc['mean'], 2)
      if math.isnan(value) == True:
         res.append('X')
      else:
         res.append(value)
  return res

# Display the header and values for the table of comparison
def compare(dataFrame, heroProfile):
   print("%29s%22s" % (hero, f"Average {heroAlignment}"))
   print("-----------------------------------------------------")

   list = handleDataframe(heroProfile)
   res = handleDataframe(dataFrame)
   items = ["Gender: ", "Eye colour: ", "Race: ", "Hair colour: ", "Height: ", "Publisher: ", "Skin colour: ", "Weight: "]
   for item, el, name in zip(items, list, res):
        if type(name) == 'float': 
         print("%-12s%20d%20d" % (item, el, name))
        else:
         print("%-12s%20s%20s" % (item, el, name))
   print("-----------------------------------------------------")

if heroProfile.empty !=True:
   if heroAlignment == 'bad':
      compare(df_bad, heroProfile)
   else:
      compare(df_good, heroProfile)


