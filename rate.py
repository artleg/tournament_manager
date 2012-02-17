#!/usr/bin/env python3 
import sys
from datetime import date
import string
import os

def AgeCategoryDefine():
	AgeCategory=input("Какая это возрастная категория? (введидте «1» если 2000 и младше, введите «2» если 1994 и младше) ")
	if AgeCategory=="1":
		NameAgeCategory="2000"
	else:
		NameAgeCategory="1994"
	return NameAgeCategory

def GetListOfMembers():
	ListOfMembers=[]
	MemberOfTour=""
	RateOfMember=float()
	ListOfMembersFile=open(NameOfFile, 'a')
	try:
		while MemberOfTour is not None:
			MemberOfTour=str(input("Введите фамилию, имя и год рождения игрока, принимавшего участие в туре: "))
			RateOfMember=float(input("Введите текущий рейтинг этого игрока: "))
			ListOfMembers.append(MemberOfTour)
			ListOfMembersFile.write(MemberOfTour+" "+"\n")
			ListOfMembers.append(RateOfMember)
			ListOfMembersFile.write(str(RateOfMember)+" "+"\n")
	except ValueError:
		pass
	return ListOfMembers


Date_Today=date.today()
NameAgeCategory=AgeCategoryDefine()
NameOfFile="/tmp/sunday_league_"+str(Date_Today.strftime("%d.%m.%Y"))+"_"+NameAgeCategory

try:
	os.path.exists(NameOfFile)
	print(NameOfFile)
	ListOfMembersFile=open(NameOfFile, 'r')
	ArrayLines=ListOfMembersFile.readlines()
	ListOfMembersFile.close()
	i=0
	k=1
	Name=[]
	Rate=[]
	while i<len(ArrayLines):
		Temp1=str(ArrayLines[i])
		Temp1=Temp1.strip("\t\n")
		Name.append(Temp1)
		Temp2=float(ArrayLines[k])
		#Temp2=Temp2.strip("\t\n")
		#Temp2=float(Temp2)
		Rate.append(Temp2)
		i+=2
		k+=2
except IOError:
	ListOfMembers=GetListOfMembers()
	i=0
	k=1
	Name=[]
	Rate=[]
	while i<len(ListOfMembers)  :
		Temp1=str(ListOfMembers[i])
	#	Temp1=Temp1.strip("\t\n")
		Name.append(Temp1)
		Temp2=float(ListOfMembers[k])
		Rate.append(Temp2)
		i+=2
		k+=2
			
print(Name)
print(Rate)
def PlayerChoose(TypePlayer):
	i=0
	while i<len(Name):
		TempPlayer=str(i+1)+" "+Name[i]
		print(TempPlayer)
		i+=1 
	TempMsg="Выбирете "+TypePlayer+" (цифрой): "
	MemberChoise=int(input(TempMsg))-1
	return MemberChoise
PlayerIndex=PlayerChoose("основного игрока")
NameMainPlayer=Name[PlayerIndex]
MainPlayerRate=Rate[PlayerIndex]
RateSum=[]
RivalTemp=float()
try:
	while RivalTemp is not None:
		RivalTemp=Rate[PlayerChoose("соперника")]
		ifWin=input("Победил? ")
		if ifWin in ("y","n",""):
			if (ifWin=="y") or (ifWin==""):
				if (MainPlayerRate-RivalTemp<100):
					print("MainPlayerRate", MainPlayerRate)
					print("RivalTemp", RivalTemp)
					TEst=(100-MainPlayerRate+RivalTemp)/100
					RateSum.append(TEst)
				else:
					RateSum.append(0)
			else:
				if (RivalTemp-MainPlayerRate<100):
					print("MainPlayerRate", MainPlayerRate)
					print("RivalTemp", RivalTemp)
					RateSum.append(((100-RivalTemp+MainPlayerRate)/-200))
				else:
					RateSum.append(0)
		else:
			print("Ошибка значение может быть только y/n, введите игрока заново")
			continue
except ValueError:
	pass
i=0
print("MainPlayerRate:", MainPlayerRate)
print(RateSum)
NewRate=float(MainPlayerRate)
while i<len(RateSum):
	NewRate=NewRate+RateSum[i]
	print("NewRate  в цикле", NewRate)
	i+=1
NewRate=NewRate+float(input("Введидте количество бонусных очков: "))
print("NewRate", NewRate)
PAth="/home/artleg/Dropbox/backup/table_tennis/sunday_league/"+str(Date_Today.strftime("%d.%m.%Y")+"_"+NameAgeCategory)
Resalt=open(PAth, 'a')
Resalt.write(NameMainPlayer+" "+"\n")
Resalt.write(str(round(NewRate, 2))+"\n")
Resalt.close()