#!/usr/bin/env python3


# Useful variables
pi = 3.14592653589793238462643383279502
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]



# Simple arithmetic
def add(a, b): # addition
    return a + b

def sub(a, b): # substraction
    return a - b

def mult(a, b): # multiplication
    return a * b

def div(a, b): # division
    return a / b

def mod(a, b): # finds modulo
    return a % b



# Simple logic checks
def isNaN(a): # check if NaN
    try:
        check = int(a)
        return False
    except:
        return True

def iseven(a): # check if even
    check = a % 2
    if check == 0:
        return True
    else:
        return False

def isodd(a): # check if odd
    check = a % 2
    if check != 0 :
        return True
    else:
        return False

def isstring(a):
    if type(a) == str:
        return True
    else:
        return False

def isint(a):
    if type(a) == int:
        return True
    else:
        return False

def isfloat(a):
    if type(a) == float:
        return True
    else:
        return False

def iscomp(a):
    if type(a) == complex:
        return True
    else:
        return False

def islist(a):
    if type(a) == list:
        return True
    else:
        return False

def istuple(a):
    if type(a) == tuple:
        return True
    else:
        return False

def isdict(a):
    if type(a) == dict:
        return True
    else:
        return False

def isrange(a):
    if type(a) == range:
        return True
    else:
        return False

def isset(a):
    if type(a) == set:
        return True
    else:
        return False

def isfrozenset(a):
    if type(a) == frozenset:
        return True
    else:
        return False

def isbool(a):
    if type(a) == bool:
        return True
    else:
        return False

def isbyte(a):
    if type(a) == bytes:
        return True
    else:
        return False

def ismemoryview(a):
    if type(a) == memoryview:
        return True
    else:
        return False

def isbytearray(a):
    if type(a) == bytearray:
        return True
    else:
        return False

def isNone(a):
    if a == None:
        return True
    else:
        return False

def isPrime(a):
    prime = False
    if a == 1:
        prime = False
    elif a > 1:
        for i in range(1, a):
            if a%i != 0:
                prime = True
                break
    return prime



# Geometry

def pythagoras(a, b, c): # Pythagoras theorem
    if a != 0 and b != 0 and c == "?":
        c = (a**2 + b**2)**0.5
        return c
    elif a == "?" and b != 0 and c != 0:
        a = (c**2 - b**2)**0.5
        return a
    elif a != 0 and b == "?" and c !=0:
        b = (c**2 - a**2)**0.5
        return b




def quadrfuncstd(a, x, b, c): # standard form quadratic function
    res = (a*(x**2)) + (b*x) + c
    return res

def quadrfuncvert(a, x, h, k): # vertex form quadratic function
    res = a * ((x-h)**2) + k
    return res

def quadrfuncpnt(vertex, point, a): # quadratic function when given a point
    firststep = "f(x) = a * (x-" + str(vertex[0]) + ")**2 +", str(vertex[1])
    secondstep = str(point[1]), "= a * (" + str(point[0]) + "-" + str(vertex[0]) + ")**2 +", str(vertex[1])
    thirdstep = str(int(point[1]) - int(vertex[1])), "= a * (" + str(point[0]) + "-" + str(vertex[0]) + ")**2"
    fourthstep = str((int(point[1]) - int(vertex[1]) / ((int(point[0]) - int(vertex[0]))**2))) + " = a"
    if a == "?": # calculates amplitude if not given
        return fourthstep
    elif a != "?" and isNaN(a) == False: # calculate function if amplitude given for vertex
        res = a * (int(point[0])-int(vertex[0]))**2 + int(vertex[1])
        return res







# Factorial
def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fac(n - 1)




# Trigonometry
# sin(x) is calculated using Bhaskaras’s Approximation Formula: ( 4*x*(180-x) ) / ( 40500 - x *(180-x) )
def sindeg(x):
    res = ( 4*x*(180-x) ) / ( 40500 - x *(180-x) )
    return res

def sinrad(x):
    res = ( 16*x*(pi-x) ) / ( 5*(pi**2) - 4*x*(pi-x) )
    return res

def sinfunc(a, b, x, c, d):
    res = a * sin((b*x + c)) + d
    return res

def cosdeg(x):
    res = sindeg(90 - x)
    return res

def cosrad(x):
    res = sinrad(90 - x)
    return res

def cosfunc(a, b, x, c, d):
    res = a * cos(b*c + c) + d
    return res

def tan(x):
    res = sindeg(x) / cosdeg(x)
    return res

def tanfunc(a, b, x, c, d):
    res = a * tan(b*x + c) + d
    return res

def deg(x): # convert radians to degrees
    rad = 180 * x/pi
    return rad

def rad(x): # convert degrees to radians
    deg = pi * x/180
    return deg





# Misc
def sroot(x): # squareroot of x
    res = x**0.5
    return res

def root(x, y): # takes y-root of x
    res = x**(1/y)
    return res

def square(x): # square of x
    res = x**2

def powerof(x, y): # x to the power of y
    res = x**y
    return res

def floor(a): # rounds a number down
    if type(a) == str:
        a = float(a)
        return int(a)
    if type(a) == int:
        return a
    elif type(a) == float:
        return int(a)

def ceil(a): # rounds a number up
    if type(a) == str:
        a = float(a)
        rounded_up_a = int(-(-a // 1))
        return rounded_up_a
    if type(a) == int:
        return a
    elif type(a) == float:
        rounded_up_a = int(-(-a // 1))
        return rounded_up_a

def asc(numlist):
    for num in range(1, len(numlist)):
       a = numlist[num]
       b = num - 1
       while b >= 0 and a < numlist[b]:
           numlist[b + 1] = numlist[b]
           b -= 1
           numlist[b + 1] = a
    return numlist


def desc(numlist):
    n = len(numlist)
    for num in range(n):
        already_sorted = True
        for i in range(n - num - 1):
            if numlist[i] < numlist[i + 1]:
                numlist[i], numlist[i + 1] = numlist[i + 1], numlist[i]
                already_sorted = False
            if already_sorted == True:
                break
    return numlist

def prime(x, y):
    prime_list = []
    for n in range(x, y):
        isPrime = True

        for num in range(2, n):
            if n % num == 0:
                isPrime = False

        if isPrime:
            prime_list.append(n)
    return prime_list


def egyptmult(a, b):
    p = 0
    while a > 0:
        if isodd(a) == True:
            p = p + b
        a = floor(a/2)
        b = b * 2
    return p

