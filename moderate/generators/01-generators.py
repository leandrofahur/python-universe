# interable
# iterate
# genertors

def generate_function(num):
    for i in range(num):
        yield i

def generate_list(num):
    result = []
    for i in range(num):
        result.append(i)
    return result

# print(generate_function(10))
# print(generate_list(10))

# for i in generate_function(10):
#     print(i)

g = generate_function(10)
print(next(g))
print(next(g))