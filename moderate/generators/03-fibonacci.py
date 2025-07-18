# def generate_function(num):
#     for i in range(num):
#         yield i

# def generate_list(num):
#     result = []
#     for i in range(num):
#         result.append(i)
#     return result

def fibonacci_generator(num):
    num1 = 0
    num2 = 1

    for i in range(num):
        yield num1
        temp = num1
        num1 = num2
        num2 = temp + num2

for i in fibonacci_generator(10):
    print(i)
    
    
    
    
    
    
    