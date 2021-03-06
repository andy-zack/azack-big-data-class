# ROMEO AND JULIET EXERCISE

# open the file.
my_file = open( "romeo.txt", "r")

# declare empty list
list_of_lines = []

# loop over lines in file.
for current_line in my_file:

	# check that current line is not blank
    if current_line != '\n':
    	# add line to list
    	list_of_lines.append( current_line )
    
my_file.close()



# count number of lines
number_of_lines = len(list_of_lines)

# COUNT NUMBER OF CHARACTERS INCLUDING SPACES AND PUNCTUATION.  ALSO COUNT WORDS
# set word counter to 0
number_of_words = 0
# set character counter to 0
number_of_characters = 0
# loop over lines in script list
for line in list_of_lines:
	# add the number of characters in current line to cumulative total
	number_of_characters = number_of_characters + len(line)
	# add the number of words in current line to cumulative total
	number_of_words = number_of_words + len(line.split())


# Strip punctuation and make lowercase
# declare an empty list
list_of_lines_without_punctuation = []

# loop over all lines
for line in list_of_lines:
	clean_line = line.lower()
	clean_line = clean_line.replace(","," ")
	clean_line = clean_line.replace("."," ")
	clean_line = clean_line.replace("!"," ")
	clean_line = clean_line.replace("?"," ")
	clean_line = clean_line.replace("-"," ")
	clean_line = clean_line.replace("["," ")
	clean_line = clean_line.replace("]"," ")
	clean_line = clean_line.replace(":"," ")
	clean_line = clean_line.replace(";"," ")
	clean_line = clean_line.replace("*"," ")
	clean_line = clean_line.replace("("," ")
	clean_line = clean_line.replace(")"," ")
	clean_line = clean_line.replace("\""," ")
	clean_line = clean_line.replace("\n","")

	# Append cleaned current line to list of lines w/o punctuation
	list_of_lines_without_punctuation.append (clean_line)

# convert list of clean lines into list of words
# declare an empty list for all the words
word_list = []

# loop over the list of lines w/o puncutation
for line in list_of_lines_without_punctuation:
	# add each word from current line to the cumulative list of all words
	word_list.extend (line.split())

# Create dictionary of unique words
word_dict = {}
# loop over list of words w/o punctuation
for word in word_list:
	# add current word to dictionary if it's not already in the dictionary
	if word not in word_dict:
		word_dict[ word ] = 0

# Insert counts into dictionary
for word in word_list:
	word_dict[word] += 1

