import pandas as pd
from pandas.errors import DataError

def convertor(dataset, heroName):
    heroProfile = dataset[dataset["Name"] == heroName]
    heroAlignment = heroProfile["Alignment"].values[0]
    heroHeight = heroProfile["Height"].values[0]
    heroHeightMax = heroHeight + 20
    heroHeightMin = heroHeight - 20
    heroWeight = heroProfile["Weight"].values[0]
    heroWeightMax = heroWeight + 20
    heroWeightMin = heroWeight - 20
    heroSkinColor = heroProfile["Skin color"].values[0]
    heroGender = heroProfile["Gender"].values[0]

    def oppositeAlignment(heroAlignment):
        if heroAlignment == 'good':
            return 'bad'
        else:
            return 'good'
    
    def converted():
        convertedAlignment = oppositeAlignment(heroAlignment)
        try:
            converted = dataset.loc[(dataset["Height"] > heroHeightMin) & (dataset["Height"] < heroHeightMax) & (dataset["Weight"] < heroWeightMax) & (dataset["Weight"] > heroWeightMin) &\
            (dataset["Skin color"] == heroSkinColor) & (dataset["Alignment"] == convertedAlignment), ["Name", "Height", "Weight"]]
            print(converted)
            return converted
        except DataError:
                print("not found")    
        #if converted.empty
    converted()