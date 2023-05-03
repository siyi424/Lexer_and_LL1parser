import re

a = 'row: 22, type: Identifier, content: c'
match = re.search(r"type:\s*(\w+)", a)
if match:
    print(match.group())