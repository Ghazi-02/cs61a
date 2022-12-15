def is_even(x):
        # Even numbers have remainder 0 when divided by 2.
        return x % 2 == 0
    
def make_keeper(n):
    """Returns a function which takes one parameter cond and prints
    out all integers 1..i..n where calling cond(i) returns True.

    
    >>> make_keeper(5)(is_even)
    2
    4
    """
  
    def check_condition(cond):
        i = 1
        while i <= n:
            if cond(i) == True:
                print(i)
                i = i + 1
            else:
                i = i + 1
            
    return  check_condition 