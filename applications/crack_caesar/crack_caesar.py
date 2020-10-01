# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# set up necessary stores. letter_count will track the frequency of items in the document. this will be compared to freq_list to provide us with our decrypt key. decrypted will be the string returned upon decryption
letter_count = {}
freq_list = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']
decrypt_key = {}
decrypted = ""

# access the encrypted information to crack
with open("ciphertext.txt", encoding="utf-8") as encrypted:
    cipher = encrypted.read()

# once we have our encrypted file, we go through each letter.
# if the letter is a special character, we'll ignore it.
# otherwise, we'll check if the letter is in our frequency counter or not, and increment appropriately.
for letter in cipher:
    if letter.isalpha():
        if letter not in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1

# with all the letters accounted for and counted
# we will create a list
# and then we will sort the list in descending order, flipping each pair around to match (freq, letter)
sort_cipher = list(letter_count.items())
sort_cipher.sort(reverse=True, key=lambda item: item[1])

# since our sort_cipher is sorted in descending order, ind0 is our most frequent letter.
# so we can enumerate over our freq_list, and for each index and letter in there, match it up with the corresponding letter in our sort cipher
# this matching will be saved in our decrypt key dict as {encrypt:decrypt}
for ind, letter in enumerate(freq_list):
    decrypt_key[sort_cipher[ind][0]] = freq_list[ind]

# now that we have the key for our cipher, cycle through it again.
# for each character that is a letter, attach the value found at that letter in our key to our decrypted string. otherwise, if it's a special character, just attach it without doing anything to it.
for letter in cipher:
    if letter.isalpha():
        decrypted += decrypt_key[letter]
    else:
        decrypted += letter

print(decrypted)

