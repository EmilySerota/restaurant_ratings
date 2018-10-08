def wordcount(file_name):
	"""takes in a file and prints out the set of words and the number of times each word occurs in the text file"""
	
	word_counts = {}
	all_words = []
	
	with open(file_name) as file:
		for line in file:
			line = line.rstrip() #removes /n from end of lines
			words = line.split(" ")
			all_words.extend(words) 
	for word in all_words:
		word_counts[word] = word_counts.get(word, 0) + 1		
	
	for word in word_counts:
		print(word, word_counts[word])


wordcount("test.txt")