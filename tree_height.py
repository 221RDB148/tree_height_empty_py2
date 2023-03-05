# python3
#221RDB148 Valters Mārtinsons
import sys
import threading
import numpy as np


def compute_height(a,list,l,ss):
    def func(a):
        if (a in list):
            for i,j in enumerate(list):
                if j==a:
                    l.append(i)

                    func(i)
                    
                    height = len(l) + 2
                    if (height > ss[-1]):
                        ss.append(height)

        if(not len(l)==0):
            l.pop()
    
    func(a)
    print(ss[-1])
    # return ss[-1]



def main():
# implement input form keyboard and from files
    
# let user input file name to use, don't allow file names with letter a
# account for github input inprecision
    # i = input()
    inp = "I"

# input number of elements
    e = 5
    e = input()
    # e = input()
    # e = 5

# input values in one variable, separate with space, split these values in an array
    # v = input()
    # v = input()
    v = "4 -1 4 1 1"
    list = []
    
   
# makes list from input
    number = ""
    for i,j in enumerate(v):
        number = number + j
        if(j == ' '):
            list.append(int(number))
            number = ""
            continue
        if(len(v)-1 == i):
            list.append(int(number))

# finds first value
    for i,j in enumerate(list):
        if j == -1:
            a = i

    l = []
    ss = [0]

    compute_height(a,list,l,ss)

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()

main()