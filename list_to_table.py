#!/usr/bin/env python3 
import sys
import string
fileName=input("Введите путь до файла: ")
f=open(fileName)
list_M=f.readlines()
f.close()
i=0
k=i+1
print(list_M[i])
Name=[]
Rate=[]
while i<len(list_M)  :
	Temp1=str(list_M[i])
	Temp1=Temp1.strip("\t\n")
	Name.append(Temp1)
	Temp2=float(list_M[k])
	Rate.append(Temp2)
	i+=2
	k+=2
i=0
tableResalt=["<table><tbody>"]
Temp=str()
while i<len(Name):
	Temp="<tr><td>"+str(Name[i]) +"</td><td>"+str(Rate[i])+"</td></tr>"
	tableResalt.append(Temp)
	i+=1
#print(Name) 
#print(Rate)
tableResalt.append("</tbody></table>")
f=open('/home/artleg/Dropbox/backup/table_tennis/sunday_league/Table_Resalt', 'w')
i=0
while i<len(tableResalt):
	f.write(tableResalt[i])
	i+=1
f.close()
print(tableResalt)