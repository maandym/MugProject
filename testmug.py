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
		
		recipe_dic = { }
		# recipe_dic = { "directions": ""}
		for row in reader:
			#print type(row)
			recipe_dic[row["Ingredient"]] = float(row["Measurement"]), row["Unit"]
			recipe_dic["directions"] = row["Directions"] + " ",
	
	print recipe_dic		
 	return recipe_dic


#convert to grams

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
		if values != "directions":
			grams = "grams"
		grams_dict[keys] = gram_values, grams
# FIX DIRECTIONS SECTION
	return grams_dict

grams_dict = convert_to_grams(recipe_dic)
print grams_dict	
			
#sum all grams

def total_grams(dictionary):
	total_grams = 0
	for ingredients, values in grams_dict.items():
		if ingredients != "directions":
			# print ingredients
			measurement = values[0]
			total_grams += measurement
	
	return total_grams


total_grams = total_grams(recipe_dic)
# print total_grams


#find the multiplier

def multiplier(dictionary):
	multiplier = 210/total_grams
	return multiplier

multiplier = multiplier(total_grams)


#mug size amount in grams

def mug(dictionary):
	mug = {}
	for keys, values in grams_dict.items():
		if keys != "directions":
			mug_values = values[0]*multiplier
			mug[keys] = mug_values
		else:
			pass
	return mug

print mug(grams_dict)



#convert back to imperial

# def final_conversion(dictionary):
# 	final_dict = {}
# 	for keys, values in recipe_dic.items():
# 		if keys != "directions":
# 			if values[1]=="grams" and values[1]<6.0:
# 				gram_values=values[0]*multiplier
# 			elif values[1]=="grams" and values[1]<28.0:
# 				gram_values=values[0]*multiplier
# 			elif values[1]=="grams" and values[1]>28.1:
# 				gram_values=values[0]*multiplier
# 			else:
# 				print values
# 		final_dict[keys] = final_values
	
# 	return final_dict

# final_dict = final_conversion(recipe_dic)
