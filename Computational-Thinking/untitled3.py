#Easy
def easy():
	count=0
	b=2
	a=1
	for count in range(5):
		a=b*a+count
	print(a)
easy()

#Medium
def medium():
	for i in range(1,101):
		x=i%3
		y=i%8
		if x!=0 and y!=0:
			print(i)
medium()

