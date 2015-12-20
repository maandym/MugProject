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
<<<<<<< HEAD
			recipe_dic[row["Ingredient"]] = float(row["Measurement"]), row["Unit"]
			recipe_dic["directions"] = recipe_dic["directions"] + row["Directions"] + " "
	 		
		
	print recipe_dic	
=======
			recipe_dic[row["Ingredient"]] = row["Measurement"], row["Unit"]
			recipe_dic["directions"] = recipe_dic["directions"] + row["Directions"] + " "
	 		
	print recipe_dic		
>>>>>>> a1673230452345f134097df27b8c88b2d5927aff
 	return recipe_dic
recipe_dic= csv_recipeDict()

def convert_to_grams(dictionary):
	grams_dict = {}
	for keys, values in recipe_dic.items():
		if keys != "directions":
			if values[1]=="c":
				gram_values=values[0]*225
			elif values[1]=="T":
				gram_values=values[0]*14
			elif values[1]=="t":
				gram_values=values[0]*5
			elif values[1]=="singles":
				gram_values=(values[0]*14)*4
			else:
				print values
		grams_dict[keys] = gram_values
	
	return grams_dict

grams_dict = convert_to_grams(recipe_dic)
			
			


def total_grams(dictionary):
	total_grams = 0
	for ingredients, values in grams_dict.items():
		if ingredients != "directions":
			print ingredients
			measurement = values
			total_grams += measurement
	
	return total_grams


total_grams = total_grams(recipe_dic)

def multiplier(dictionary):
	multiplier = 210/total_grams
	return multiplier

print multiplier(total_grams)
	
	
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


