#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv

def enc(m, k):
    mb = ''.join(format(ord(i), '08b') for i in m)
    kb = ''.join(format(ord(i), '08b') for i in k)
    c = ''.join('0' if mb[i] == kb[i] else '1' for i in range(len(mb)))
    return f"Key: {kb}\nCipher: {c}"

def dec(c, k):
    m = ''.join('0' if c[i] == k[i] else '1' for i in range(len(c)))
    return ''.join(chr(int(m[i*8:i*8+8],2)) for i in range(len(m)//8))

if __name__ == "__main__":
    match argv[1]:
        case "enc":
            print(enc(argv[2], argv[3]))
        case "dec":
            print(dec(argv[2], argv[3]))
