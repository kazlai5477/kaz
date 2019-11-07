import random

#1
def driving(a):
	if a>18:
		print(True)
	elif a<18:
		print(False)

(driving(16))
(driving(25))

#2
def id_triangle(h,o,a):
	if h**2==(a**2)+(o**2):
		print("Right-Angled Triangle")
	elif h**2>(a**2)+(o**2):
		print("Obtuse Triangle")
	elif h**2<(a**2)+(o**2):
		print("Acute Triangle")
	else:
		("Not a Triangle")

(id_triangle(3,4,5))

#3
def fizzbuzz(a):
	if a%3==0 and a%5==0:
		print("FIZZ BUZZ!")
	elif a%5==0:
		print("BUZZ")
	elif a%3==0:
		print("FIZZ")
	else:
		print("Huh?")

(fizzbuzz(15))

#4
def guess_dice(a,b,c):
	#global count, dice1, dice2, dice3
	count=0
	count2=0
	count3=0

	dice1=random.randint(1,6)
	dice2=random.randint(1,6)
	dice3=random.randint(1,6)
	
	if a==dice1:
		count=count+1
	if b==dice2:
		count=count+1
	if c==dice3:
		count=count+1
	if b==dice1:
		count2=count2+1
	if c==dice2:
		count2=count2+1
	if a==dice3:
		count2=count2+1
	if c==dice1:
		count3=count3+1
	if a==dice2:
		count3=count3+1
	if b==dice3:
		count3=count3+1

	print("Rolled:",dice1,dice2,dice3)

	if count>count2:
		print("Correct Guesses:",count)
	elif count>count3:
		print("Correct Guesses:",count)
	elif count2>count3:
		print("Correct Guesses:",count2)
	elif count2>count:
		print("Correct Guesses:",count2)
	elif count3>count2:
		print("Correct Guesses:",count3)
	elif count3>count:
		print("Correct Guesses:",count3)
	elif count==count2:
		print("Correct Guesses:",count)
	elif count==count3:
		print("Correct Guesses:",count)
	elif count2==count3:
		print("Correct Guesses:",count2)
	elif count2==count:
		print("Correct Guesses:",count2)
	elif count3==count2:
		print("Correct Guesses:",count3)
	elif count3==count:
		print("Correct Guesses:",count3)

(guess_dice(5,3,1))
(guess_dice(6,5,4))


#5
def gimme_random(a,b,c):
	num=random.uniform(b,c)
	if a=="float":
		print(float(num))
	elif a=="int":
		print(int(num))

(gimme_random("float",0.5,1.9))
(gimme_random("int",10,56))
(gimme_random("float",10,56))
(gimme_random("int",0.1,7.8))


