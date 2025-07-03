# map
# map(func,iterable)
def multiply_by_two(item):
    return item * 2

print(map(multiply_by_two,[1,2,3]))
print(list(map(multiply_by_two,[1,2,3])))
# print(list(map(lambda item: item * 2,[1,2,3])))

# zip(iterable1,iterable2)
print(list(zip([1,2,3],[4,5,6])))

# reduce