with open("robin.txt", "r") as t:
    hood = t.read().lower()

to_skip = ["\"", ":", ";", ",", ".", "-", "+", "=", "/", "\\",
               "|", "[", "]", "{", "}", "(", ")", "*", "^", "&", '', "!", "?"]
space = " "
word_track = {}
curr = "" # the current word we are parsing out
max_length = 0 # length of longest word yet
hist = '' # this will be used when displaying results

# iterate over each character in the file. for each character, by default we will attach that to our word string
# if its a special character, continue and skip past it.
# if we've hit a space or new line, then we're at the end of our word. so we will check our counter for that word. if it's there, increment; otherwise, add it. after we are done with that, reset our string again.
# when a new word gets added to the dict, we'll also set our max_length to that word if its the longest we've received. this will ensure we place all chars in their correct place when displaying
for chars in hood:
    if chars in to_skip:
        continue
    if chars == space or chars == "\n":
        if curr == '':
            continue
        if curr in word_track:
            word_track[curr] += 1
        else:
            if len(curr) > max_length:
                max_length = len(curr)
            word_track[curr] = 1
        curr = ""
    else:
        curr += chars

# now that we've gone through the whole document, we need to sort the tuple pairs of our word tracker. we'll do this using reverse sorting

# first get the alphabetical list of our words as tuples
# then sort them in reverse order based on the number of occurences
sort_by_word = sorted(word_track.items(), key=lambda w: w[0])
sorted_count = sorted(sort_by_word, reverse=True, key=lambda c: c[1])
# print(sorted_count)
# print(max_length) 

# now we display results. for each pair we have in the sorted list
for pair in sorted_count:
    # we will first add our word from the pair onto our histogram
    # then we can compare our max length(+2) to the length of our histogram to see how many spaces need to be between our word and hash marks
    hist += pair[0]
    
    for s in range(0, (max_length + 2) - len(hist)):
        hist += ' '

    # once we have all our spaces put into place, we add one hash for every tally in the tracker from our pair
    for h in range(0, pair[1]):
        hist += '#'
    
    #once we're done creating our histogram, we want to print and clear it for the next pair
    print(hist)
    hist = ''