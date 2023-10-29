inputs = eval(input())


# inputs = [1, 2, 3]


# def logging_decorator(fn):
#     def wrapper(*args):
#         print(f"You called {fn.__name__}{args}")
#         result = fn(args[0], args[1], args[2])
#         print(f"It returned: {result}")
#
#     return wrapper

def logging_decorator(function):
    # You called a_function(1, 2, 3)
    # It returned: 6
    def logging(*args):
        print(f"You called {function.__name__}{args}")
        print(f"It returned: {function(*args)}")

    return logging


@logging_decorator
def a_function(a, b, c):
    return a * b * c


a_function(inputs[0], inputs[1], inputs[2])
