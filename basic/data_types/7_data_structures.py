# Lists:
print("Lists:")
print([1, 2, 3])
print(type([1, 2, 3]))
print([1, 2, 3][0]) # 1
print([1, 2, 3][0:2]) # [1, 2]
print([1, 2, 3][::-1]) # [3, 2, 1]
print([1, 2, 3][::2]) # [1, 3]
print([1, 2, 3][::3]) # [1]
print([1, 2, 3][::4]) # [1]
print([1, 2, 3][::5]) # [1]

print([1, 2, 3] + [4, 5, 6]) # [1, 2, 3, 4, 5, 6]
print([1,'a',{'id':10, 'name':'John'}]) # [1, 'a', {'id': 10, 'name': 'John'}]

# List methods:
print("\nList methods:")
print([1, 2, 3].append(4)) # [1, 2, 3, 4]
print([1, 2, 3].pop()) # 3
print([1, 2, 3].remove(2)) # [1, 3]
print([1, 2, 3].reverse()) # [3, 2, 1]

# Matrix:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix)
print(matrix[0]) # [1, 2, 3]
print(matrix[2][1]) # 8
print(matrix[0][::-1]) # [3, 2, 1]

# Tuples:
print("\nTuples:")
print((1, 2, 3))
print(type((1, 2, 3)))

# Sets:
print("\nSets:")
print({1, 2, 3})
print(type({1, 2, 3}))

# Dictionaries:
print("\nDictionaries:")
print({"name": "John", "age": 20})
print(type({"name": "John", "age": 20}))

dictionary = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": [1, 2, 3],
}
print(dictionary)
print(dictionary["a"]) # 1
print(dictionary["b"]) # 2
print(dictionary["c"]) # 3
print(dictionary["d"]) # [1, 2, 3]
print(dictionary["d"][1]) # 2

# Variables rules:
# 1. snake_case
# 2. Start with lowercase or underscore
# 3. Can only contain letters, numbers, and underscores
# 4. Case sensitive
# 5. Don't overwrite keywords
# 6. Don't overwrite built-in functions (dunder)
# 7. Constants are in uppercase
# 8. Variables are in lowercase
# 9. Variables are mutable
# 10. Constants are immutable
# 11. Variables are dynamic
# 12. Constants are static
# 13. Variables are local
# 14. Constants are global

# GUI:
picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0],
]

print("Picture before:")
for row in picture:    
    print(row)

print("\n\nPicture after:")
for row in range(len(picture)):
    for index in range(len(picture[row])):
        # print(f'Picture[{row}][{index}]:', picture[row][index])
        if picture[row][index] == 0:
            picture[row][index] = ' '
        else:
            picture[row][index] = '*'

for row in picture:
    print(row)

print("\n\nFormated picture:")
for row in picture:
    filtered_row = ''
    for index in row:
        if index == ' ':
            filtered_row += ' '
        else:
            filtered_row += '*'
    print(filtered_row)