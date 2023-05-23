# !/usr/bin/python3

import re

# I have added incorect formats just to point out that the regular expressions won't work if the format does not meet the requirement
ISBN_numbers =['ISBN 087-5-010-50987-5', 'ISBN 0-575-08082-9', 'ISPV -79sb-79h-%', 'ISBN 007-5-010-59587-9']
regex_ISBN = '^ISBN\s+?\d{3}\-\d{1}\-\d{3}\-\d{5}\-\d{1}$'

for x in ISBN_numbers:
    if re.findall(regex_ISBN, x):
        print(x, 'is a correct ISBN')
    else:
        print(x, 'is an incorrect ISBN')