

import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False
#Nosaukums logam un ikona tam
pygame.display.set_caption("Kovidnieks")
icon = pygame.image.load("skull.png")
pygame.display.set_icon(icon)

#Speeleetaja varonis charecter
playerImg = pygame.image.load("mask.png")
playerX = 370
playerY = 480
playerX_change = 0

#Pretinieks ienaidnieks...
enemyImg = pygame.image.load("coronavirus (1).png")
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemyX_change = 0.3
enemyY_change = 40

#Lode shausana
#ready ir lai neredzeetu lodi pirms izshausanas
#fire lai lode kusteetos
bulletImg = pygame.image.load("syringe (1).png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 1
bullet_state = "ready"

def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def player(x, y):
    screen.blit(playerImg, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16, y+10))

done = True
while done:
    screen.fill((250, 250, 250))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
    #pygame.display.flip()
    #Ekrana aizpildishanai RGB: krasas
        #screen.fill((250, 250, 250))



    #Kontroles: ja poga ir piespiesta kustiiba pa labi un pa kreisi : KEYDOWN(Nospiestaa poga)
        if event.type == pygame.KEYDOWN:
            print("Poga nospiesta")
            if event.key == pygame.K_LEFT:
                #print("Kreisaa poga ir nospiesta")
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                #print("Labaa poga ir nospiesta")
                playerX_change = 0.3

            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                # Noskaidro speleetaja atrashanaas vietu
                bulletX = playerX
                fire_bullet(playerX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or  event.key == pygame.K_RIGHT:
                #print("Poga ir atlaista")
                playerX_change = 0
    # 5 = 5 + -0.1 -> 5 = 5 - 0.1
    # 5 = 5 + 0.1
    playerX += playerX_change
    #Lai neiziet arpus ekrraana robezas
    if playerX <=0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    enemyX += enemyX_change
    # Pretinieks : Lai neiziet arpus ekrraana robezas
    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = - 0.3
        enemyY += enemyY_change

    #Lodes kustiiba papildus nosaciijumi lai var vairaakas lodes izsaukt bullet =480 un bullet_state = "ready"
    if bulletY <= 0 :
        bulletY = 480
        bullet_state = "ready"


    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)

    enemy(enemyX, enemyY)

    pygame.display.update()
