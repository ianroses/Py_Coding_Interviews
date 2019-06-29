#!/bin/python3

#Implement an algorithm to determine if a string has all unique characters.
#What if you cannot use additional data structures?

import itertools

if __name__ == '__main__':
    s = input()
    s = ''.join(sorted(s)) #this use extra space because sorted() return a list.
    for i,j in zip(range(len(s)), range(1,len(s))):
        if(s[i]==s[j]):
            print("Isn't Unique")
            exit()
    print("Is Unique")
