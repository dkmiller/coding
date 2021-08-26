import math

# 19.1. Swap two numbers in place. This doesn't work if the numbers are so large
# that overflow occurs.
def swap_in_place(a, b):
    a = a + b
    b = a - b
    a = a - b
    return (a,b)

# 19.3. Compute the number of trailing zeros in the factorial of n.
# Mathematically, this is the min(v_2(n!),v_5(n!)).
def num_trailing_zeros_in_factorial(n):
    # Compures v_p(n!)
    def v(p,n):
        ppow = p
        result = 0
        for e in xrange(int(math.log(n,p))):
            result += n/ppow
            ppow *= p
        return result
    return min(v(2,n),v(5,n))

# 19.4. Finds the max of two numbers.
def clever_max(a, b):
    pass
