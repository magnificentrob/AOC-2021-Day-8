import csv
sentences = []
with open('input.txt', 'r') as file:
	reader = csv.reader(file, delimiter = ' ')
	for row in reader:
		sentences.append(row)

def sortString(str):
	return ''.join(sorted(str))
answer = 0
for sentence in sentences:	
	first10 = sentence[:10]
	last4 = sentence[-4:]
	lcheck = ''
	numbers = [''] *10

	for i in range(len(first10)):
		first10[i] = sortString(first10[i])
	for i in range(len(last4)):
		last4[i] = sortString(last4[i])

	for word in first10:
		if len(word) == 2: #1
			numbers[1] = word
		if len(word) == 4:#4
			numbers[4] = word
		if len(word) == 3: #7
			numbers[7] = word
		if len(word) == 7:#8
			numbers[8] = word

	lcheck = "".join(list(set(numbers[4]) - set(numbers[1])))
	lcheck = sortString(lcheck)
	for word in first10:
		if len(word) == 6:
			if numbers[1][0] not in word or numbers[1][1] not in word and lcheck[0] in word and lcheck[1] in word:
				numbers[6] = word
			elif numbers[1][0] in word and numbers[1][1] in word and lcheck[0] in word and lcheck[1] in word:
				numbers[9] = word
			else:
				numbers[0] = word
		elif len(word) == 5:
			if numbers[1][0] in word and numbers[1][1] in word:
				numbers[3] = word
			elif lcheck[0] in word and lcheck[1] in word:
				numbers[5] = word
			else:
				numbers[2] = word

	answerString = ''
	for num in last4:
		if num in numbers:
			answerString += str(numbers.index(num))
	print(answerString)
	answer += int(answerString)