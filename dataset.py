"""
Program: dataset.py
Author: Nadiia Voloshyna
"""
import pandas as pd
import math
from convertor import convertor

INCH_TO_CENTIMETERS = 2.54
FIVE_FEET_TO_INCHES = 60

hero = input("Enter the name: ")
heroes = pd.read_csv("C:\ABERTAY\Voloshyna_Week5-assignment\SuperHeroes.csv", sep=';')
df = heroes.copy()

# Check if the hero's name exists and get the hero's data
names = df.groupby(df.Name)
try:
   heroProfile = names.get_group(hero)
   heroAlignment = heroProfile["Alignment"].values[0]
except KeyError:
   heroProfile = pd.DataFrame()
   print("Error: the hero with this name does not exist!")

# Get dataframes with good and bad heroes
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
      value = round(dataFrame[item].mean(), 2)
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

if heroProfile.empty != True:
   if heroAlignment == 'bad':
      compare(df_bad, heroProfile)
   elif heroAlignment == 'good':
      compare(df_good, heroProfile)
   else:
      print("The hero is neither bad nor good")

# Convert a bad hero to the good and vice versa
print("The converted hero for " + str(hero) + " is ")
convertor(df, hero)

# Make ndarrays with female and male height and weight attributes
df_female = df[df["Gender"] == 'Female']
df_femaleHeightWeight = df_female.loc[(df_female["Height"] > 0) & (df_female["Weight"] > 0), ["Height", "Weight"]]
femaleHeightWeightnp = df_femaleHeightWeight.to_numpy()

df_male = df[df["Gender"] == 'Male']
df_maleHeightWeight = df_male.loc[(df_male["Height"] > 0) & (df_male["Weight"] > 0), ["Height", "Weight"]]
maleHeightWeightnp = df_maleHeightWeight.to_numpy()

# Calculate the ideal weight
def idealWeight(height, str):
   heightIn = height / INCH_TO_CENTIMETERS
   if str == 'female':
      idealWeight = round(float(49 + 1.7 * (heightIn - FIVE_FEET_TO_INCHES)), 2)
   else:
      idealWeight = round(float(52 + 1.9 * (heightIn - FIVE_FEET_TO_INCHES)), 2)
   return idealWeight

# Compute the number of heroes with healthy and unhealthy weight 
def compute(npArray, str):
   healthyHeroes = 0
   unhealthyHeroes = 0
   for el in npArray:
      heroHeight = el[0] 
      heroWeight = el[1]
      idealHeroWeight = idealWeight(heroHeight, str)
      if heroWeight < idealHeroWeight:
         healthyHeroes += 1
      else:
         unhealthyHeroes += 1
   return healthyHeroes, unhealthyHeroes

print("............................")
res = compute(maleHeightWeightnp, 'male')
print("Healthy male heroes: " + str(res[0]), "\nUnhealthy male heroes: " + str(res[1]))
print("............................")
res = compute(femaleHeightWeightnp, 'female')
print("Healthy female heroes: " + str(res[0]), "\nUnhealthy female heroes: " + str(res[1]))
print("............................")