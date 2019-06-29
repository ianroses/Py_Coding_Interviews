#!/bin/python3

#Implement an algorithm to determine if a string has all unique characters.
#What if you cannot use additional data structures?

if __name__ == '__main__':
    s = input()
    a = set(s) #Use of an addtional data structure
    if len(s) != len(a):
        print("Isn't Unique")
        exit()
    print("Is Unique")
