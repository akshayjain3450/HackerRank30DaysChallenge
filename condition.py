#!/bin/python3

import math
import os
import random
import re
import sys


def printfun(num):
    if num % 2 == 1:
        print("Weird")
    elif num >= 2 and num <= 5:
        print("Not Weird")
    elif num >= 6 and num <= 20:
        print("Weird")
    else:
        print("Not Weird")

if __name__ == '__main__':
    N = int(input())
    if N >= 1 and N <= 100:
        printfun(N)
    else:
        exit()
