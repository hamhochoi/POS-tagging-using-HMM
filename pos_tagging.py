import os
from read_next_token import read_next_token
from find_word_in_dictionary import find_word_label

untagged_path = "D:\\OneDrive for Business 1\\OneDrive - student.hust.edu.vn\\OD\\20171\\NLP\\Project\\pos_tagging_materials\\datasets\\untagged"
path = "D:\\OneDrive for Business 1\\OneDrive - student.hust.edu.vn\\OD\\20171\\NLP\\Project\\pos_tagging_materials\\datasets\\brown"

untagged_dir = os.listdir(untagged_path)
untagged_len = len(untagged_dir)

# find all labels
all_labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j']	

for i in range(untagged_len):	 
	file_name = untagged_dir[i]
	path_file = untagged_path + "\\" + str(file_name)		
	f = open(path_file, 'r')
	f_read = f.read();
	f_read = f_read.split('\n')
	file_size = len(f_read)
	
	current_line = 0;
	current_word = 0;	# To append 2 fake word in beginning of line.
	word = ''
	
	while (word != "EOF"):		
		word = read_next_token(f_read, current_line, current_word)
		pre_word = read_next_token(f_read, current_line, current_word-1)
		pre_pre_word = read_next_token(f_read, current_line, current_word-2)
		
		current_word = current_word + 1
		if (word == "EOL"):
			current_line = current_line + 1;
			current_word = 0
		if (word == "EOL" or word == "EOF"):
			continue;
		print (word)
		
		labels = find_word_label(f_read, word)
		pre_labels = find_word_label(f_read, pre_word)
		pre_pre_labels = find_word_label(f_read, pre_pre_word)
		
		if (labels == -1):
			labels = all_labels
		if (pre_labels == -1):
			pre_labels = all_labels	
		if (pre_pre_labels == -1):
			pre_pre_labels = all_labels
			
			
		print (labels)
		print (pre_labels)
		print (pre_pre_labels)
		
		
	
	
