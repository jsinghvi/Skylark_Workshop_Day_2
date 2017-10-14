#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 09:49:40 2017

@author: root
"""
a = 0
b = 1
n = int(input("till when do you want the fibonacci series : "))

c = a+b
while c<=n:
    print(c)
    a=b
    b=c
    c=a+b