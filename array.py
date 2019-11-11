#!/bin/python3

import math
import os
import random
import re
import sys

def printfun(array,length):
    for i in range(1,length+1):
        print(array[length-i],end = " ")

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    printfun(arr,n)
