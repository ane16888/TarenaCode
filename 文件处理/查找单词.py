word = input("请输入一个单词：")
f = open("dict.txt")
for i in f:
    m = i.split(" ",1)
    m[1]=m[1].strip()
    if word == m[len(i)]:
        print(m[len(i)][0],m[len(i)][1])