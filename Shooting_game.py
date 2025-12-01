import pygame
import sys
import random
pygame.init()

######
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
yellow = (255,255,0)
blue = (0,0,255)
skyblue = (141,156,255)
######



w = 480
h = 640

pad = pygame.display.set_mode((w,h))

pygame.display.set_caption("Shooting Game") #제목


#-------ㅡ글씨 쓰기 함수-------------

def write(string,a,b,color, size = 20):
    global pad
    font = pygame.font.Font("images/NanumGothic.ttf",size)
    text = font.render(string,False,color)
    pad.blit(text,(a,b))







    

#----------이미지 로드 함수 -------------
def img_load(obj):
    img = pygame.image.load("images/"+str(obj)+".png")
    img_size = img.get_rect().size
    return img, img_size[0], img_size[1]
#-------------------------------------

bg = img_load("background")[0]
p,pw,ph = img_load("ironman")
px = w/2-pw/2
py = h-ph
ps = 0  # 전투기 스피드
#--------바위 그리기------------
rlist = ["rock01","rock02","rock03","rock04","rock05",
         "rock06","rock07","rock08","rock09","rock10"]

r,rw,rh = img_load(random.choice(rlist))
rx = random.randint(0,w-rw)
ry = random.randint(0,w-rw)
rs = 2  #바위 떨어지는 속도

def rock_init(): #바위 초기화
    global r, rw, rh, rx, ry
    r,rw,rh = img_load(random.choice(rlist))
    rx = random.randint(0,w-rw)
    ry =10


#-----미사일 그리기--------
m,mw,mh = img_load("missile")
mx = px+pw/2-mw/2
my = py- mh
mlist = []

#----------폭발 이미지 만들기--------------
exp = img_load("explosion")[0]
    
pad.blit(bg, (0,0))
pad.blit(p,(px,py))

pygame.display.update() 

clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type in [pygame.KEYDOWN]:
            if event.key == pygame.K_LEFT: #왼쪽 화살표키
                ps = -5
            elif event.key == pygame.K_RIGHT: #오른쪽 화살표키
                ps = +5
            elif event.key == pygame.K_SPACE:
                mx = px+pw/2-mw/2
                my = py - mh
                mlist.append([mx,my])
        if event.type in [pygame.KEYUP]:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                ps = 0
            


                
    px += ps
    #전투기가 화면 밖으로 나가지 않도록
    if px <0:
        px = 0
    elif px > w-pw:
        px = w-pw

    ry += rs
    pad.blit(bg,(0,0)) ###잔상 제거
    pad.blit(p,(px,py))
    pad.blit(r,(rx,ry))

    if ry > h:#바위가 화면 아래로 떨어지면
        rock_init()#새로운 바위 불러오기

    #전투기와 운석이 충돌 상황
    if (py <ry + rh) and (px < rx+rw) and (px +pw >rx):
        pad.blit(exp,(rx,ry))
        rock_init()
        
    if len(mlist) != 0: # 발사된 미사일이 있을때
        for mis in mlist:
            mis[1] -=10
            #미사일이 운석과 충돌 상황
            if (mis[1] < ry+rh) and (mis[0] < rx+rw) and (mis[0]+mw>rx):
                pad.blit(exp,(rx,ry))
                mlist.remove(mis)
                rock_init()
            
            elif mis[1] < -50:
                mlist.remove(mis)
            pad.blit(m,(mis[0],mis[1]))
    write("Scores:  ",  10, 10,white, size = 20)
    write("Miss: ", 400,10,red)

    
    pygame.display.update()
    clock.tick(60)









            
            












































































































































































