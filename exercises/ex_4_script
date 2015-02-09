# Romeo And Juliet Exercise

# store file name. --- not sure what this does
file_name = "romeo.txt"

# open the file.
my_file = open( "romeo.txt", "r")

# declare empty list
script_list = []

# loop over lines in file.
for current_line in my_file:

    if current_line != '\n':
    	# add line to list
    	script_list.append( current_line )
    
my_file.close()



# count number of lines
num_lines = len(script_list)

# count number of characters including spaces and punctuation.  also count words
num_words = 0
num_characters = 0
# loop over lines in script list
for line in script_list:
	num_characters = num_characters + len(line)
	num_words = num_words + len(line.split())


# Strip punctuation and make lowercase
no_chars = []
for line in script_list:
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

	no_chars.append (clean_line)

# convert list of clean lines into list of words
word_list = []
for line in no_chars:
	word_list.extend (line.split())

# Create dictionary of unique words
word_dict = {}
for word in word_list:
	if word not in word_dict:
		word_dict[ word ] = 0

# Insert counts into dictionary
for word in word_list:
	word_dict[word] += 1

