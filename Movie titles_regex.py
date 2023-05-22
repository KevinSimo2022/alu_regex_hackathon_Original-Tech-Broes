import re
# !/usr/bin/python3

# I have added incoorect formats just to point out that the regular expressions won't work if the format does not meet the requirement
'''ISBN_numbers =['ISBN 087-5-010-50987-5', 'ISBN 0-575-08082-9', 'ISPV -79sb-79h-%', 'ISBN 007-5-010-59587-9']
regex_ISBN = '^ISBN\s+?\d{3}\-\d{1}\-\d{3}\-\d{5}\-\d{1}$'

for x in ISBN_numbers:
    if re.findall(regex_ISBN, x):
        print(x, 'is a correct ISBN')
    else:
        print(x, 'is an incorrect ISBN')'''

# I am trying to be smart here
# This code matches an input and loops through it. If the input matches my regular expression pattern,
# it will print out Good movie. And if it dosen't, It will print out, Bad movie
# I only modifed this code after our learning coach said we could use input functions
# the previous version of this code is on github

'''This code matches movie titles with the pattern "Title (yyyy)", 
where "Title" is any string of characters, and "yyyy" is a four-digit year.'''

# !/usr/bin/python3
import re

pattern = "\w+\s*\(\d{4}\)"

while True:
    try:
        # this Prompts the user to enter a movie title or data type
        user_input = input("Enter a movie title or data type (or 'quit' to exit): ")

        # If user input is 'quit', break out of the loop
        if user_input == 'quit':
            break

        # this Checks if the user input matches the regular expression pattern
        if re.search(pattern, user_input):
            print(user_input, 'is a good match for the pattern')
            break # Exit the loop if the input matches the pattern
        else:
            print(user_input, 'is a bad match for the pattern')

    except:
        print("An error occurred while processing the user input.")
        continue