"""
A collection of simple math operations
"""

def simple_add(a,b):
    """Addition of 2 numbers.

    Parameters
    ----------
    a : int float
        The first number to add.
    b : int float
        The second number to add.

    Returns
    -------
    a+b : int float
        The sum of a and b.
    """    
    return a+b

def simple_sub(a,b):
    """Subtraction of 2 numbers.

    Parameters
    ----------
    a : int float
        The first number.
    b : int float
        The second number.

    Returns
    -------
    a-b : int float
        The difference of a and b.
    """
    return a-b

def simple_mult(a,b):
    """Multiplication of 2 numbers.

    Parameters
    ----------
    a : int float
        The first number.
    b : int float
        The second number.

    Returns
    -------
    a*b : int float
        The product of a and b.
    """
    return a*b

def simple_div(a,b):
    """Division of 2 numbers.

    Parameters
    ----------
    a : int float
        The first number.
    b : int float
        The second number.

    Returns
    -------
    a/b : int float
        The quotient of a and b.
    """
    return a/b

def poly_first(x, a0, a1):
    """Polynomial of first order (linear function).

    Parameters
    ----------
    x : int float
        The input value.
    a0 : int float
        The constant term.
    a1 : int float
        The coefficient of the first-order term.

    Returns
    -------
    a0 + a1*x : int float
        The value of the first-order polynomial at x.
    """    
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    """Polynomial of second order (non-linear function)

    Parameters
    ----------
    x : int float
        The input value.
    a0 : int float
        The constant term.
    a1 : int float
        The coefficient of the first-order term.
    a2 : int float
        The coefficient of the second-order term.

    Returns
    -------
    a0 + a1*x + a2*(x**2) : int float
        The value of the second-order polynomial at x.
    """    
    return poly_first(x, a0, a1) + a2*(x**2)

# Feel free to expand this list with more interesting mathematical operations...
# .....
