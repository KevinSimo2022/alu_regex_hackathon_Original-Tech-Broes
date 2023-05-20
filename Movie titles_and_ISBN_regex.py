import re
# !/usr/bin/python3

'''This code matches movie titles with the pattern "Title (yyyy)", 
where "Title" is any string of characters, and "yyyy" is a four-digit year.'''

# I have added incoorect formats just to point out that the regular expressions won't work if the format does not meet the requirement
Movie_title = ['Avatar (2022)', 'Inception (2019)',  'Black Panther (2022)','Bob Marley']
regex_movie = "\w+\s*\(\d{4}\)"

for movie in Movie_title:
    if re.findall(regex_movie, movie):
        print(movie, 'matches the Movie pattern')
    else:
        print(movie, "does not match the Movie pattern")



'''This code matches the pattern "ISBN xxx-x-xxx-xxxxx-x", where x is a digit'''

# I have added incoorect formats just to point out that the regular expressions won't work if the format does not meet the requirement
ISBN_numbers =['ISBN 087-5-010-50987-5', 'ISBN 0-575-08082-9', 'ISPV -79sb-79h-%', 'ISBN 007-5-010-59587-9']
regex_ISBN = '^ISBN\s+?\d{3}\-\d{1}\-\d{3}\-\d{5}\-\d{1}$'

for x in ISBN_numbers:
    if re.findall(regex_ISBN, x):
        print(x, 'is a correct ISBN')
    else:
        print(x, 'is an incorrect ISBN')