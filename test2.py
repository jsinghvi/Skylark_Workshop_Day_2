#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 08:42:38 2017

@author: root
""
"""
import math as m

n = int(input("Enter a number : "))
x = int(input("To the power of? ... :"))
print("The Sqrt(%d) is %r"%(n,m.sqrt(n)))

print("%d raised to the power %d is %d"%(n,x,m.pow(n,x)))