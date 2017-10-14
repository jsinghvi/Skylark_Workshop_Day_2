#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 12:07:12 2017

@author: root
"""

def gradeCminus(grade):
    print("C minus grade!")
    return


def gradeCplus(grade):
    print("C Plus grade!")
    return


def gradeBminus(grade):
    print("B minus grade!")
    return


def gradeBplus(grade):
    print("B plus grade!")
    return


def gradeA(grade):
    print("A grade!")
    return

grade = int(input("Enter your grade : "))

if grade<=60:
    gradeCminus(grade)
elif grade>60 and grade<=70:
    gradeCplus(grade)
elif grade>70 and grade<=80:
    gradeBminus(grade)
elif grade>80 and grade<=90:
    gradeBplus(grade)
else:
    gradeA(grade)