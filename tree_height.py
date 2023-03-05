# python3
#221RDB148 Valters Mārtinsons
import sys
import threading
import numpy as np


def compute_height(n1,list,l,ss):
    def func(n1):
        if n1 in list:
            for i,j in enumerate(list):
                if j==n1:
                    l.append(i)
                    func(i)
                    height = len(l) + 2
                    if height > ss[-1]:
                        ss.append(height)
        if not len(l)==0:
            l.pop()
    func(n1)
    print(ss[-1])
    # return ss[-1]



def main():
    # implement input form keyboard and from files  
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    # input number of elements
    # i = input()
    inp = input()
    if inp[0] == "I":
        e = input()
        if int(e) > 105 or int(e) < 1:
            return
        v = input()
        # v = "4 -1 4 1 1"
        list = []
        # 
        # makes list from input
        number = ""
        for i,j in enumerate(v):
            number = number + j
            if j == ' ':
                list.append(int(number))
                number = ""
                continue
            if len(v)-1 == i:
                list.append(int(number))

        # finds root value
        n = 0
        for i,j in enumerate(list):
            if j == -1:
                n = i

        l = []
        ss = [0]
        compute_height(n,list,l,ss)

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()

main()