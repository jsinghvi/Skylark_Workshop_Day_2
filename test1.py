#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 08:34:02 2017

@author: root
"""
import math as m
a = float(input("Enter number 1 : "))
b = float(input("Enter number 2 : "))
c = float(input("Enter number 3 : "))
d = float(input("Enter number 4 : "))
e = float(input("Enter number 5 : "))

choice = int(input("1. Min \n 2. Max \n Your choice : "))

if choice==1:
    print(min(a,b,c,d,e))
else:
    print(max(a,b,c,d,e))