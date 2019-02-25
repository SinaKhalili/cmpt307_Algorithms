# Chapter 1: Algorithms with numbers

def gcd(a,b):
    # returns greatest common divisor using Euclid's algorithm
    if(b == 0):
        return a
    else:
        return gcd(b,a%b)
    
def lcm(a,b):
    # returns least common multiple. Exercise 1.33.
    return (a*b) / gcd(a,b)
    # a*b -> O(n^1.6..) + gcd(a,b) -> O(log(n)) + division -> O(n^2)
    # running time is : O(n^2) where n is length of a*b



