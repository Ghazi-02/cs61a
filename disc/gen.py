### Mutability

def add_this_many(x, el, s):
    """ Adds el to the end of s the number of times x occurs in s.
    >>> s = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """
    z = 0
    counter = 0
    for i in range(len(s)):
        if x == s[i]:
            counter += 1
    while z < counter:
        s.append(el)
        z += 1
    
### Generators
def filter_iter(iterable, f):
    """
    >>> is_even = lambda x: x % 2 == 0
    >>> list(filter_iter(range(5), is_even)) # a list of the values yielded from the call to filter_iter
    [0, 2, 4]
    >>> all_odd = (2*y-1 for y in range(5))
    >>> list(filter_iter(all_odd, is_even))
    []
    >>> naturals = (n for n in range(1, 100))
    >>> s = filter_iter(naturals, is_even)
    >>> next(s)
    2
    >>> next(s)
    4
    """
    #yield [x for x in iterable if f(x)]
    #yield from iterable
    #yield  from f(iterable) 
    for x in iterable:
        if f(x) == True:
            yield x
def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def helper(i):
        if i > (n ** 0.5): # Could replace with i == n
            return True
        elif n % i == 0:
            return False
        return helper(i + 1)
    return helper(2)

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def helper(i):
        if i > (n ** 0.5): # Could replace with i == n
            return True
        elif n % i == 0:
            return False
        return helper(i + 1)
    return helper(2)

def primes_gen(n):
    """Generates primes in decreasing order.
    >>> pg = primes_gen(7)
    >>> list(pg)
    [7, 5, 3, 2]
    """
    i = n-1
    lst = [n]
    while i > 1:
        lst = lst + [i]
        i = i - 1     
    
    for x in lst:
        if is_prime(x) == True:
            yield x

def primes_gen_recur(n):
    """Generates primes in decreasing order.
    >>> pg = primes_gen_recur(7)
    >>> list(pg)
    [7, 5, 3, 2]
    """
    if n == 1:
        return 0
    if is_prime(n):
        yield n
    yield from primes_gen_recur(n-1)
