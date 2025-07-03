# 1 - Given the same input, will always return the same output
# 2 - No side effects

def multiply_by_two(li1):
    new_list = []    
    for i in range(len(li1)):
        new_list.append(li1[i] * 2)
    return new_list

print(multiply_by_two([1,2,3]))



