import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
#get each individual word on whitespace split
each_word = words.split()
#we will store all of our words into word_coll
word_coll = {}
start_word = []
stop_word = []

for ind, word in enumerate(each_word):
    # we start iterating over the word list, pulling index and word from it.
    # we check that there's still words in the each_word list to analyze
    if ind < len(each_word) - 1:
        # then we check for our starting words conditions if the first letter is capitalized or if the first letter is a " followed by a capital it's a starting.
        if (word[0] == '"' and word[1].isupper()) or word[0].isupper():
            start_word.append(word)
        # then we check for our ending conditions. words end on .!? and those symbols followed by "
        if (word[-1] == '"' and word[:-1].endswith(("!", "?", "."))) or word.endswith(("!", "?", ".")):
            stop_word.append(word)
        # now that we have determined our start and stop words we need to determine follow words. to do this we need to check if we have the word in our dict. once we do, we will chain any words that can follow it on to the list.
        if word not in word_coll:
            word_coll[word] = []
        # at this point our word is in our dict, so now, append the word following our current word into the dict
        word_coll[word].append(each_word[ind+1])

# TODO: construct 5 random sentences
# Your code here

# since we have 5 sentences
for sen in range(5):
    # each sentence needs to start with a start word
    ran_word = random.choice(start_word)
    print(ran_word, end = ' ')
    # as long as we haven't hit a stopping word
    while ran_word not in stop_word:
        #set ran_word to a following word, chosen from the list at the index of our ran_word until we reach a word that stops it
        ran_word = random.choice(word_coll[ran_word])
        print(ran_word, end = ' ')
    print('\n')