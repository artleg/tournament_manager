#!/usr/bin/env python3 
import sys

try :
	Main_Player=sys.argv[1]  
except IndexError:
	Main_Player=input("Введите рейтинг основного игрока: ")
Main_Player=float(Main_Player)
Rate_Sum=[]
Rival_Temp=""
yR=""
try:
	while Rival_Temp is not None:
		Rival_Temp=input("Введите рейтинг соперника: ")
		ifWin=input("Победил? ")
		Rival_Temp=float(Rival_Temp)
		if Main_Player-Rival_Temp>=100:
			Rate_Sum.append(0)
		else:
			if ifWin=="y":
				Rate_Sum.append((100-Main_Player+Rival_Temp)/10*0.1)
			else:
				Rate_Sum.append((100-Main_Player+Rival_Temp)/20*-0.1)
		
except ValueError:
	pass
i=0
New_Rate=float(Main_Player)
while i<len(Rate_Sum):
	New_Rate+=Rate_Sum[i]
	i+=1
print(Rate_Sum)
print(New_Rate)