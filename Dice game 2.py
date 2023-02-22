import random
a=int(input("Enter the number of players: "))
player=[]

y={}
z=0

while a!=0:
	b=input("player name: ")
	player.append(b)
	a-=1
	
for x in player:
	c=int(input("\n press 1 to roll the dice: "))
	a=random.randint(1,6)
	b=random.randint(1,6)
	c=a+b
	y[player[z]]=c
	print(player[z],":",a,":",b)

	z+=1
print('\n',y)