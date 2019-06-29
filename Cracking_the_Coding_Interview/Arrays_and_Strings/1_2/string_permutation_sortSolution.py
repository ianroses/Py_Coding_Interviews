#!/bin/python3

#Given two strings, write a method to decide if one is a permutation of the other.

import string

if __name__ == '__main__':
    sA = input()
    sB = input()
    A = sorted(sA.translate({ord(c): None for c in string.whitespace}))
    B = sorted(sB.translate({ord(c): None for c in string.whitespace}))
    if (len(A)!= len(B)):
        print("No")
        exit()
    for i in range(len(A)):
        if A[i] != B[i]:
            print("No")
            exit()
    print("Yes")
