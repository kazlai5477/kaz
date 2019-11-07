import random
#1
def both():
	for i in range(8,-4,-1):
		print(i)
	a=9
	while a>=-2:
		print(a-1)
		a-=1
both()

#2
def is_odd(a):
	if a%2==1:
		return True
	else:
		return False

for i in range(1,11):
	is_odd(i)
	if is_odd(i)==True:
		print("odd")
	else:
		print("even")

#3
def dice_roll(a):
    alldice = 0
    count = 0
    while alldice != a:
        count += 1
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        dice3 = random.randint(1,6)
        alldice = dice1 + dice2 + dice3
    print(count)
dice_roll(17)
dice_roll(13)

#4
def odd_even_count(a):
	odd=0
	even=0
	while a>0:
		b=a%10
		if b%2==0:
			even+=1
		else:
			odd+=1
		a=int(a/10)
	print("odds:",odd,"evens:",even)
odd_even_count(789319231)
odd_even_count(987654)

#5
def string_analysis(a):
	digits = sum(i.isdigit() for i in a)
	letters = sum(i.isalpha() for i in a)
	blanks = sum(i.isspace() for i in a)
	print("Letters:",letters,", Digits:",digits,", Blanks:",blanks)
string_analysis("I'm not 89 years old")

