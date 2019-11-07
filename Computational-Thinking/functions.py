import math

#1
def mixed_number(x,y):
	sol=(str(x//y))+" "+(str(x%y))+"/"+str(y)
	return sol

ans=mixed_number(9,2)
print(ans)


#2
def vowel_count_1(a):
	var1=a.count("a")
	var2=a.count("e")
	var3=a.count("i")
	var4=a.count("o")
	var5=a.count("u")
	var6 = var1+var2+var3+var4+var5
	return var6

print(vowel_count_1("aeiouAEIOU"))


#3
def vowel_count_1(a):
	var1=a.count("a")
	var2=a.count("e")
	var3=a.count("i")
	var4=a.count("o")
	var5=a.count("u")
	var6 = var1, var2, var3, var4, var5
	return var6

print(vowel_count_1("aaeeiouu"))


#4
def sphere_volume(r):
	vol= 4/3*math.pi*r**3
	return vol
print(sphere_volume(10))

def sphere_surface_area(r):
	sa=4*math.pi*r**2
	return sa
print(sphere_surface_area(10))


#5
def sphere_metrics(r):
	return vol, sa
print("Sphere Volume:",sphere_volume(10),"\nSphere Surface Area:",sphere_surface_area(10))

#6

#7


	





