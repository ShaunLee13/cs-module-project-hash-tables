def no_dups(s):
    # create a list to hold our used words, and a string to attach words onto
    words = {}
    dup_free = ""

    # split all words in the string being passed in
    for word in s.split():
        # if we haven't encountered the word, and it isn't whitespace
        # attach f-string to our result string, and add the word to our dict
        if word not in words and word != "":
            dup_free += f'{word} '
            words[word] = 1
    # then return our string, stripped of whitespace at the end
    return dup_free.strip()



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))