def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    
    def helper(x):
 
        if x == 1:
            return True
        elif n % x == 0:
            return False
        else:
            return helper(x-1)
    return helper(n-1)

def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    x = 0
    
    print(n)
    if n == 1:
      return 1
    elif n % 2 == 0:
        x = hailstone(n // 2) + 1
    else:
        x = hailstone((n*3)+ 1) + 1

    return x

def merge(n1, n2):
    """ Merges two numbers by digit in decreasing order
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31) 
    3211
    """
    x=None
    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1
    else:
        return merge(n1%10+n2%10*10+n1//10*100+n2//10*1000,0)