import re

s = "Afganistan, America, Bangladesh, Canada, NewZealand, Denmark, England, Greenland, Netherlands, Iceland, Sweden"

countries = s.split(",")
print(countries)

li = [item for item in countries if item.endswith("land") or item.endswith("lands")]
print(li)

li_regular_expression = re.findall(r'(\w+lands*)', s)
# '*' makes the 's' in 'lands' optional
# 'r' is used for backslash 

print(li_regular_expression)