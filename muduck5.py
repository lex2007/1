fh = open("hello.txt", "w")
fh.write("hello.txt\n")
fh.close()
fh = open("hello.txt", "r")
print(fh.read())
fh.close()