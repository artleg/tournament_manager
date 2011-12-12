#!/usr/bin/env python3 
import sys
STart=[]
f=open('test_data', 'r+')
STart=f.readlines()
#print(STart)
f.close()
String_Test=STart[1]
print(String_Test[-6:-1])