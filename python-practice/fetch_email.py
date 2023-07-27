import re
text = "hello mew book12@subeen.com book@subeen thank you"

match = re.findall(r'\w+@\w+[.]+\w+', text)
print(match)

text = "Email your feedback book@subeen.com, py.book@subeen.com thanks"
match = re.findall(r'[.\w]+@+\w+[.]+\w+',text)
print(match)

text = "book at subeen.com, book AT subeen.com, book (at) subeen.com, book [at] subeen [dot] com"
match = re.sub(r'\s*[\[\(]*\s*at\s*[\]\)]*\s+', '@',text, flags =re.IGNORECASE)
match2 = re.sub(r'\s*[\[\(]*\s*dot\s*[\]\)]\s*', ".", match, flags = re.I)
print(match2)