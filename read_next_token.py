def read_next_token(f_read, current_line, current_word):
	file_size = len(f_read)
	
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
