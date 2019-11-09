#!/bin/python3

import math
import os
import random
import re
import sys

def printfun(num):
    res = 0
    for i in range(1,11):
        res = num * i
        print("{} x {} = {}".format(num,i,res))

if __name__ == '__main__':
    n = int(input())
    printfun(n)
