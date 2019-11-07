# 1
import pygame
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
running = True
r = 0
g = 0
b = 0
x=1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))
    pygame.draw.circle(screen, (0,g,0), (320, 240), 50)
    pygame.display.update()

    g+=x
    if g>=255 or g<=0:
    	x=x*-1
    clock.tick(200)
pygame.quit()

#2
import pygame
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
a=10
c=20
d=30
e=40
r=50
aa=1
cc=1
dd=1
ee=1
rr=0

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	screen.fill((0,0,0))
	pygame.draw.circle(screen, (255, 255, 255), (100, 240), a)
	pygame.draw.circle(screen, (200, 200, 200), (210, 240), c)
	pygame.draw.circle(screen, (155, 155, 155), (320, 240), d)
	pygame.draw.circle(screen, (100, 100, 100), (430, 240), e)
	pygame.draw.circle(screen, (55, 55, 55), (540, 240), r)
	pygame.display.update()
	
	a+=aa
	if a==50:
		aa=aa*-1
	if a==2:
		aa=1
	
	c+=cc
	if c==50:
		cc=cc*-1 
	if c==2:
		cc=1

	d+=dd
	if d==50:
		dd=dd*-1 
	if d==2:
		dd=1

	e+=ee
	if e==50:
		ee=ee*-1 
	if e==2:
		ee=1
	
	r+=rr
	if r==50:
		rr=-1 
	if r==2:
		rr=1

	clock.tick(60)
pygame.quit()

#3
import pygame
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
a = 0
b = 150
c = 100
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))
    pygame.draw.circle(screen, (a%250,b%250,c%250), (640, 360), 300)
    pygame.draw.circle(screen, (a%1,b%250,c%1), (640, 360), 290)
    pygame.draw.circle(screen, (a%20,b%30,c%250), (640, 360), 280)
    pygame.draw.circle(screen, (a%230,b%220,c%220), (640, 360), 270)
    pygame.draw.circle(screen, (a%21,b%10,c%210), (640, 360), 260)
    pygame.draw.circle(screen, (a%20,b%200,c%200), (640, 360), 250)
    pygame.draw.circle(screen, (a%190,b%190,c%190), (640, 360), 240)
    pygame.draw.circle(screen, (a%180,b%80,c%180), (640, 360), 230)
    pygame.draw.circle(screen, (a%170,b%160,c%150), (640, 360), 220)
    pygame.draw.circle(screen, (a%20,b%10,c%230), (640, 360), 210)
    pygame.draw.circle(screen, (a%240,b%24,c%240), (640, 360), 200)
    pygame.draw.circle(screen, (a%220,b%203,c%40), (640, 360), 190)
    pygame.draw.circle(screen, (a%240,b%20,c%40), (640, 360), 180)
    pygame.draw.circle(screen, (a%20,b%20,c%240), (640, 360), 170)
    pygame.draw.circle(screen, (a%24,b%243,c%20), (640, 360), 160)
    pygame.draw.circle(screen, (a%20,b%230,c%40), (640, 360), 150)
    pygame.draw.circle(screen, (a%203,b%30,c%40), (640, 360), 140)
    pygame.draw.circle(screen, (a%20,b%240,c%240), (640, 360), 130)
    pygame.draw.circle(screen, (a%22,b%123,c%231), (640, 360), 120)
    pygame.draw.circle(screen, (a%22,b%40,c%220), (640, 360), 110)
    pygame.draw.circle(screen, (a%40,b%30,c%123), (640, 360), 100)
    pygame.draw.circle(screen, (a%24,b%40,c%240), (640, 360), 90)
    pygame.draw.circle(screen, (a%231,b%20,c%240), (640, 360), 80)
    pygame.draw.circle(screen, (a%123,b%10,c%240), (640, 360), 70)
    pygame.draw.circle(screen, (a%20,b%240,c%240), (640, 360), 60)
    pygame.draw.circle(screen, (a%121,b%123,c%40), (640, 360), 50)
    pygame.draw.circle(screen, (a%255,b%23,c%2), (640, 360), 40)
    pygame.draw.circle(screen, (a%40,b%210,c%40), (640, 360), 30)
    pygame.draw.circle(screen, (a%2,b%2,c%220), (640, 360), 20)
    pygame.draw.circle(screen, (a%1,b%200,c%64), (640, 360), 10)
    pygame.display.update()
    a=a+10
    b=b+10
    c=c+10
    clock.tick(30)
pygame.quit()

#4
import pygame, random, math

screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

a=random.randint(0,640)
b=random.randint(0,480)

running = True
screen.fill((0,0,0))
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	
	x=random.randint(1,639)
	y=random.randint(1,479)
	
	pygame.draw.circle(screen, (255, 255, 255), (a, b), 3)
	pygame.draw.line(screen, (255, 255, 255), (a, b), (x, y), 1)
	a=x
	b=y
	pygame.draw.circle(screen, (255, 255, 255), (a, b), 3)

	clock.tick(3)
	pygame.display.flip()
pygame.quit()

