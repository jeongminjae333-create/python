#Shooting_game.py 배경 그림 넣기
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



#####배경화면 넣기####
bg =pygame.image.load("images/background2.jpg")#상대적
pad.blit(bg,(0,0))
p = pygame.image.load("images/ironman.png")
px = w/2 - 45/2
py = h * 0.9
pad.blit(p,( px,py))

#######################
pygame.display.update() #화면업데이트

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()





































































