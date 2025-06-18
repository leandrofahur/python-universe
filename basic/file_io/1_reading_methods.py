fs = open("test.txt")
print(fs)

# read(): reads the whole file content and print it:
print("read():")
print(fs.read())
print(fs.read()) # nothing will be printed because the cursor is at the end of the file

# seek(0): reset file cursor to the beginning of the file:
fs.seek(0)


# readline(): reads the first line of the file and print it:
print("readline():")
print(fs.readline())

# readlines(): reads the whole file content and print it as a list of lines:
print("readlines():")
print(fs.readlines())

fs.close()

