import re
s="Bangladesh is our homeland"

match = re.search('o\w\w', s)
print("Starting from n, then 2 more words: ", match.group())

# Only words/letters
match = re.search('\w+h',s)
print("Only words/letters", match.group())

# Including spaces
match = re.search('.+h',s)
print("Including spaces: " , match.group())

# Starting from n, until the first h
match = re.search('n.+?h', s)
print("Starting from n, until the first h :", match.group())

# Get only the phone number(aka, digits)
text = "Phone number is 01234567890"
match = re.search('\d+',text)
print("Get only the phone number(aka, digits) : " ,match.group())

# Get the number that has 11 digits
# Phone numbers have 11 digits
text = "House no : 5 Phone no: 01234567890"
match = re.search('\d{11}', text)
print("Get the number that has 11 digits: ", match.group())

# If there is space, get the whole number
# \s denotes space bar. * means there can be 1 or more spaces. \s? means can be at most 1 space
text = "House no : 5 Phone no: 012 34567890"
match = re.search('\d{3}\s*\d{8}', text)
print("If there is space, get the whole number: " ,match.group())

# Multiple numbers
# use findall()
text = "multiple -phone numbers, 01711111111, 01822222222, 00000000000, 019 34523234"
result = re.findall(r'\d{3}\s*\d{8}', text)
print(result)

#Specify 'one among these values'
result = re.findall(r'01[56789]\s*\d{8}',text)
print(result)

# Select Everything
print(re.findall(r'^.*?$',text, re.MULTILINE))

# Select the contents of a <li>
text = "<li>Tamim</li><li>Mustafiz</li><li>Mominul</li><li>Mahmudullah</li><li>Shakib</li>"
result = re.findall(r'<li>(.*?)</li>', text)
print("Result is: ",result)