print("Built-in functions:")
print(round(3.1)) # 3
print(round(3.5)) # 4
print(round(3.9)) # 4
print(abs(-20)) # 20

print("\nBinary, Hexadecimal, Octal:")
print(bin(5)) # 0b101
print(hex(10)) # 0xa
print(oct(10)) # 0o12

print("\nCaveat: Bin to int:")
print(int("0b101", 2)) # 5
