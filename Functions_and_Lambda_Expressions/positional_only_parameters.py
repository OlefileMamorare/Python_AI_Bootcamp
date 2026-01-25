#Posiotional-Only Parameters
#params that come before the / are positional-only parameters:

def my_function(a, b, /, c, d):#here a and b are positional-only parameters
    pass


def divide(numerator, denominator, /):
    """Divides two numbers"""

    if denominator == 0:
        raise ValueError('Division by zero!')
    return numerator / denominator

#correct usage:
result = divide(10, 2)
print(result)

#incorrect usage:
#res = divide(numerator=10, denominator=5)
