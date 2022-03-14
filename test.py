from termcolor import colored as cl
from random import randint as ri, choice
from time import sleep as s, perf_counter
from string import ascii_lowercase as lc, ascii_uppercase as uc, printable

def Move1Over(arr):
    last = arr[-1]
    temp = arr[0]
    for i in range(len(arr)-1):
        arr[i+1] = temp
        temp = arr[i+2]

    return arr

l = ['h','m','n','p']
print(Move1Over(l))






