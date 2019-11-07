#Easy
def easy():
	count = 0
	while count < 10:
		count = count+1
	print(count*10)
easy()

#Medium
def medium():
	count = 0
	while count < 5.3:
		count = count+0.2
	print(count)
medium()

#Hard
def hard():
	count = 0
	prime_count = 0
	while prime_count < 10:
		num=str(count)
		is_prime=True
		for digit in num:
			if digit is ["0","1","4","6","8","9"]:
				is_prime=False
hard()







