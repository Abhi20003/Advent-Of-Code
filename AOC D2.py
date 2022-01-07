# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 13:13:21 2021

@author: 91971
"""


f1=r"C:\Users\91971\OneDrive\Desktop\AOC\Inputs\input_D2.txt"

file=open(f1,'r')
h_pos=0
depth=0
aim=0
lines=file.readlines()
for i in lines:
    if i[0]=='f':
        for j in i:
            if j.isdigit():
                a=int(j)
        h_pos+=a
        depth+=aim*a
    elif i[0]=='d':
        for k in i:
            if k.isdigit():
                a=int(k)
        aim+=a
    else:
        for l in i:
            if l.isdigit():
                a=int(l)
        aim-=a
print(h_pos*depth)
