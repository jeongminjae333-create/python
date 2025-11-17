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

#-----------이미지 로드 함수 -------
def img_load(obj):
    img = pygame.image.load("images/"+str(obj)+".png")
    img_size = img.get_rect().size#이미지의 가로 세로 길이
    return img, img_size[0],img_zise[1]
#------------------------------

bg = img_load('background')[0]
p = img_load('irinman')
r = img_load('rock02')

pad.blit(bg,(0,0))

pad.blit(p,(w/2-20,h-50))

pad.blit(r,(w/2,0))


#######################
pygame.display.update() #화면업데이트

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()





































































