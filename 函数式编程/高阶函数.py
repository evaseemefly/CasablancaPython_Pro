
def square(x):
    return x*x

def delegate(x,y,f):
    return f(x)+f(y)

print(delegate(2,4,square))
