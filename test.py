from termcolor import colored as cl
from random import randint as ri, choice
from time import sleep as s, perf_counter
from string import ascii_lowercase as lc, ascii_uppercase as uc, printable


class MyClass:
    def __init__(self,name,value):
        self.name = name
        self.value = value
        self.constant = 3.14

    def __str__(self):
        return f"{self.name} - {self.value} - {self.constant}"

l = [MyClass("Yuval", x) for x in range(10)]
dic = {x.value: x for x in l}
keys = dic.keys()
vals = dic.values()

for k, v in zip(keys,vals):
    print(f"{k=} | {v=}")






