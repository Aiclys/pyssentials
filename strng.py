#!/usr/bin/env python3

up_alphabet = {
    "a" : "A",
    "b" : "B",
    "c" : "C",
    "d" : "D",
    "e" : "E",
    "f" : "F",
    "g" : "G",
    "h" : "H",
    "i" : "I",
    "j" : "J",
    "k" : "K",
    "l" : "L",
    "m" : "M",
    "n" : "N",
    "o" : "O",
    "p" : "P",
    "q" : "Q",
    "r" : "R",
    "s" : "S",
    "t" : "T",
    "u" : "U",
    "v" : "V",
    "w" : "W",
    "x" : "X",
    "y" : "Y",
    "z" : "Z"
}
low_alphabet = {
    "A" : "a",
    "B" : "b",
    "C" : "c",
    "D" : "d",
    "E" : "e",
    "F" : "f",
    "G" : "g",
    "H" : "h",
    "I" : "i",
    "J" : "j",
    "K" : "k",
    "L" : "l",
    "M" : "m",
    "N" : "n",
    "O" : "o",
    "P" : "p",
    "Q" : "q",
    "R" : "r",
    "S" : "s",
    "T" : "t",
    "U" : "u",
    "V" : "v",
    "W" : "w",
    "X" : "x",
    "Y" : "y",
    "Z" : "z"
}

all_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", \
           "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", \
           "V", "W", "X", "Y", "Z"]
low_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", \
           "y", "z"]
up_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", \
           "V", "W", "X", "Y", "Z"]
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
punctuation = ["!", "/", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".",\
               "/", ":", ";", "<", "=", ">", "?", "@", "[", "/", "]", "^", "_", "`", "{", "|", "}", "~"]


def concat(a, b): # concatenates 2 strings
    return str(a) + str(b)

def strpos(a, b): # postition of a in b if it is in b
    if isin(a, b) == True:
        e = 0
        for i in b:
            e += 1
            if a == i:
               return e - 1
    else:
        return None

def stratpos(strlist, i): # gets a string at postion b in the string strlist
    return strlist[i]

def length(a): # self explanatory
    strlen = 0
    for i in str(a):
        strlen += 1
    return strlen

def binval(a): # binary value of an integer a
    bin_a = f'{a:08b}'
    return bin_a

def isin(a, strlist): # checks if a is in strlist
    if a in strlist:
        return True
    elif a not in strlist:
        return False

def slice(strlist, a, b): # slices strlist from index a to b
    return strlist[a:b]

def allup(strlist): # turns all letters from strlist in their capitalized equivalent
    e = 0
    up_alph = up_alphabet
    new_strlist = strlist
    for letter in strlist:
        try:
            if letter in up_alph:
                new_strlist = new_strlist.replace(letter, up_alph[letter])
                e += 1
        except:
            return None
    if e > 0:
        return new_strlist

def alllow(strlist): # does the opposite of allup()
    e = 0
    low_alph = low_alphabet
    new_strlist = strlist
    for letter in strlist:
        try:
            if letter in low_alph:
                new_strlist = new_strlist.replace(letter, low_alph[letter])
                e += 1
        except:
            return None

    if e > 0:
        return new_strlist

def rev(inp): # reverses inp wether it be a list or string or an other data type
    return inp[::-1]

def cap(strlist): # capitalizes the first letter of strlist
    up_alph = up_alphabet
    new_strlist = strlist
    first_letter = new_strlist[0]
    try:
        new_strlist = new_strlist[0].replace(first_letter, up_alph[first_letter]) + new_strlist[1::]
    except:
        return "The string is already capitalized"
    return new_strlist

