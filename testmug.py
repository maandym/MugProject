#instructions

print """
********************************************\n
	WELCOME TO THE MUG PROJECT\n
	   By Mandy C. Souza\n
********************************************\n

N/A: This is a work in progress. In the future, you will be able to input your own recipe, and the app will scale down to a single serving. Not just for cakes, but any meal you'd like to make.\n

SAFETY:\n
Please make sure your mug can withstand high temperatures. Most mugs can (as they're made of glass, pure ceramic or procelain), but some can only hold hot liquids up to 212F. If you are not sure about what you have home, a good alternative is using a small (8oz and up) MASON JAR. Those are made to take high tempartures and will not bulge or break with heat.
Be careful when touching either mug or mason jar after baking. None of them will look hot, but they will be!
Happy baking!

INSTRUCTIONS:\n
Please type the number for the recipe you would like to bake.

RECIPES TO CHOOSE FROM:

1. 	VANILLA CAKE\n
2. 	CHOCOLATE CAKE\n
3. 	RED VELVET CAKE\n
"""
#conditionals for users


option = 0
while option <1 :
    option = int(raw_input("Please choose a cake recipe: "))
    print option
    # print "Sorry, I didn't understand that."
    # print "You did not choose a valid option. Please try again."
else:
    if option==1:
        print "You have chosen to make the Vanilla Cake, here is the recipe:"
        cake = "VanillaCake.csv"
    if option==2: 
    	print "You have chosen to make the Chocolate Cake, here is the recipe:"
    	cake = "ChocolateCake.csv"
    if option==3: 
    	print "You have chosen to make the Red Velvet Cake, here is the recipe:"
    	cake = "RedVelvetCake.csv"
    if option==4: 
    	print "You have chosen to make the Butter Cake, here is the recipe:"
    	cake = "ButterCake.csv"
    if option==5: 
        print "You have chosen to make the Pound Cake, here is the recipe:"
        cake = "PoundCake.csv"
    	



#import recipe

import fractions

import csv

def csv_recipeDict():
	
	with open(cake, "rb") as csvin:
		reader = csv.DictReader(csvin)
		
		recipe_dic = { "directions": ""}
		# recipe_dic = { "directions": ""}
		for row in reader:
			#print type(row)
			recipe_dic[row["Ingredient"]] = float(row["Measurement"]), row["Unit"]
			recipe_dic["directions"] = recipe_dic["directions"] + row["Directions"] + " "
	
	# print recipe_dic
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
	return grams_dict

grams_dict = convert_to_grams(recipe_dic)
# print grams_dict	
			
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
	multiplier = 200/total_grams
	return multiplier

multiplier = multiplier(total_grams)


#mug size amount in grams

def mug(dictionary):
	mug = {}
	for keys, values in grams_dict.items():
		if keys != "directions" and values != "directions":
			mug_values = values[0]*multiplier
			grams = "grams"
			mug[keys] = mug_values, grams
		else:
			pass
	return mug

mug = mug(grams_dict)
# print mug
# print "\n"


#convert back to imperial

def final_conversion(dictionary):
	final_dict = {}
	recipe_dic= csv_recipeDict()

	for keys, values in mug.items():
		# print keys
		# print values
		if values[0]<6.0:
			final_values= float("%.2f" % float(values[0]/5))
			unit="t"
		elif values[0]<28.0:
			final_values= float("%.2f" % float(values[0]/14))
			unit="T"
		elif values[0]>28.1:
			final_values= float("%.2f" % float(values[0]/225))
			unit="c"
		else:
			print "WRONG!"
		final_dict[keys] = final_values, unit
	
	print final_values
	print "\n"
	return final_dict
	

def final_print(dictionary1, dictionary2):
	for ingredients, values in recipe_dic.items():
		if ingredients != "directions":
			print ingredients, values, "\n"
	for key, items in final_dict.items():
		print key, items

final_dict = final_conversion(mug)
final_print(recipe_dic, final_dict)

# final_conversion = final_conversion(mug)

print recipe_dic["directions"]

