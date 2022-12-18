def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    
    """
    i = 0
    total = 1
    while (i < k):
        total = total * n
        i = i + 1
        n = n - 1
        
    return total    
               

def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    """   print(4224 % 10, 422 % 10, 42 % 10, 4 % 10 )
    print(    None ,4224 // 10, 4224 // 100, 4224 // 1000)

    a = y % 10
    b = (y // 10) % 10
    c = (y // 10) % 10
    d = (y // 10) % 10
    """

    sum = 0
    while (y > 0): 
    
        sum = sum + (y % 10)
  
        y = y // 10
       
    return sum
   
def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(28828)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    doubleEight = 0
    while n > 0:
        if n % 10 == 8: #checks if last digit is 8
            n = n // 10 #removes last digit of n
            if n % 10 == 8:
                return True
        n = n // 10
    return False