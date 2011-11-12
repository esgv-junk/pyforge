from decorators import *

def decorator(arg):
    def inner_decorator(func):
        print('Calling inner on ' + str(func))
        
        return func
    
    print('Calling outer on ' + str(arg))
    return inner_decorator

@partial_decorator(vectorize, (0, 'x'))
def f(x, y=20):
    return x + y

print(f(x=[10, 20, 30], y=200))