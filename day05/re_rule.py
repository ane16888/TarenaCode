import re
a = re.findall(r'\(.+?\)',"(abcd)efgh(higk)")
print(a) # ['(abcd)', '(higk)']
s= "dd1949年10月1号，中华人民共和国成立"
it = re.finditer(r"\d+",s)
for i in it:
    print(i.group())

obj =re.match(r"\d+",s)
print(obj)
obj = re.search(r"\d+",s)
print(obj)
obj = re.fullmatch(r".+",s)
print(obj)