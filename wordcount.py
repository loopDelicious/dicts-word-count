# 
def word_counter(file_path):    
    """
        Returns a count of all the words in a text file. 
    """
# open file
    opened_file = open(file_path)
# create an empty dictionary
    word_count = {}
# for each line,  
#   remove extra white spaces, and split on space delimiter to return a list of each word 
    for line in opened_file:
        line = line.rstrip().split(" ")
        for word in line:
# if word is an existing key in the dictionary, increment value count by 1 
# if word is not an existing key in the dictionary, add it to the dictionary with value of 1
            if word in word_count:
                word_count[word] += 1 
            else:
                word_count[word] = 1
            # instead of if/else . . . 
            # word_count[word] = word_count.get(word, 0) + 1
    for key, value in word_count.iteritems():
        print key, value

# close file
    opened_file.close()

word_counter("test.txt")