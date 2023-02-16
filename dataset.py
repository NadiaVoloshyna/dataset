"""
Program: dataset.py
Author: Nadiia Voloshyna
"""
import pandas as pd
import math
from convertor import convertor
from analysis import compute

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
   heroAlignment = ''
   print("Error: The hero with this name does not exist!")

# Get dataframes with good and bad heroes
grouped = df.groupby(df.Alignment)
df_bad = grouped.get_group("bad")
df_good = grouped.get_group("good")

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
if heroProfile.empty != True and heroAlignment == 'good' or heroAlignment == 'bad':
   print(f"The converted hero for {str(hero)} is:")
   convertor(df, hero)

# Make 2D arrays with female and male height/weight attributes
df_female = df[df["Gender"] == 'Female']
df_femaleHeightWeight = df_female.loc[(df_female["Height"] > 0) & (df_female["Weight"] > 0), ["Height", "Weight"]]
female_npArray = df_femaleHeightWeight.to_numpy()

df_male = df[df["Gender"] == 'Male']
df_maleHeightWeight = df_male.loc[(df_male["Height"] > 0) & (df_male["Weight"] > 0), ["Height", "Weight"]]
male_npArray = df_maleHeightWeight.to_numpy()

# Display the results of the ideal weight to real weight comparison
print("....................................")
print("Some statistics about the heroes:")
res = compute(male_npArray, 'male')
print(f"Healthy male heroes: {str(res[0])}\nUnhealthy male heroes: {str(res[1])}")
res = compute(female_npArray, 'female')
print(f"Healthy female heroes: {str(res[0])}\nUnhealthy female heroes: {str(res[1])}")
print("....................................")
