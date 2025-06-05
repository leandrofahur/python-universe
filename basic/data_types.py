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
print(type("Hello"))
print(type('Hello'))
print(type("""Hello"""))

# Variables rules:
# 1. snake_case
# 2. Start with lowercase or underscore
# 3. Can only contain letters, numbers, and underscores
# 4. Case sensitive
# 5. Don't overwrite keywords
# 6. Don't overwrite built-in functions (dunder)
# 7. Constants are in uppercase
