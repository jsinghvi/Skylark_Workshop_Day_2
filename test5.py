#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 11:49:04 2017

@author: root
"""

def add(a,b):
    return (a+b)

def sub(a,b):
    return (a-b)

def mult(a,b):
    return (a*b)

def div(a,b):
    return (a/b)

def mod(a,b):
    return (a%b)

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

choice = int(raw_input("1. Add \n 2. Subtract \n 3. Multiply \n 4. Divide \n 5.Mod \n Enter your choice :"))

if choice==1:
    print(add(a,b))
elif choice==2:
    print(sub(a,b))
elif choice==3:
    print(mult(a,b)) 
elif choice==4:
    print(div(a,b))
elif choice==5:
    print(mod(a,b))
else:
    print("Wrong choice!")