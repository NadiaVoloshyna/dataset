INCH_TO_CENTIMETERS = 2.54
FIVE_FEET_TO_INCHES = 60

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

