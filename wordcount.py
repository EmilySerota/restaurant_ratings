def wordcount(file_name):
	"""takes in a file and prints out the set of words and the number of times each word occurs in the text file"""
	
	word_counts = {}										#create empty dictionary
	all_words = []											#create empty list that will store words
	punctuation = [ ]

	with open(file_name) as file:
		for line in file:			
			line = line.rstrip() 							#removes /n from end of lines
			words = line.split(" ")							#split phrase where there are spaces
			all_words.extend(words) 						#put words into a single list
	for word in all_words:
		word = word.lower()									#all words in lowercase

										#removing punctuation
		#for letter in ["!@#$%^&*(),./';<>?:"]:
		#			word = word.replace(letter,"")

																#remove punctuation
		word_counts[word] = word_counts.get(word, 0) + 1		
	
	for word in word_counts:
		print(word, word_counts[word])


wordcount("test.txt")