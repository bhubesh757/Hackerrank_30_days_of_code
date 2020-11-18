#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the triplets function below.
def triplets(a, b, c):
    a=  sorted(set(a))
    b=  sorted(set(b))
    c=  sorted(set(c))
    
    count = m = n = 0
    
    # loop the value
    
    for value in b:
        while m < len(a) and a[m] <= value :
            m = m+1
        while n < len(c) and c[n] <= value:
            n = n+1
        count = count + m*n
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()
