import csv
outputValues = []
with open('input.txt', 'r') as file:
	reader = csv.reader(file, delimiter = ' ')
	for row in reader:
		outputValues += row[-4:]

uniquenumber = 0
#1 = length 2 | 4 = length 4 | 7 = length 3 | 8 = length 7
a=2
b=4
c=3
d=7
for i in outputValues:
	if len(i) == a or len(i) == b or len(i) == c or len(i) == d:
		uniquenumber += 1