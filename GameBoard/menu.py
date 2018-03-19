#
import pygame
import time
import random

pygame.init()
display_width = 800; display_height = 600

black = (0, 0, 0);white = (255, 255, 255);red = (255, 0, 0);green = (0,255,0);blue = (0,0,250)
bright_red = (100,0,0);bright_green = (0,100,0);bright_blue = (0,0,100)

car_width = 73
# starting display
gameDisplay = pygame.display.set_mode((display_width, display_height))
fond = pygame.image.load("background1.jpg").convert()
gameDisplay.blit(fond, (0,0))
pygame.display.set_caption('Space race')
clock = pygame.time.Clock()

shipImg = pygame.image.load('ship.png')
astImg = pygame.image.load('asteroid.png')
lasImg = pygame.image.load('laser.png')
expImg = pygame.image.load('explosion.png')
shieldImg = pygame.image.load('shield.png')
#Display of asteroid counter
def asteroiDodged(count):
    font = pygame.font.SysFont(None, 40)
    text = font.render("Score: " + str(count), True, white)
    gameDisplay.blit(text, (10, 10))

#Display the asteroid
def asteroid(asteX, asteY, asteW, asteH):
    global astImg
    #pygame.draw.rect(gameDisplay, blue, [330, -600, asteW, asteH])
    astImgresized = pygame.transform.scale(astImg, (int(asteW * 1.4), int(asteH * 1.4)))
    gameDisplay.blit(astImgresized, (int((asteX - asteW * 0.2)), int((asteY - asteH * 0.2))))
def explosion(asteX, asteY, asteW, asteH):
    global expImg
    expImgresized = pygame.transform.scale(expImg, (int(asteW * 2), int(asteH * 2)))
    gameDisplay.blit(expImgresized, (int((asteX - asteW)), int((asteY - asteH))))
#Display the shoots
def shoot(array):
    for i in range(0, len(array)):
        array[i][1] -=10
        [X,Y]= array[i]
        gameDisplay.blit(lasImg,(X-16,Y-70))
#Display spaceships
def spaceship(x, y):
    gameDisplay.blit(shipImg, (x, y))

def shield(x, y):
    gameDisplay.blit(shieldImg, (x, y))

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()

def crash():
    message_display('You Crashed')

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        gameDisplay.blit(fond, (0, 0))
        largeText = pygame.font.SysFont("comicsansms", 115)
        TextSurf, TextRect = text_objects("Space race", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!", 150, 450, 100, 50, green, bright_green, game_loop)
        button("Bluetooth!", 350, 450, 100, 50, blue, bright_blue, quit)
        button("Quit", 550, 450, 100, 50, red, bright_red, quit)

        pygame.display.update()
        clock.tick(15)
gameExit = False
def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.85)

    x_change = 0
    shootsarray=[]
    asteX = random.randrange(0, display_width)
    asteY = -100
    asteSpeed = 4
    asteW = random.randrange(50, 150)
    asteH = asteW
    global gameExit
    dodged = 0
    explo = 0
    exploX = 0
    exploY = 0
    shieldisON = 0
    end=0

    while not gameExit:
        #Key entry handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -10
                if event.key == pygame.K_RIGHT:
                    x_change = 10
                if event.key == pygame.K_SPACE:
                    shootsarray.append([int(x),int(y)])
                if event.key == pygame.K_DOWN:
                    shieldisON=1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT :
                    x_change = 0
                if event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_DOWN:
                    shieldisON = 0


        x += x_change
        #Displaying everything
        gameDisplay.fill(white)
        gameDisplay.blit(fond, (0, 0))
        asteroid(asteX, asteY, asteW, asteH)
        shoot(shootsarray)
        asteY += asteSpeed
        spaceship(x, y)
        asteroiDodged(dodged)
        if shieldisON ==1:
            shield(x-14,y-15)
        if explo>0:
            explosion(exploX, exploY, exploSize, exploSize)
            explo+=1
            if explo>20:
                explo=0

        #Screen border crossing
        if x > display_width:
            x=x-display_width
        if x < 0-car_width:
            x=x+display_width
            #crash()

        if asteY > display_height:
            asteY = 0 - asteH
            asteX = random.randrange(0, display_width)
            dodged += 1
            asteSpeed += 0.5
            asteW = random.randrange(50, 150)
            asteH = asteW

        for i in range (0,len(shootsarray)):
            #print(asteX)#print(asteX + asteW)#print(asteY)#print(shootsarray[i][0])#print(shootsarray[i][1])
            if shootsarray[i][0]>(asteX-asteX*0.4) and shootsarray[i][0]<(asteX+asteW) and shootsarray[i][1] < asteY+1.5*asteH:
                #asteY+=display_height+600
                exploSize = asteH
                exploX = asteX+asteW/2
                exploY = asteY
                asteY = 0 - asteH
                asteX = random.randrange(0, display_width)
                dodged += 1
                asteSpeed += 0.5
                asteW = random.randrange(50, 150)
                asteH = asteW
                explo=1
                #exploX = shootsarray[i][0]#+asteW
                #exploY = shootsarray[i][1]-exploSize*1.2
                shootsarray[i]=[-100,-100]

                #print(exploX)
                #print(exploY)


        if y < asteY + asteH:
            #print('y crossover')
            if x > asteX and x < asteX + asteW or x + car_width > asteX and x + car_width < asteX + asteW:
                if shieldisON == 0 :
                    #print('x crossover')
                    end=1
                    print(gameExit)
                    crash()
                    gameExit=True
                    game_intro()
                if shieldisON == 1 :
                    exploSize = asteH
                    exploX = asteX + asteW / 2
                    exploY = asteY
                    asteY = 0 - asteH
                    asteX = random.randrange(0, display_width)
                    dodged += 1
                    asteSpeed += 0.5
                    asteW = random.randrange(50, 150)
                    asteH = asteW
                    explo = 1



        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()