path = "D:\\OneDrive for Business 1\\OneDrive - student.hust.edu.vn\\OD\\20171\\NLP\\Project\\pos_tagging_materials\\datasets\\brown"

f = open(path + "\\dictionary.txt", 'r')
f_read = f.read();
f_read = f_read.split('\n')
file_size = len(f_read)


def find_word_label(word):
	for i in range(file_size):
		dict_word = f_read[i].split('/')[0]
		# Compare upper case:
		#if (word.upper() == dict_word.upper()):
		
		if (word == dict_word):
			labels = f_read[i].split('/')[1].split(',')	
			return labels;
		
	return -1;
		
