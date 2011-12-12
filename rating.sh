#!/usr/bin/env python3 
import sys
try :
	Player_Win=sys.argv[1]  
except IndexError:
	Player_Win=input("Введите рейтинг выигрывшего игрока: ")
try :
	Player_Lose=sys.argv[2]  
except IndexError:
	Player_Lose=input("Введите рейтинг проигравшего игрока: ")
Player_Win=float(Player_Win)
Player_Lose=float(Player_Lose)

if Player_Win-Player_Lose>=100:
	Raiting_Win=0
	Raiting_Lose=0
else:
	Raiting_Win=(100-Player_Win+Player_Lose)/10*0.1
	Raiting_Lose=-(100-Player_Win+Player_Lose)/20*0.1
print(Raiting_Win)
print(Raiting_Lose)

