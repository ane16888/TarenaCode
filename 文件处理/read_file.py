"""
文件读取演示
"""
f = open('file')
# while True:
#     data = f.read(2)
#     if not data:
#         break
#     print(data)
data = f.readline(8)
print(data)
f.close()