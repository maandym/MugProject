#instructions

print "***************************************"
print
print
print
print
print "***************************************"
print "\n"

#import recipe

import fractions

import csv
with open("vanillacake.csv") as csvin:
	reader = csv.DictReader(csvin)
	ingredients = []
	for row in reader:
		print float(row["Measurement"]), row["Unit"], row["Ingredient"]
		ingredient_row = {"ingredient": row["Ingredient"], "unit": row["Unit"], "measurement": float(row["Measurement"])}
 		ingredients.append(ingredient_row)

#conversion to grams

for row in ingredients:
	if row["unit"]==str("c") or row["unit"]==str("C") or row["unit"]==str("Cup") or row["unit"]==str("cup") or row["unit"]==str("Cups") or row["unit"]==str("cup"):
		row["measurement"]=225*row["measurement"]
		row["unit"]="grams"
	elif row["unit"]==str("T") or row["unit"]==str("Tablespoon") or row["unit"]==str("tablespoon") or row["unit"]==str("Tablespoons") or row["unit"]==str("tablespoons"):
		row["measurement"]=14*row["measurement"]
		row["unit"]="grams"
	elif row["unit"]==str("t") or row["unit"]==str("Teaspoon") or row["unit"]==str("teaspoon") or row["unit"]==str("Teaspoons") or row["unit"]==str("teaspoons"):
		row["measurement"]=5*row["measurement"]
		row["unit"]="grams"
	elif row["unit"]==str("singles") or row["unit"]==str("single") or row["unit"]==str("Singles") or row["unit"]==str("Single"):
		row["measurement"]=(14*row["measurement"])*4
		row["unit"]="grams"
	else:
		print "Go away."
	print row

print "\n"

#finding the multiplier

total_grams = 0
for row in ingredients:
	total_grams = total_grams + row["measurement"]
print total_grams

multiplier = 210/total_grams
print multiplier

print "\n"

#mug size amount in grams

for newrow in ingredients:
	newrow["measurement"]=newrow["measurement"]*multiplier
	print newrow

print "\n"

#conversion back to cups

# for newrow in ingredients:
# 	if newrow["unit"]==str("grams") and newrow["measurement"]<6.0:
# 		newrow["measurement"]=newrow["measurement"]/14
# 		newrow["unit"]="t"
# 	elif newrow["unit"]==str("grams") and newrow["measurement"]<28.0:
# 		newrow["measurement"]=newrow["measurement"]/5
# 		newrow["unit"]="T"
# 		newrow["unit"]="grams"
# 	elif newrow["unit"]==str("grams") and newrow["measurement"]>29.0:
# 		newrow["measurement"]=newrow["measurement"]/225
# 		newrow["unit"]="c"
# 	else:
# 		print "Mandy, something went horribly wrong!"
# 	print newrow

# for finalamounts in ingredients:
# 	if finalamounts["unit"]==str("grams")>29:
# 		finalamounts["measurement"]=finalamounts["measurement"]/225
# 		finalamounts["unit"]="c"
# 	elif finalamounts["unit"]==str("grams")<6:
# 		finalamounts["measurement"]=finalamounts["measurement"]/14
# 		finalamounts["unit"]="t"
# 	elif finalamounts["unit"]==str("grams")=<28:
# 		finalamounts["measurement"]=finalamounts["measurement"]/5
# 		finalamounts["unit"]="T"
# 	else:
# 		print "Mandy, something went horribly wrong!"
# 	print finalamounts


