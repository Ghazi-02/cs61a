def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    i = 1
    factors = 0
    while i <= n:
        if(n % i == 0):
            i = i + 1
            factors = factors + 1 
        elif (n % i != 0):
            i = i + 1
    
    if(n == 1):
        return False
    elif (factors > 2):
        return False
    else:
        return True

def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    if n == 1:
        return False
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k += 1
    return True

def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> result is None  # No return value
    True
    """
    i = 1
    while i <= n :
        if(i % 5 == 0 and i % 3 == 0 ):
            print("FizzBuzz")
            i= i + 1
            
        elif(i % 5 == 0):
            print("Buzz")
            i = i + 1 
         
        elif(i % 3 == 0):
            print("Fizz")
            i = i + 1
            
        else:
            print(i)
            i=i+1   

def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(1313131) # 1 and 3
    2
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(10000) # 0 and 1
    2
    >>> unique_digits(101) # 0 and 1
    2
    >>> unique_digits(10) # 0 and 1
    2
    """
    i = 0
    qtyU = 0
    while i < 10:
        if(has_digit(n,i) == True):

            qtyU = qtyU + 1
        i = i + 1
    return qtyU
 


def has_digit(n, k):
    """Returns whether K is a digit in N.
    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """


    while n > 0:
        if(n % 10 == k):
            return True
        elif(n % 10 != k):
            n = n // 10
    if(n != k ):
        return False
      
        
     