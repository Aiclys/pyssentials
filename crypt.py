#!/usr/bin/env python3
import strng
import rand
import ma

def caesar(message_to_encrypt, shift):
    encrypted_message = ""
    for i in strng.alllow(message_to_encrypt):
        try:
            j = (strng.strpos(i, strng.low_letters) + shift) % 26
            encrypted_message += strng.low_letters[j]
        except:
            encrypted_message += i
    return encrypted_message

def decrypt_caesar(message_to_decrypt, shift):
    decrypted_message = ""
    for i in message_to_decrypt:
        try:
            j = (strng.strpos(i, strng.low_letters) - shift) % 26
            decrypted_message += strng.low_letters[j]
        except:
            decrypted_message += i
    return decrypted_message

def diffie_hellman(p, b, x, y):
    key_one = x
    key_two = y
    res_one = b**x % p
    res_two = b**y % p
    common_key = res_two**x % p
    return key

def rev_ciph(message_to_encrypt):
    encrypted_message = ""
    e = strng.length(message_to_encrypt) - 1
    while e >= 0:
        encrypted_message = encrypted_message + message_to_encrypt[e]
        e = e - 1
    return encrypted_message

def korealis(text, password, mode):
    if mode == "encrypt":
        text += password
        return text

print(rand.randprime(1, 100))
