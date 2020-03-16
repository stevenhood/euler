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
    return list(map(int, divisors_list))

# Highly divisible triangular number
def p12():
    triangle = 1
    i = 2
    while True:
        if len(divisors(triangle)) > 500:
            print(triangle)
            break
        print(f"{triangle} + {i} = {triangle + i}")
        triangle += i
        i += 1

# Large sum
def p13():
    values = [
        37107287533902102798797998220837590246510135740250,
        46376937677490009712648124896970078050417018260538,
        74324986199524741059474233309513058123726617309629,
        91942213363574161572522430563301811072406154908250,
        23067588207539346171171980310421047513778063246676,
        89261670696623633820136378418383684178734361726757,
        28112879812849979408065481931592621691275889832738,
        44274228917432520321923589422876796487670272189318,
        47451445736001306439091167216856844588711603153276,
        70386486105843025439939619828917593665686757934951,
        62176457141856560629502157223196586755079324193331,
        64906352462741904929101432445813822663347944758178,
        92575867718337217661963751590579239728245598838407,
        58203565325359399008402633568948830189458628227828,
        80181199384826282014278194139940567587151170094390,
        35398664372827112653829987240784473053190104293586,
        86515506006295864861532075273371959191420517255829,
        71693888707715466499115593487603532921714970056938,
        54370070576826684624621495650076471787294438377604,
        53282654108756828443191190634694037855217779295145,
        36123272525000296071075082563815656710885258350721,
        45876576172410976447339110607218265236877223636045,
        17423706905851860660448207621209813287860733969412,
        81142660418086830619328460811191061556940512689692,
        51934325451728388641918047049293215058642563049483,
        62467221648435076201727918039944693004732956340691,
        15732444386908125794514089057706229429197107928209,
        55037687525678773091862540744969844508330393682126,
        18336384825330154686196124348767681297534375946515,
        80386287592878490201521685554828717201219257766954,
        78182833757993103614740356856449095527097864797581,
        16726320100436897842553539920931837441497806860984,
        48403098129077791799088218795327364475675590848030,
        87086987551392711854517078544161852424320693150332,
        59959406895756536782107074926966537676326235447210,
        69793950679652694742597709739166693763042633987085,
        41052684708299085211399427365734116182760315001271,
        65378607361501080857009149939512557028198746004375,
        35829035317434717326932123578154982629742552737307,
        94953759765105305946966067683156574377167401875275,
        88902802571733229619176668713819931811048770190271,
        25267680276078003013678680992525463401061632866526,
        36270218540497705585629946580636237993140746255962,
        24074486908231174977792365466257246923322810917141,
        91430288197103288597806669760892938638285025333403,
        34413065578016127815921815005561868836468420090470,
        23053081172816430487623791969842487255036638784583,
        11487696932154902810424020138335124462181441773470,
        63783299490636259666498587618221225225512486764533,
        67720186971698544312419572409913959008952310058822,
        95548255300263520781532296796249481641953868218774,
        76085327132285723110424803456124867697064507995236,
        37774242535411291684276865538926205024910326572967,
        23701913275725675285653248258265463092207058596522,
        29798860272258331913126375147341994889534765745501,
        18495701454879288984856827726077713721403798879715,
        38298203783031473527721580348144513491373226651381,
        34829543829199918180278916522431027392251122869539,
        40957953066405232632538044100059654939159879593635,
        29746152185502371307642255121183693803580388584903,
        41698116222072977186158236678424689157993532961922,
        62467957194401269043877107275048102390895523597457,
        23189706772547915061505504953922979530901129967519,
        86188088225875314529584099251203829009407770775672,
        11306739708304724483816533873502340845647058077308,
        82959174767140363198008187129011875491310547126581,
        97623331044818386269515456334926366572897563400500,
        42846280183517070527831839425882145521227251250327,
        55121603546981200581762165212827652751691296897789,
        32238195734329339946437501907836945765883352399886,
        75506164965184775180738168837861091527357929701337,
        62177842752192623401942399639168044983993173312731,
        32924185707147349566916674687634660915035914677504,
        99518671430235219628894890102423325116913619626622,
        73267460800591547471830798392868535206946944540724,
        76841822524674417161514036427982273348055556214818,
        97142617910342598647204516893989422179826088076852,
        87783646182799346313767754307809363333018982642090,
        10848802521674670883215120185883543223812876952786,
        71329612474782464538636993009049310363619763878039,
        62184073572399794223406235393808339651327408011116,
        66627891981488087797941876876144230030984490851411,
        60661826293682836764744779239180335110989069790714,
        85786944089552990653640447425576083659976645795096,
        66024396409905389607120198219976047599490197230297,
        64913982680032973156037120041377903785566085089252,
        16730939319872750275468906903707539413042652315011,
        94809377245048795150954100921645863754710598436791,
        78639167021187492431995700641917969777599028300699,
        15368713711936614952811305876380278410754449733078,
        40789923115535562561142322423255033685442488917353,
        44889911501440648020369068063960672322193204149535,
        41503128880339536053299340368006977710650566631954,
        81234880673210146739058568557934581403627822703280,
        82616570773948327592232845941706525094512325230608,
        22918802058777319719839450180888072429661980811197,
        77158542502016545090413245809786882778948721859617,
        72107838435069186155435662884062257473692284509516,
        20849603980134001723930671666823555245252804609722,
        53503534226472524250874054075591789781264330331690,
    ]
    print(str(sum(values))[0:10])

