"""Count words in file."""

import sys

txt = open(sys.argv[1])

# tokenizing
def tokenize(file=txt):
    """return a list of words from file"""
    words = []
    
    for line in file:

        # split the line for space
        split_line = line.rstrip().split(' ')
        words.extend(split_line)
    
    return words

# word_count

def count_words(words):
    """ take in list of words, return dict of how many times each word appears"""
    
    # create empty word count dictionary
    word_count = {}
    
    for word in words:
                word = word.lower().rstrip('.,?')
                word_count[word] = word_count.get(word, 0) + 1
    
    return word_count


# Print each key: value pair
def print_dict(word_count):
    for key, value in word_count.items():
        print(f'{key} : {value}')
    return


print_dict(count_words(tokenize()))


