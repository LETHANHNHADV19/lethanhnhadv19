# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 15:36:41 2021

@author: LENOVO
"""
def check_prime_number(n):
    flag = True;
    if (n <2):
        flag = False
        return flag  
    
    for p in range(2, n):
        if n % p == 0:
            flag = False
            break
    return flag

def cau1a(arr):
    count = 0
    for i in arr:
        if check_prime_number(i):
            count = count + 1
    if count >= 2:
        return True
    return False
