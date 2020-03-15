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

# Largest prime factor
def p3():
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
    count = 1
    n = 0
    while count <= 10001:
        n += 1
        if isPrime(n):
            count += 1
    print(n)

def product(sequence):
    return functools.reduce(lambda x,y: x*y, sequence, 1)

# Largest product in a series
def p8():
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
    c = 1
    while True:
        for b in range(1, c):
            for a in range(1, b):
                if isTriplet(a, b, c) and a+b+c == 1000:
                    print(f"found triplet {a}^2 + {b}^2 = {c}^2")
                    print(f"product = {a*b*c}")
                    return
        c += 1

# Summation of primes
def p10():
    total = 0
    for n in range(1, 2000000):
        if isPrime(n):
            total += n
    print(total)

# Largest product in a grid
def p11():
    grid = [
        [ 8, 2,22,97,38,15,00,40,00,75, 4, 5, 7,78,52,12,50,77,91, 8],
        [49,49,99,40,17,81,18,57,60,87,17,40,98,43,69,48, 4,56,62,00],
        [81,49,31,73,55,79,14,29,93,71,40,67,53,88,30, 3,49,13,36,65],
        [52,70,95,23, 4,60,11,42,69,24,68,56, 1,32,56,71,37, 2,36,91],
        [22,31,16,71,51,67,63,89,41,92,36,54,22,40,40,28,66,33,13,80],
        [24,47,32,60,99, 3,45, 2,44,75,33,53,78,36,84,20,35,17,12,50],
        [32,98,81,28,64,23,67,10,26,38,40,67,59,54,70,66,18,38,64,70],
        [67,26,20,68, 2,62,12,20,95,63,94,39,63, 8,40,91,66,49,94,21],
        [24,55,58, 5,66,73,99,26,97,17,78,78,96,83,14,88,34,89,63,72],
        [21,36,23, 9,75,00,76,44,20,45,35,14,00,61,33,97,34,31,33,95],
        [78,17,53,28,22,75,31,67,15,94, 3,80, 4,62,16,14, 9,53,56,92],
        [16,39, 5,42,96,35,31,47,55,58,88,24,00,17,54,24,36,29,85,57],
        [86,56,00,48,35,71,89, 7, 5,44,44,37,44,60,21,58,51,54,17,58],
        [19,80,81,68, 5,94,47,69,28,73,92,13,86,52,17,77, 4,89,55,40],
        [ 4,52, 8,83,97,35,99,16, 7,97,57,32,16,26,26,79,33,27,98,66],
        [88,36,68,87,57,62,20,72, 3,46,33,67,46,55,12,32,63,93,53,69],
        [ 4,42,16,73,38,25,39,11,24,94,72,18, 8,46,29,32,40,62,76,36],
        [20,69,36,41,72,30,23,88,34,62,99,69,82,67,59,85,74, 4,36,16],
        [20,73,35,29,78,31,90, 1,74,31,49,71,48,86,81,16,23,57, 5,54],
        [ 1,70,54,71,83,51,54,69,16,92,33,48,61,43,52, 1,89,19,67,48]
    ]
    length = 20
    adjacent = 4
    greatestProduct = 0

    # Vertical
    for y in range(length):
        for x in range(length - adjacent + 1):
            selection = grid[y][x:x+4]
            prod = product(selection)
            if prod > greatestProduct:
                greatestProduct = prod
                print(f"product of {selection} == {prod}")

    # Horizontal
    for x in range(length):
        for y in range(length - adjacent + 1):
            selection = [grid[y][x], grid[y+1][x], grid[y+2][x], grid[y+3][x]]
            prod = product(selection)
            if prod > greatestProduct:
                greatestProduct = prod
                print(f"product of {selection} == {prod}")

    # Diagonal
    for y in range(length - adjacent + 1):
        for x in range(length - adjacent + 1):
            # Diagonal (left to right)
            selection = [grid[y][x], grid[y+1][x+1], grid[y+2][x+2], grid[y+3][x+3]]
            prod = product(selection)
            if prod > greatestProduct:
                greatestProduct = prod
                print(f"product of {selection} == {prod}")

            # Diagonal (right to left)
            selection = [grid[y][x+3], grid[y+1][x+2], grid[y+2][x+1], grid[y+3][x]]
            prod = product(selection)
            if prod > greatestProduct:
                greatestProduct = prod
                print(f"product of {selection} == {prod}")

def divisors(n):
    divisors_list = []
    limit = math.ceil(math.sqrt(n))
    for i in range(1, limit):
        if n % i == 0:
            divisors_list.append(i)
            if i != n/i:
                divisors_list.append(n/i)
    return len(divisors_list)

# Highly divisible triangular number
def p12():
    triangle = 1
    i = 2
    while True:
        if divisors(triangle) > 500:
            print(triangle)
            break
        print(f"{triangle} + {i} = {triangle + i}")
        triangle += i
        i += 1


p12()
