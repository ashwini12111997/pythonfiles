# rfile = open ("test.txt", "r")
# print("name of file: ", rfile.name)
# print("closed or not : ", rfile.closed)
# print("opening mode : ", rfile.mode)

file = open ("test.txt", "w+")
str1 = "\n\n hello everyone all the best"
file.write(str1)
file.close()

file = open ("test.txt", "r")
str2 = file.read(20)
print("name of file: ", str2)
# file.close()

pos = file.tell()
print("current position : ", pos)
pos = file.seek(0,0)
print("seek position : ", pos)
print(file.read(100))
file.close()