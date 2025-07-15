# Generators are useful when we are calculating
# long lists of values

from time import time

def performance(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f"Time taken: {end_time - start_time} seconds")
        return result
    return wrapper

A_BIG_NUMBER = 1000000
num = A_BIG_NUMBER

# This is a long time function using a generator
@performance
def long_time(num):
    for i in range(num):
        i*5
        yield i

# This is a long time function using a list
@performance
def long_time2(num):
    result = []
    for i in list(range(num)):
        result.append(i*5)
    return result

long_time(num)
long_time2(num)
