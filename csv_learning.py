print "***************************************"
print
print
print
print
print "***************************************"
print "\n"

import fractions

import csv
with open("vanillacake.csv") as csvin:
	reader = csv.DictReader(csvin)
	for row in reader:
		print float(row["Measurement"]), row["Unit"], row["Ingredients"]


