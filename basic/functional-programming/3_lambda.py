# lambda functions are anonymous functions that can be used to create a function object.
# lambda functions are defined using the lambda keyword.
# lambda functions are used to create a function object.
# lambda param: function(param)

print(lambda x: x + 1)

print(list(map(lambda x: x + 1, [1, 2, 3, 4, 5])))
print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])))