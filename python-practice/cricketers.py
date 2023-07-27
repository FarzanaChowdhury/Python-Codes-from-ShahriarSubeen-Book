import re

with open("cricketers.html", "r") as fp:
    cricketers = fp.read()

# pattern = re.compile(r'<li>(.*?)</li>')
# result = pattern.findall(cricketers)
result = re.findall(r'<li>(.*?)</li>',cricketers)
# result = re.findall(r'<ul>\s*<li>\s*(.*?)<ol>\s*<li>(.*?)</li>\s*<li>(.*?)</li>\s*</ol>\s*</li>\s*</ul>', cricketers, re.MULTILINE)

pattern = r"<li>\s*([^<]+)\s*<ol>(.*?)</ol>\s*</li>"
result = re.findall(pattern, cricketers, re.DOTALL)
print(result)