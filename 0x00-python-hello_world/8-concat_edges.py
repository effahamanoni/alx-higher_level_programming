#!/usr/bin/python3

# Set the variable str to the long string
str = "Python is an interpreted, interactive, object-oriented programming \
        language that combines remarkable power with very clear syntax"

# Slice the string to get the words "interpreted, interactive, object-oriented"
substr1 = str[39:67]

# Slice the string to get the word "power"
substr2 = str[107:112]

# Slice the string to get the word "Python"
substr3 = str[:6]

# Concatenate the three substrings to form the new string
new_str = substr1 + substr2 + substr3

# Print the new string
print(new_str)

