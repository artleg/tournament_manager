#!/usr/bin/env python3 
import sys

f=open('list_of_m')
list_m=f.readlines()
f.close()
i=0
k=i+1
print(list_m[i])
Name=[]
Rate=[]
while i<len(list_m)  :
	Temp1=str(list_m[i])
	Name.append(Temp1)
	Temp2=float(list_m[k])
	Rate.append(Temp2)
	i+=2
	k+=2
Temp=0
Uids=[]
Uid=[]
for x in Name:
	Temp+=1
	Temp1=str(Uid)
	Temp="Uid_"+Temp1
	
	Uid.append(x)
	Uids.append(Uid)
print(Name)
#print(Rate)
print(Uids)