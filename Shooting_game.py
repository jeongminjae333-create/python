#Shooting_game.py 배경 그림 넣기
#민재의 게임만들기
import pygame
import sys
import random
pygame.init()

######
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
pink = (255, 133, 215)
orange = (240, 155, 89)
#####


w = 480
h = 640

pad = pygame.display.set_mode((w,h)) #화면 생성
pygame.display.set_caption('Shooting Game') #제목 설정

#---------이미지 로드 함수 -----------
def img_load(obj):
    img = pygame.image.load("images/"+str(obj)+".png")
    img_size = img.get_rect().size #이미지의 가로 세로 길이
    return img, img_size[0],img_size[1]
#---------------------------------

bg = img_load("background")[0]
#------전투기 설정-------------
p,pw,ph = img_load("ironman")
px = w/2-pw/2
py =  h-ph
ps = 0 #전투기 속도
#---------------------

r,rw,rh = img_load("rock02")

pad.blit(bg,(0,0))
pad.blit(p,(px,py))
pad.blit(r,((random.randint(0,w-rw)), 20))

pygame.display.update() #화면 업데이트

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type in [pygame.KEYDOWN]:
            if event.key == pygame.K_LEFT:
                ps = -20
            elif event.key == pygame.K_RIGHT:
                ps = +20
        if event.type in [pygame.KEYUP]:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                ps = 0
            



                
    pad.blit(bg,(0,0)) #잔상제거
    px += ps
    #######전투기 화면 벗어나지 않도록
    if px< 0:
        px = 0
    elif px > w-pw:
        px = w - pw
    
    pad.blit(p,(px,py))
    pad.blit(r,(200,20))
    pygame.display.update() #화면 업데이트
    clock.tick(60)
            


























































