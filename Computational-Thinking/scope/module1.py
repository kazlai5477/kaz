import math

var1=10
def name(f,l):
	fullname=("Hello,")+(str(f))+(str(l))
	return fullname

print(name(" Kaz", " Lai"))


def sphere_volume(r):
	vol= 4/3*math.pi*(pow(r,3))
	return vol
print(sphere_volume(10))

def sphere_surface_area(r):
	sa=4*math.pi*(pow(r,2))
	return sa
print(sphere_surface_area(10))