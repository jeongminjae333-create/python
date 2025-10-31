#turtle_Lotto.py 로또 번호 생성기

import turtle as t
import random
#통에 공을 넣는다(1~45)
'''
lotto_num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
                     21,22,23,23,24,25,26,27,28,29,30,31,32,33,34,35,36,
                     37,38,39,40,41,42,43,44,45]
'''
lotto_num1 = []
for n in range(1,46):
    lotto_num1.append(n)
ball_color = ["blue","orange","red","brown","purple","green"]
#print(lotto_num1)
    
random.shuffle(lotto_num1)
#print(lotto_num1)
'''
num1 = lotto_num1[0]
num2 = lotto_num1[1]
num3 = lotto_num1[2]
num4 = lotto_num1[3]
num5 = lotto_num1[4]
num6 = lotto_num1[5]
print(f"첫번째 공 = {num1}")
print(f"두번째 공 = {num2}")
print(f"세번째 공 = {num3}")
print(f"네번째 공 = {num4}")
print(f"다섯번째 공 = {num5}")
print(f"여섯번째 공 = {num6}")
'''

#제목
t.shape("turtle")
t.hideturtle()
t.speed(7)#0~10 가장빠른 0 10 9 8 7...
s = t.Screen()
t.bgcolor("black")
t.goto(0,200)
t.color("white")
t.write("Random Lotto",align= "center", font=("lmpact",90,"bold"))

t.penup()

count = 0
for i in range(-500,501,200):
    t.penup()
    t.goto(i,-100)
    t.pendown()
    t.color(ball_color[count])
    t.begin_fill()
    t.circle(70,360)
    t.end_fill()
    t.color("white")
    t.write(lotto_num1[count],align= "center",font=("lmpact",70,"bold"))
    count = count+1


































































