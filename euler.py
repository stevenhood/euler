#!/usr/bin/env python3

import functools
import math

# Multiples of 3 and 5
def p1():
    sum = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    print(sum)

# Even Fibonacci numbers
def p2():
    f1 = 1
    f2 = 2
    # 2 is even, so add it to the initial sum
    sum = 2
    while f2 < 4000000:
        new_term = f1 + f2
        if new_term % 2 == 0:
            sum += new_term
        f1, f2 = f2, new_term
    print(sum)

# Largest prime factor
def p3():
    def isPrime(n):
        # Prime numbers are greater than 1
        if n <= 1:
            return False

        for i in range(2, n):
            if (n % i) == 0:
                return False
        return True

    val = 600851475143
    largest_prime_factor = 1
    for i in range(1, val):
        if val % i == 0 and isPrime(i) and i > largest_prime_factor:
            largest_prime_factor = i
        print(f"i: {i}, largest: {largest_prime_factor}")
    print(largest_prime_factor)

# Largest prime factor (optimal solution)
def p3_optimal():
    n = 600851475143
    if n % 2 == 0:
        lastFactor = 2
        n = n / 2
        while n % 2 == 0:
            n = n / 2
    else:
        lastFactor = 1
    factor = 3
    maxFactor = math.sqrt(n)
    while n > 1 and factor <= maxFactor:
        if n % factor == 0:
            n = n / factor
            lastFactor = factor
            while n % factor == 0:
                n = n / factor
            maxFactor = math.sqrt(n)
        factor = factor + 2
    if n == 1:
        print(lastFactor)
    else:
        print(n)

# Largest palindrome product
def p4():
    reverse = lambda s: ''.join(reversed(s))
    largestProduct = 0
    for x in range(999, 99, -1):
        for y in range(999, 99, -1):
            product = x * y
            if str(product) == reverse(str(product)):
                if product > largestProduct:
                    largestProduct = product
    print(largestProduct)

# Smallest multiple
def p5():
    n = 1
    while True:
        smallest = True
        for i in range(2, 21):
            if n % i != 0:
                smallest = False
                break
        if smallest:
            print(n)
            return
        n += 1

# Sum square difference
def p6():
    limit = 101
    sumofsquares = (sum(map(lambda x: x**2, range(limit))))
    squareofsum = (sum(range(limit))**2)
    print(squareofsum - sumofsquares)

# 10001st prime
def p7():
    # Optimised version of isPrime (see PDF)
    def isPrime(n):
        if n == 1: return False
        if n < 4: return True
        if n % 2 == 0: return False
        if n < 9: return True
        if n % 3 == 0: return False
        r = math.floor(math.sqrt(n))
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            if n % (f + 2) == 0:
                return False
            f = f + 6
        return True
    count = 1
    n = 0
    while count <= 10001:
        n += 1
        if isPrime(n):
            count += 1
    print(n)

# Largest product in a series
def p8():
    def product(sequence):
        return functools.reduce(lambda x,y: x*y, sequence, 1)
    thousanddigits = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
    largestProduct = 0    
    start = 0
    end = 13
    while end <= len(str(thousanddigits)):
        prod = product(map(int, str(thousanddigits)[start:end]))
        if prod > largestProduct:
            largestProduct = prod
        start += 1
        end += 1
    print(largestProduct)

# Special Pythagorean triplet
def p9():
    isTriplet = lambda a,b,c: a**2 + b**2 == c**2
    s = 1000
    c = 1
    while True:
        for b in range(1, c):
            for a in range(1, b):
                if isTriplet(a, b, c) and a+b+c == 1000:
                    print(f"found triplet {a}^2 + {b}^2 = {c}^2")
                    print(f"product = {a*b*c}")
                    return
        c += 1

p9()
