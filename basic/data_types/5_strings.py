print("Strings:")
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
