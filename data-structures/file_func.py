def greet():
    print("Hello, everyone")
    # return <something>


greet()


# Variables :
#     - inside function
#     - outside function

# def name(age, name='bhavya'):  default value

# Recursion :
#   - 2 parts : best case(end) , alternate case

def upper_case(func):
    def wrapper():
        result = func().upper()
        return result

    return wrapper


# function decorator : decorator applied to return of function
@upper_case
def preet():
    return "hello"


print(preet())

# Higher order function : nested function, like calling and declaring function inside function

# Lambda function : concise one line function
dbl = lambda x: x ** 2
result = dbl(5)
print(result)

# lambda in higher order
numbers = [1,2,3,4,5]
squared = list(map(lambda x: x * 2, numbers))
print(squared)



# Function Caching and Memoization :
#     - Caching : saving values
import functools

@functools.lru_cache()
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(10))


# Memoization :
def memoize(func):
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))

# x = lambda x: x%2==0 --> lambda function to check even or odd


### Python Module : pre-stored functions
#  import module
#   while calling : module.func()

### Open files :
# f = open("file_name", #open-modes)
# Open Models :
#  r : default read only , rb : binary read only, r+ : default read and write, rb+ : binary read and write
#  w : default write only , f.readline() , f.read(x) : specific x line , f.close(),