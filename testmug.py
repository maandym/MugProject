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

def csv_recipeDict():
	
	with open("VanillaCake.csv", "rb") as csvin:
		reader = csv.DictReader(csvin)
		
		recipe_dic = { "directions": ""}
		for row in reader:
			#print type(row)
			recipe_dic[row["Ingredients"]] = row["Measurement"], row["Unit"]
			recipe_dic["directions"] = recipe_dic["directions"] + row["Directions"] + " "
	 		
			
 	return recipe_dic
recipe_dic= csv_recipeDict()

def calculate_grams(dictionary):
	total_grams = 0
	for ingredients, values in recipe_dic.items():
		if ingredients != "directions":
			measurement = float(values[0])
			total_grams += measurement
	
	return total_grams

print calculate_grams(recipe_dic)

	
	
# 	print type(row)
# 	print type(ingredient_row)
# 	#print type(ingredients)

# #conversion to grams

# for key, value in ingredient_row.items():
# 	if ingredient_row["unit"]=="c":
# 		ingredient_row["measurement"]=225*ingredient_row["measurement"]
# 		ingredient_row["unit"]="grams"
# 	elif ingredient_row["unit"]=="T":
# 		ingredient_row["measurement"]=14*ingredient_row["measurement"]
# 		ingredient_row["unit"]="grams"
# 	elif ingredient_row["unit"]=="t":
# 		ingredient_row["measurement"]=5*ingredient_row["measurement"]
# 		ingredient_row["unit"]="grams"
# 	elif ingredient_row["unit"]=="singles":
# 		ingredient_row["measurement"]=(14*ingredient_row["measurement"])*4
# 		ingredient_row["unit"]="grams"
# 	else:
# 		print "Go away."
# 	print row

# print "\n"

# #finding the multiplier


# multiplier = 210/total_grams
# print multiplier

# print "\n"

# #mug size amount in grams

# for newrow in ingredient_row:
# 	newrow["measurement"]=newrow["measurement"]*multiplier
# print newrow

# print "\n"

# #conversion back to cups

# for newrow in ingredient_row:
# 	# if newrow["unit"]==str("grams") and newrow["measurement"]<6.0:
# 	# 	newrow["measurement"]=newrow["measurement"]/14
# 	# 	newrow["unit"]="t"
# 	# elif newrow["unit"]==str("grams") and newrow["measurement"]<28.0:
# 	# 	newrow["measurement"]=newrow["measurement"]/5
# 	# 	newrow["unit"]="T"
# 	# 	newrow["unit"]="grams"
# 	# elif newrow["unit"]==str("grams") and newrow["measurement"]>29.0:
# 	# 	newrow["measurement"]=newrow["measurement"]/225
# 	# 	newrow["unit"]="c"
# 	# else:
# 	# 	print "Mandy, something went horribly wrong!"
# 	print newrow

# # for finalamounts in ingredients:
# # 	if finalamounts["unit"]==str("grams")>29:
# # 		finalamounts["measurement"]=finalamounts["measurement"]/225
# # 		finalamounts["unit"]="c"
# # 	elif finalamounts["unit"]==str("grams")<6:
# # 		finalamounts["measurement"]=finalamounts["measurement"]/14
# # 		finalamounts["unit"]="t"
# # 	elif finalamounts["unit"]==str("grams")=<28:
# # 		finalamounts["measurement"]=finalamounts["measurement"]/5
# # 		finalamounts["unit"]="T"
# # 	else:
# # 		print "Mandy, something went horribly wrong!"
# # 	print finalamounts


