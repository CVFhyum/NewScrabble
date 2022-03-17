from termcolor import colored as cl
from random import randint as ri, choice
from time import sleep as s, perf_counter
from string import ascii_lowercase as lc, ascii_uppercase as uc, printable

curword = "HELLOLOL"
letters = [x for x in "HELLO"]

def LettersCheck():
    curwordL = [char for char in curword]
    letterscopy = letters.copy()
    for i in [char for char in curword]:
        if i in letterscopy:
            curwordL.remove(i)
            letterscopy.remove(i)
        else:
            return False
    return True

print(LettersCheck())






