#!/bin/python3

import math
import os
import random
import re
import sys

def printfunc(num):
    string = ''
    temp = num
    while temp != 0:
        rem = temp % 2
        temp = int(temp/2)
        string = string + str(rem)
        #print(string)
    string = string[::-1]
    #print(string)
    count = 0
    string_list = list(string)
    res = 0
    for item in string_list:
        if item is '0':
            count = 0
        else:
            count += 1
            res = max(res,count)
    print(res)

if __name__ == '__main__':
    n = int(input())
    printfunc(n)
