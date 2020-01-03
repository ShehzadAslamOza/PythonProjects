import pygame
import random
import math
import os
from pygame import mixer

os .chdir('c:/Users/Shehzad/Desktop/Alevels/PythonProjects/Space_Invaders/')

# Constants
PLAYER_SPEED = 4
ALIEN_SPEED = 6
BULLET_SPEED = 10
NUM_ALIENS = 8

pygame.init()

# Screen Setup
screen = pygame.display.set_mode((800,600))

# Background Music
mixer.music.load("background.wav")
mixer.music.play(-1)

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# Background
backImg = pygame.image.load("background.jpg")

# Player
playerImg = pygame.image.load('ship.png')
playerX = 370
playerY = 480

# Alien
alienImg = []
alienX = []
alienY = []
alien_speed = []


for i in range(NUM_ALIENS):
    alienImg.append(pygame.image.load('alien.png'))
    alienX.append(random.randint(0,764))
    alienY.append(random.randint(50,150))
    alien_speed.append(random.choice([ALIEN_SPEED, - ALIEN_SPEED, ALIEN_SPEED - 1, -ALIEN_SPEED + 1, ALIEN_SPEED - 2, -ALIEN_SPEED + 2]))
    
# Bullet
bulletImg = pygame.image.load('bullet2.png')
bulletY = 480
bulletX = 0
bulletState = 'ready'

# score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# Game Over Text
over_font = pygame.font.Font("freesansbold.ttf", 64)

# Functions
def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255,255,255))
    screen.blit(score, (x, y))
    
def player(x, y):
    screen.blit(playerImg, (x, y)) 
    
def alien(x, y, i):
    screen.blit(alienImg[i], (x, y)) 

def bullet(x, y):
    bulletX = 0
    
def fire_bullet(x, y):
    global bulletState
    global bulletX
    bulletState = 'fire'
    bulletX = x
    screen.blit(bulletImg, (bulletX + 23, y - 20))
    
def isCollision(AlienX, AlienY, BullletX, BulletY):
    distance = math.sqrt( (AlienX - BullletX)**2 + (AlienY - BulletY)**2 )
    if distance < 35:
        return True
    else:
        return False

def ship_collision(AlienX, AlienY, playerX, playerY):
    distance = math.sqrt( (AlienX - playerX)**2 + (AlienY - playerY)**2 )
    if distance < 40:
        return True
    else:
        return False

def game_over():
    over_text = over_font.render("GAME OVER", True, (255,255,255))
    screen.blit(over_text, (200,250))
    
# initilising
running = True
player_moveLeft = False
player_moveRight = False
collision = False

while running:
    # Screen Fill
    screen.fill((12,34,56))
    
    # Background Image
    screen.blit(backImg, (0,0))
    
    # Exits the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Keyboard Binding 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:  player_moveLeft  = True
            if event.key == pygame.K_RIGHT: player_moveRight = True
            if event.key == pygame.K_SPACE:
                if bulletState == 'ready':
                    bullet_sound = mixer.Sound("laser.wav")
                    bullet_sound.play()
                    fire_bullet(playerX, playerY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:  player_moveLeft  = False
            if event.key == pygame.K_RIGHT: player_moveRight = False
            
    # Border Checking
    if playerX < -63 :
        playerX = 799
    if playerX > 799:
        playerX = -63
    
        
    # Player Movement        
    if player_moveLeft: playerX -= PLAYER_SPEED
    if player_moveRight: playerX += PLAYER_SPEED   
    
    # Alien Movement
    for i in range(NUM_ALIENS):
        
        if ship_collision(alienX[i], alienY[i], playerX, playerY) or alienY[i] > 540:
            for j in range(NUM_ALIENS):
                alienY[j] = 2000
            game_over()
        
        alienX[i] += alien_speed[i]
        
        if alienX[i] >= 736:
            alien_speed[i] *= -1
            alienX[i] = 735
            alienY[i] += 40
            
        if alienX[i] <= 0:
            alienX[i] = 1
            alien_speed[i] *= -1
            alienY[i] += 40
            
        # Collision
        collision = isCollision(alienX[i], alienY[i], bulletX, bulletY)
        if collision:
            collision_sound = mixer.Sound("explosion.wav")
            collision_sound.play()
            bulletY = 480
            bulletState = 'ready'
            score_value += 1
            alienX[i] = random.randint(0,764)
            alienY[i] = random.randint(50,150)
            alien_speed[i] = random.choice([ALIEN_SPEED, - ALIEN_SPEED, ALIEN_SPEED - 1, -ALIEN_SPEED + 1, ALIEN_SPEED - 2, -ALIEN_SPEED + 2])
        
            
        alien(alienX[i], alienY[i], i)
        
    # Bullet Movement
    if bulletState == 'fire':
        bulletY -= BULLET_SPEED
        screen.blit(bulletImg, (bulletX + 23, bulletY - 20))
    
    if bulletY <= 0:
        bulletState = 'ready'
        bulletY = 480
        
    
    player(playerX, playerY)
    show_score(textX, textY)
    # Screen Update
    pygame.display.update()
       
       
