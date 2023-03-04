# python3

import sys
import threading
import numpy as np


def compute_height(n, parents):
    # Write this function
    max_height = 0
    # Your code here
    return max_height


def main():
    # implement input form keyboard and from files

    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision

    # input number of elements
    # e = input()
    e = 5

    # input values in one variable, separate with space, split these values in an array
    # v = input()
    v = "4 -1 4 1 1"
    list = []
    number = ""
    for i,j in enumerate(v):
        number = number + j
        if(j == ' '):
            list.append(int(number))
            number = ""
            continue
        if(len(v)-1 == i):
            list.append(int(number))
    print(list)

    l = []

    for i,j in enumerate(list):
        if j == -1:
            l.append(i)
    for i,j in enumerate(list):
        if j == l[0]:
            l.append(i)
    print("l: ", l)


    new_list = []
    for i,j in enumerate(l):
        if i == 0:
            continue
        print(j)
        new_list.append(list[list==j])
    print("new_list", new_list)



            
        
    
    
    # call the function and output it's result

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
# main()
# print(numpy.array([1,2,3]))