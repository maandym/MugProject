import os
from flask import Flask, render_template

#instructions
text = """
***************************************\n





***************************************\n
\n
"""
#conditionals for users




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
		if keys != "directions" and values != "directions":
			mug_values = values[0]*multiplier
			grams = "grams"
			mug[keys] = mug_values, grams
		else:
			pass
	return mug

mug = mug(grams_dict)
print mug
print "\n"


#convert back to imperial

def final_conversion(dictionary):
	final_dict = {}
	for keys, values in mug.items():
		# print keys
		# print values
		if values[0]<6.0:
			final_values=values[0]/5
			unit="t"
		elif values[0]<28.0:
			final_values=values[0]/14
			unit="T"
		elif values[0]>28.1:
			final_values=values[0]/225
			unit="c"
		else:
			print "WRONG!"
		final_dict[keys] = final_values, unit
	
	

	print final_values
	return final_dict
print final_conversion(mug)
final_dict = final_conversion(mug)


#FLAAAAASK

from flask import Flask, render_template
app = Flask(__name__) 

@app.route('/')
def hello():
    msg=text
    final_dict = final_conversion(mug)
    ingredients = final_dict.keys()
    print ingredients
    measurements = final_dict.values()
    print measurements
    return render_template('index.html', msg=msg, ingredients=ingredients,  measurements=measurements, final_dict=final_dict)

if __name__=='__main__':
    #IP settings to run on cloud9
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)), debug=True) #for running in cloud9
    #IP settings to run on local machine
    # app.run(debug=True, port=5000)  