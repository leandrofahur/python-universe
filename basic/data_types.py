# Fundamental data types:

# Integers:
print("Integers:")
print(type(2 + 4))
print(type(2 - 4))
print(type(2 * 4))
print(type(2 / 4))
print(type(2 // 4)) # 0.5
print(type(2 % 4))
print(type(2 ** 4))

# Caveat: Operator precedence
# 1. Parentheses () 
# 2. Exponents **
# 3. Multiplication and Division (from left to right) * / // %
# 4. Addition and Subtraction (from left to right) + -  

# Floats:
print("\nFloats:")
print(type(2.0 + 4.0))
print(type(2.0 - 4.0))
print(type(2.0 * 4.0))
print(type(2.0 / 4.0))
print(type(2.0 // 4.0))
print(type(2.0 % 4.0))
print(type(2.0 ** 4.0))

# Built-in functions:
print("\nBuilt-in functions:")
print(round(3.1)) # 3
print(round(3.5)) # 4
print(round(3.9)) # 4
print(abs(-20)) # 20

# Binary, Hexadecimal, Octal:
print("\nBinary, Hexadecimal, Octal:")
print(bin(5)) # 0b101
print(hex(10)) # 0xa
print(oct(10)) # 0o12

# Caveat: Bin to int:
print("\nCaveat: Bin to int:")
print(int("0b101", 2)) # 5

#  Complex numbers:
print("\nComplex numbers:")
print(5j) # 5j
print(5J) # 5J
print(complex(5)) # 5+0j
print(complex(5, 2)) # 5+2j

# Strings:
print("\nStrings:")
print("Hello")
print('Hello')
print("""Hello""")
print('Hello'[0]) # H
print('Hello'[0:3]) # Hel
# [start:stop:step]
print('Hello'[::-1]) # olleH
print('Hello'[::2]) # Hlo
print('Hello'[::3]) # Hl
print('Hello'[::4]) # Hl
print('Hello'[::5]) # Hl

# Formatting strings:
print("\nFormatting strings:")
print("Hello {}".format("World")) # Hello World
print("Hello {0} {1}".format("World", "Python")) # Hello World Python
print("Hello {name} {age}".format(name="World", age=20)) # Hello World 20
print("Hello {0:.2f}".format(3.14159)) # Hello 3.14
print(f"Hello {20}") # Hello 20
print(f"Hello {20:.2f}") # Hello 20.00
a = "Hello"
b = "World"
print(f"{a} {b}") # Hello World

# Boolean:
print("\nBoolean:")
print(True)
print(False)

# None:
print("\nNone:")
print(None)
print(type(None))

# Lists:
print("\nLists:")
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
