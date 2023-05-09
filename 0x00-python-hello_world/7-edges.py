#!/usr/bin/python3

# Set the variable word to "Holberton"
word = "Holberton"

# Get the first three characters of the string and assign them to the variable word_first_3
word_first_3 = word[:3]

# Get the last two characters of the string and assign them to the variable word_last_2
word_last_2 = word[-2:]

# Get the characters of the string from the second character up to but not including the last character and assign them to the variable middle_word
middle_word = word[1:-1]

# Print the values of word_first_3, word_last_2, and middle_word using the format() method
print("First 3 letters: {}".format(word_first_3))
print("Last 2 letters: {}".format(word_last_2))
print("Middle word: {}".format(middle_word))

