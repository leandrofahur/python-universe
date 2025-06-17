my_file = open("test.txt", "r")

# # read the file and print the content and reset the cursor to the beginning of the file:
# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())

# # read the file line by line:
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())

# read the file line by line and print the content:
print(my_file.readlines())
# for line in my_file.readlines():
    # print(line)


my_file.close()