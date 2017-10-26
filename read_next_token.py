path = "D:\\OneDrive for Business 1\\OneDrive - student.hust.edu.vn\\OD\\20171\\NLP\\Project\\pos_tagging_materials\\datasets\\brown"

f = open(path + "\\ca1.txt", 'r')
f_read = f.read();
f_read = f_read.split('\n')
file_size = len(f_read)

def read_next_token(f_read, current_line, current_word):
	if (current_word < 0):		# To append 2 fake word in beggining of line.
		return "XXXXXX"

	if (current_line >= file_size):
		return "EOF";		# End of file.
		
	read_line = f_read[current_line].split(' ')
	line_size = len(read_line)
	
	if (current_word >= line_size):
		if (current_word  <= line_size ):	# To append 2 fake word in end of line
			return "XXXXXX"
		else:
			return "EOL";	# Don't have next word
	
	char = read_line[current_word]
	return char;
	
	
'''
current_line = 0;
current_word = -2;	
char = ''

while (char != "EOF"):		
	char = read_next_token(f_read, current_line, current_word)
	current_word = current_word + 1
	if (char == "EOL"):
		current_line = current_line + 1;
		current_word = -2		# To append 2 fake word in beggining of line
	if (char == "EOL" or char == "EOF"):
		continue;
	#print (char)

'''