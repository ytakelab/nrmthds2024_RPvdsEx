# -*- coding: utf-8 -*-
"""
template_mainFuc.py
normal script with direct main function
Copyright (C) 2020 Yuichi Takeuchi
"""

# import libraries
'''
import numpy as np
import matplotlib as mpl
'''
a = 1
b = 2

# define functions and classes #########
def myfunc_a(x, y):
    '''
    Docstring for this function
    '''
    return x + y


def myfunc_b(x, y):
    '''
    Docstring for this function
    '''
    return x - y


def main():
    '''
    Docstring for this function
    '''
    x, y = 3, 5
    mainFunc_out1 = myfunc_a(x, y)
    mainFunc_out2 = myfunc_b(x, y)
    print(mainFunc_out1, mainFunc_out2)
    return mainFunc_out1, mainFunc_out2


# main procedure when called
if __name__ == '__main__':
    main()
    c = 3
    d = 4
