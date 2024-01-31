#!/usr/bin/env python3
import strng
import ma

def random_number(minimum,maximum): # another possible rng but it uses the time module
    now = str(time.time())
    rnd = float(now[::-1][:3:])/1000
    return minimum + rnd*(maximum-minimum)

# Don't actually use it. importing the built-in random module is faster and more efficient
def randint(x, y, z): # random number between x and y in z intervalls
    rand_set = set()
    for i in range(x, y, z):
        rand_set.add(str(i))
    for e in rand_set:
        return int(e)

def randintv2(): # version 2 of the randint function
    lst=[0]
    lst.append(lst[-1]+1)
    a=str(id(lst[-1]))
    num=0
    for i in (a):
        num+=int(i)
    n=(str(num)[1])
    n=int(n)
    return(n)

def randstr(strlist): # random string in a list
    str_set = set()
    for i in range(0, len(strlist), 1):
        str_set.add(str(i))
    for e in str_set:
        rstr = str(strlist[int(e)-1])
        return rstr

def floatdummy(x, y, z): # dummy function for the randfloat function random number between x and y in z intervalls
    rand_set = set()
    for i in range(x, y, z):
        rand_set.add(str(i))
    for e in rand_set:
        return int(e)

def randfloat(x, y, comma): # wip doesn't work yet
    dummy1 = randintv2()
    dummy = randint(1, 100, 1)
    rand_float = str(randintv2())
    rand_float = rand_float + "."
    res = rand_float + str(floatdummy(dummy1, dummy, 1))
    return res

def randchoice(inp): # random choice in a list or string
    e = 0
    for i in inp:
        e += 1
    a = randint(0, e, 1)
    return inp[a]

def randprime(start, end):
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
    random_prime = randchoice(prime(start, end))
    return random_prime

print(randprime(1, 100))