def collatz(start):
    seq = [start]
    n = start
    while n > 1:
        if n % 2 == 0:
            # n is even
            n = int(n/2)
        else:
            # n is odd
            n = (3*n)+1
        seq.append(n)
    return seq

# Longest Collatz sequence
def p14():
    largestChain = 0
    for n in range(1000000):
        seq = collatz(n)
        length = len(seq)
        if length > largestChain:
            largestChain = length
            print(n)

# Lattice paths
def p15():
    pass

# Power digit sum
def p16():
    x = 2**1000
    sum_of_digits = sum(list(map(lambda n: int(n), str(x))))
    print(sum_of_digits)

# Number letter counts
def p17():
    single = ['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    tens_map = {
        1: 'ten',
        2: 'twenty',
        3: 'thirty',
        4: 'forty',
        5: 'fifty',
        6: 'sixty',
        7: 'seventy',
        8: 'eighty',
        9: 'ninety',
    }

    totalLen = 0
    for n in range(1000):
        if n < len(single):
            totalLen += len(single[n])
            print(single[n])
        else:
            number_in_words = ''
            hundreds = math.floor(n / 100)
            tens = math.floor((n - hundreds * 100) / 10)
            units = n - (tens * 10) - (hundreds * 100)
            combined_tens_and_units = False
            # print(f"hundreds: {hundreds}")
            # print(f"tens: {tens}")
            # print(f"units: {units}")

            if hundreds > 0:
                number_in_words += single[hundreds] + 'hundred'

            if hundreds > 0 and (tens > 0 or units > 0):
                number_in_words += 'and'

            if tens == 1 and units >= 0:
                combined_tens_and_units = True
                number_in_words += single[units + 10]
            elif tens > 1:
                number_in_words += tens_map[tens]

            # e.g. "eleven"
            if not combined_tens_and_units:
                number_in_words += single[units]

            totalLen += len(number_in_words)
            print(f"{n} = {number_in_words}")
    print('onethousand')
    totalLen += len('onethousand')
    print(totalLen)

# Maximum path sum I
def p18():
    triangle = [
        [75],
        [95,64],
        [17,47,82],
        [18,35,87,10],
        [20, 4,82,47,65],
        [19, 1,23,75, 3,34],
        [88, 2,77,73, 7,63,67],
        [99,65, 4,28, 6,16,70,92],
        [41,41,26,56,83,40,80,70,33],
        [41,48,72,33,47,32,37,16,94,29],
        [53,71,44,65,25,43,91,52,97,51,14],
        [70,11,33,28,77,73,17,78,39,68,17,57],
        [91,71,52,38,17,14,91,43,58,50,27,29,48],
        [63,66, 4,68,89,53,67,30,73,16,69,87,40,31],
        [ 4,62,98,27,23, 9,70,98,73,93,38,53,60, 4,23]
    ]

    testTriangle = [
        [3],
        [7,4],
        [2,4,6],
        [8,5,9,3]
    ]

    for row in range(len(testTriangle)):
        print(testTriangle[row])

# Counting Sundays
def p19():
    # start on Tuesday as 01/01/1901 was a Tuesday
    days_of_the_week = ['mon','tue','wed','thu','fri','sat','sun']
    days_in_each_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    total_day_count = 0
    sundays_on_first_of_month = 0

    for year in range(1901, 2001):
        leap_year = year % 4 == 0
        for month in range(1, 13):
            days_in_month = days_in_each_month[month]
            if leap_year and month == 2:
                days_in_month += 1
            #print(f"{year}/{month}: days = {days_in_month}")
            for day in range(1, days_in_month + 1):
                total_day_count += 1
                #print(f"{year}/{month}/{day} is a {days_of_the_week[total_day_count % len(days_of_the_week)]}")
                if day == 1 and days_of_the_week[total_day_count % len(days_of_the_week)] == 'sun':
                    #print(f"found sunday on {year}/{month}/{day} ({total_day_count})")
                    sundays_on_first_of_month += 1
    print(sundays_on_first_of_month)

# Factorial digit sum
def p20():
    factorial = lambda n: product(range(1, n+1))
    print(sum(map(int, str(factorial(100)))))

# Amicable numbers
def p21():
    def d(n):
        # Sum of proper divisors of n
        # (numbers less than n which divide evenly into n)
        return sum(filter(lambda x: x < n, divisors(n)))
    amicable = set()
    for a in range(1, 10000):
        b = d(a)
        if d(b) == a and a != b:
            amicable.add(a)
            amicable.add(b)
    print(sum(amicable))

p21()
