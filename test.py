#!/usr/bin/env python3 
import sys
import os
from datetime import date

def GetListOfMembers():
	ListOfMembers=dict()
	SurnameOfMember=""
	NameOfMember=""
#	BirthDateOfMember=date()
	RateOfMember=float()
#	ListOfMembersFile=open(NameOfFile, 'a')
	try:
		while SurnameOfMember is not None:
			SurnameOfMember=str(input("Введите фамилию игрока: "))
			NameOfMember=str(input("Введите имя игрока: "))
			BirthDateOfMember=date(int(input("Введите год рождения игрока: ")),1,1)
			RateOfMember=float(input("Введите текущий рейтинг этого игрока: "))
			Player=dict(Surname=SurnameOfMember, Name=NameOfMember, BirthDate=BirthDateOfMember, Rate=RateOfMember)
			print Player.items()
			PlayerId=SurnameOfMember+NameOfMember
			if ListOfMembers.get(PlayerId) == None:
				ListOfMembers[PlayerId]=ListOfMembers.setdefault(PlayerId, Player)
				print ListOfMembers.items()
			else:
				pass
	except ValueError:
		pass
	return ListOfMembers



GetListOfMembers()
print ListOfMembers.items()