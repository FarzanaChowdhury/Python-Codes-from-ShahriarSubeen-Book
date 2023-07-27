import re
# cpat = re.compile(pattern)
# result = cpat.findall(string)

# Change date format
s = "22/07/2017, 20/01/2017, 01/01/2018"
new_s = re.sub(r'(\d{2})/(\d{2})/(\d{4})', r'\3-\2-\1', s)
print("new date format: ", new_s)
#Can write \g<3> instead of \3