def find_word_label(f_read, word):
	file_size = len(f_read)
	for i in range(file_size):
		dict_word = f_read[i].split('/')[0]
		# Compare upper case:
		#if (word.upper() == dict_word.upper()):
		
		if (word == dict_word):
			labels = f_read[i].split('/')[1].split('-')	
			return labels;
		
	return -1;
		
