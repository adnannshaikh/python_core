# At least 8 char long
# contain any sort letters,number $%#@

import re

# pattern = re.compile(r"(^[a-zA-Z\d$%#]+@[a-zA-Z\d]+\.[a-zA-Z\d]+$)")
#
# string = "adnan123@gmail.com"
#
# print(pattern.search(string))

pass_pattern = re.compile(r"[a-zA-Z\d%$#@]{8,}\d")

password = 'adnansjuf9@84a1A2'

check = pass_pattern.fullmatch(password)
print(check)