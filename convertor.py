def convertor(dataset, heroName):
    # Set parameters for the search
    heroProfile = dataset[dataset["Name"] == heroName]
    heroAlignment = heroProfile["Alignment"].values[0]
    heroHeight = heroProfile["Height"].values[0]
    heroWeight = heroProfile["Weight"].values[0]

    def oppositeAlignment(heroAlignment):
        if heroAlignment == 'good':
            return 'bad'
        else:
            return 'good'
        
    # Find the hero with the opposite alignment and most similar height/weight
    def converted():
        convertedAlignment = oppositeAlignment(heroAlignment)
        count = 0

        while count < 20:
         converted = dataset.loc[(dataset["Height"] > heroHeight - count) & (dataset["Height"] < heroHeight + count) & (dataset["Weight"] < heroWeight + count) &\
         (dataset["Weight"] > heroWeight - count) & (dataset["Alignment"] == convertedAlignment), ["Name", "Gender", "Alignment", "Height", "Weight"]]
         
         if converted.empty != True:
             if len(converted) > 1:
                 print(converted.head(1))
                 return converted
             else:
                 print(converted)
                 return converted
         count += 1
         if count == 20:
             print("not found")

    converted()
      
