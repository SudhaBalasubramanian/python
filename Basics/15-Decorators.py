def check_factorial(func):
    def wrapper_func(n):
        if type(n) == int and n > 0:
            return func(n)
        else:
            raise Exception(f'{n} is not a non-negative number')
    return wrapper_func



@check_factorial
def factorial(n):
    if n== 1:
        return 1
    else:
        return n*factorial(n-1)
    
for i in range(1, 10):
    print(i, factorial(i))

try:
    print(factorial(-1))
except Exception as e:
    print(e)

try:
    print(factorial(1.354))
except Exception as e:
    print(e)
