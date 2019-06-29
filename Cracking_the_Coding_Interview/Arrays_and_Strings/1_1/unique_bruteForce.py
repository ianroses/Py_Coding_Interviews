#!/bin/python3

#Implement an algorithm to determine if a string has all unique characters.
#What if you cannot use additional data structures?

#This solution doesnt use any addtional data structure but it's not optimal in speed.
if __name__ == '__main__':
    s = input()
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i] == s[j]:
                print("Isn't Unique")
                exit()
    print("Is Unique")
