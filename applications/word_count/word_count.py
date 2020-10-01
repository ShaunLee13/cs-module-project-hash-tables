def word_count(s):
    # create a dictionary to store our counted words
    dict_words = {}

    # define a list that holds our special characters
    exceptions = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']
    # list comprehension to join any characters that aren't in exceptions list to an empty string and then split at whitespace into a new list of just words
    s2 = ''.join(char.lower() for char in s if not char in exceptions)
    indiv_words = s2.split()

    #for every word in the list,
    for word in indiv_words:
        # if there are no words, continue and return dict_words which will be empty
        if word == " ":
            continue
        # if the word is already in the dict, increment counter
        elif word in dict_words:
            dict_words[word] += 1
        # otherwise start the counter in the dict
        else:
            dict_words[word] = 1
    return dict_words



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))