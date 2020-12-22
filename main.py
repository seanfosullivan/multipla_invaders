import pygame
import random
import math

#initiate pygame
pygame.init()

#create screen
screen = pygame.display.set_mode((800,600))
backgroundImg = pygame.image.load("spaceBackground.png")


pygame.display.set_caption("Multipla Invaders")
icon = pygame.image.load("tesla32x32.png")
pygame.display.set_icon(icon)

#Player Image
playerImg = pygame.image.load("elon64x64.png")
playerX = 370
playerY = 510
playerXchange = 0

enemyImg = []
enemyX = []
enemyY = []
enemyXchange = []
enemyYchange = []
num_of_enemies = 15
for i in range(num_of_enemies):
	enemyImg.append(pygame.image.load("multipla64x64.png"))
	enemyX.append(random.randint(0,736))
	enemyY.append(random.randint(30,80))
	enemyXchange.append(4.5)
	enemyYchange.append(40)

fireballImg = pygame.image.load("fireball.png")
fireballX = 0
fireballY = 510
fireballXchange = 0
fireballYchange = 10
fireballstate = "ready"

score_value=0
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10


over_font = pygame.font.Font('freesansbold.ttf',64)

def game_over_text():
	over_text = over_font.render("GAME OVER",True, (255,255,255))
	screen.blit(over_text, (200, 250))

def show_score(x,y):
	score = font.render("Score : " + str(score_value),True, (255,255,255))
	screen.blit(score, (x,y))

def player(x, y):
	#blit means draw
	screen.blit(playerImg, (x, y))

def enemy(x, y, i):
	#blit means draw
	screen.blit(enemyImg[i], (x, y))

def fire(x,y):
	global fireballstate
	fireballstate = "fire"
	screen.blit(fireballImg, (x+16, y+10))

def isCollision(enemyX, enemyY, fireballX, fireballY):
	distance = math.sqrt((math.pow(enemyX-fireballX,2))+ (math.pow(enemyY-fireballY,2)))
	if distance <28:
		return True
	else:
		return False  

#Game loop
running = True
while running:
	screen.fill((0,0,0))
	screen.blit(backgroundImg, (0, 0))
	#Quit check
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		#keyboard input & check
		if event.type == pygame.KEYDOWN:
			if event.key ==pygame.K_a:
				playerXchange = -5
			if event.key ==pygame.K_d:
				playerXchange = 5
			if event.key ==pygame.K_SPACE:
				if fireballstate is "ready":
					fireballX=playerX
					fire(fireballX,fireballY)
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_a or event.key == pygame.K_d:
				playerXchange = 0 

	#player under screen fill as it is drawn in order
	playerX += playerXchange

	if playerX<=0:
		playerX=0
	if playerX>=736:
		playerX=736

	for i in range(num_of_enemies):
		if enemyY[i] > 509:
			for j in range(num_of_enemies):
				enemyY[j] = 2000
			game_over_text()
			break

		enemyX[i] += enemyXchange[i]

		if enemyX[i] <= 0:
			enemyXchange[i] = 4.5
			enemyY[i] += enemyYchange[i]

		if enemyX[i] >= 736:
			enemyXchange[i] = -4.5
			enemyY[i] += enemyYchange[i]  
		
		collision = isCollision(enemyX[i], enemyY[i], fireballX, fireballY)
		if collision:
			fireballY=510
			fireballstate="ready"
			score_value+=1
			
			enemyX[i] = random.randint(0,736)
			enemyY[i] = 30
		enemy(enemyX[i],enemyY[i],i)
	if fireballstate is "fire":
		fire(fireballX,fireballY)
		fireballY-=fireballYchange
	if fireballY == 0:
		fireballY=510
		fireballstate ="ready"

	player(playerX,playerY)
	show_score(textX,textY)
	pygame.display.update()