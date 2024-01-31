#!/usr/bin/env python3
import strng




def killdupe(strlist): # kills duplicates in a string or list. Doesn't work atm
    no_dupe = "" .join(dict.fromkeys(strlist))
    return no_dupe

def rem(a, b): # removes element a in the list b
    new_list = b
    if a in b:
        pos_a = int(strpos(a, b))
        new_list = new_list[:pos_a] + new_list[pos_a+1:]
    return new_list

def remv2(a, b): # same as above but with built-in in pop() method
    new_list = b
    if a in b:
        new_list.pop(a)
    return new_list

def remall(inp): # removes every item of a list
    e = 0
    for i in inp:
        e += 0
    return inp[e:e]

def copy(inp): # returns a copy of a list
    inp_copy = inp
    return inp_copy

def small(num_or_str_list, data_type):
    if data_type == "int" or data_type == "float" or data_type == "complex":
        smallest = 0
        for i in num_list:
            if i <= smallest:
                smallest = i
        return smallest
    if data_type == "str":
       for j in num_or_str_list:
           smallest = num_or_str_list[0]
           for i in num_or_str_list:
               if ord(smallest) >= ord(i):
                   smallest = i
       return smallest

def big(num_list):
    biggest = 0
    for i in num_list:
        if i >= biggest:
            biggest = i
    return biggest

def sortlst(inp):
    while inp:
        smallest = small(inp)
    return inp


print(small("zljwqkh", "str"))
