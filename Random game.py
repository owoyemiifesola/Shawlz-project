import random
a=random.randint(1,31)
b=1
while b<=5:
	c=int(input("Choose a number: "))
	if c==a:
		print("You guessed right in ", b,'Trials')
		break
	elif b==5 and c!=a:
		print("Try again")
	elif c>a:
		print("Your guess is high,guess lower")
	elif c<a:
		print("Your guess is low,guess higher")
	else:
		print("please guess between 1and 30")
	b +=1

