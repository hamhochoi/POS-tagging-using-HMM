import os

path = "D:\\OneDrive for Business 1\\OneDrive - student.hust.edu.vn\\OD\\20171\\NLP\\Project\\pos_tagging_materials\\datasets\\brown"
path_dict = "D:\\OneDrive for Business 1\\OneDrive - student.hust.edu.vn\\OD\\20171\\NLP\\Project\\dictionary.txt"
path_label = "D:\\OneDrive for Business 1\\OneDrive - student.hust.edu.vn\\OD\\20171\\NLP\\Project\\labels.txt"

f_dict = open(path_dict, 'w')
f_labels = open(path_label, 'w')

dir = os.listdir(path)
dir_len = len(dir)
dict = []
labels = []

for i in range(dir_len):	# dir_len
	print ('\t\t\t\t ' + str(dir[i]))
	dir_path = path + "\\" + str(dir[i])	# uncomment this

	f = open(dir_path, 'r')
	f_read = f.read();
	f_read = f_read.split('\n')

	file_size = len(f_read)	# number of lines

	# read each line in a file
	for i in range(file_size):
		words = f_read[i].split(' ')	# read each word separate by ' '
		line_size = len(words)	# numbers of words in a line.
		
		# read word in each a line
		for j in range(line_size):
			#print ("Words: \n", words)
			if (words[j] == ''):
				continue;
			word = words[j].split('/')[0]		# read each word separate by '/'
			#print (words[j].split('/')[1])
			word_labels = words[j].split('/')[1]
			word_labels = word_labels.split('-')			
			
			#print (word_labels)
			if ((word in dict)==False):
				dict.append(word)
				f_dict.write(word)
				f_dict.write('\n')
				
			for k in range(len(word_labels)):
				if ((word_labels[k] in labels) == False):
					labels.append(word_labels[k])
					f_labels.write(word_labels[k])
					f_labels.write('\n')
			
		#print (dict)		
		#print (labels)		
				
print (len(dict))
print (len(labels))
				
				
				
				
				
				
				
				
				
				
				

		