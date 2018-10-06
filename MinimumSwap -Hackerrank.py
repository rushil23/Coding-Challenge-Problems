#!/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.

def minIndex(arr,start):
    minn = math.pow(10,5)
    min_i = 0
    for i in range(start,len(arr)):
        if (arr[i]<minn):
            min_i=i
            minn = arr[i]
    return min_i
        


def minimumSwaps(arr):
    swaps=0
    start=0
    for i in range(len(arr)-1):
        min_i=minIndex(arr,start)
        if min_i!=i:
            #Swap
            arr[i],arr[min_i]=arr[min_i],arr[i]
            swaps+=1
        start+=1
        
    return swaps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()

