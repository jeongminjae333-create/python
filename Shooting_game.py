#Shooting_game.py
import pygame
import sys
pygame.init()

#####
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
yellow = (255,255,0)
blue = (0,0,255)
pink = (255,133,215)
orange = (240,155,89)
#####


w = 480
h = 640

pad = pygame.display.set_mode((w,h)) #화면생성
pygame.display.set_caption("민재의 슈팅게임") #제목 설정

pad.fill((pink))




#pygame.draw.line(pad,red,(240,0),(240,h),5)        #선그리기
#pygame.draw.line(pad,red,(0,210),(480,210),5)    #선그리기
pygame.draw.circle(pad,blue, (100,100),50,0)      #원그리기
pygame.draw.circle(pad,blue, (360,100),50,0)      #원그리기
pygame.draw.rect(pad, black, (70,400,340,200)) #사각형그리기
pygame.draw.polygon(pad,orange,( (320,300),(160,300),(240,210)))
pygame.draw.ellipse(pad,yellow,(300,300,100,50),0)
pygame.draw.ellipse(pad,yellow,(0,300,100,50),0)
pygame.display.update() #화면업데이트

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()





































































