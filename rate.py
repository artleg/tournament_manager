#!/usr/bin/env python3 
import sys
from datetime import date
import string

def AgeCategoryDefine():
	AgeCategory=input("Какая это возрастная категория? (введидте «1» если 2000 и младше, введите «2» если 1993 и младше) ")
	if AgeCategory=="1":
		NameAgeCategory="2000"
	else:
		NameAgeCategory="1993"
	return NameAgeCategory

Date_Today=date.today()
NameAgeCategory=AgeCategoryDefine()
NameOfFile="/tmp/sunday_league_"+str(Date_Today.strftime("%d.%m.%Y"))+"_"+NameAgeCategory

def GetListOfMembers():
	ListOfMembers=[]
	MemberOfTour=""
	RateOfMember=float()
	try:
		while MemberOfTour is not None:
			MemberOfTour=str(input("Введите фамилию, имя и год рождения игрока, принимавшего участие в туре: "))
			RateOfMember=float(input("Введите текущий рейтинг этого игрока: "))
			ListOfMembers.append(MemberOfTour)
			ListOfMembers.append(RateOfMember)
	except ValueError:
		pass
	return ListOfMembers

def MakeFileOfMembers():
	ListOfMembers=GetListOfMembers()
	NameOfFile="/tmp/sunday_league_"+str(Date_Today.strftime("%d.%m.%Y"))+"_"+NameAgeCategory
	ListOfMembersFile=open(NameOfFile, 'a')
	i=0
	while i<len(ListOfMembers):
		Temp=str(ListOfMembers[i])
		ListOfMembersFile.write(Temp+" "+"\n")
		i+=1
	ListOfMembersFile.close()
	return ListOfMembers

try:
	ListOfMembersFile=open(NameOfFile, 'r')
	ArrayLines=ListOfMembersFile.readlines()
	ListOfMembersFile.close()
	i=0
	k=i+1
	Name=[]
	Rate=[]
	while i<len(ArrayLines):
		Temp1=str(ArrayLines[i])
		Temp1=Temp1.strip("\t\n")
		Temp2=float(ArrayLines[k])
		Name.append(Temp1)
		Rate.append(Temp2)
		i+=1
except IOError:
	MakeFileOfMembers()


i=0
k=1
Name=[]
Rate=[]
ListOfMembers=[]
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
yR=""
try:
	while RivalTemp is not None:
		RivalTemp=PlayerChoose("соперника")
		ifWin=input("Победил? ")
		if MainPlayerRate-RivalTemp>=100:
			RateSum.append(0)
		else:
			if ifWin=="y" or ifWin=="n":
				if ifWin=="" or ifWin=="y":
					RateSum.append((100-MainPlayerRate+RivalTemp)/10*0.1)
				else:
					RateSum.append((100+MainPlayerRate-RivalTemp)/20*-0.1)
			else:
				print("Ошибка значение может быть только y/n, введите игрока заново")
				continue
except ValueError:
	pass
i=0
NewRate=float(MainPlayerRate)
while i<len(RateSum):
	NewRate+=RateSum[i]
	i+=1
NewRate=NewRate+float(input("Введидте количество бонусных очков: "))
print(NewRate)
PAth="/home/artleg/Dropbox/backup/table_tennis/sunday_league/"+str(Date_Today.strftime("%d.%m.%Y")+"_"+NameAgeCategory)
Resalt=open(PAth, 'a')
Resalt.write(NameMainPlayer+" "+"\n")
Resalt.write(str(round(NewRate, 2))+"\n")
Resalt.close()