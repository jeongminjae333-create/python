#turtle_pattern.py

from turtle import * 
#import turtle  as t          

'''

#색상 설정

color =[]

color ('orange', 'blue') # 선 색은'red', 채우는 색은 'yellow'로 설정

begin_fill() #도형을 그리기 시작할 때 채우기를 시작

while True: #무란 루프 시작(조건을 만족할 때까지 계속 반복)
    forward(200) #터틀이 200픽셀만큼 직선으로 이동
    left(170) #터틀이 왼쪽으로 170도 회전
    # abs(pos( )) < 1: 터틀이 처음 위치에 근접하면 루프 종료
    if abs(pos( )) < 1: #터틀이 시작 위치 근처에 있으면(거리가 1픽셀 이내이면)종료
        break #루프를 종료
    
end_fill() #도형을 그리는 것이 끝났으므로 채우기를 완료
done() #그래픽 창을 닫지 않고 유지 (그리기 작업이 끝났음을 알림)

color ('orange', 'blue') # 선 색은'red', 채우는 색은 'yellow'로 설정
speed(7)
begin_fill() #도형을 그리기 시작할 때 채우기를 시작

while True: #무란 루프 시작(조건을 만족할 때까지 계속 반복)
    forward(10) #터틀이 200픽셀만큼 직선으로 이동
    left(20) #터틀이 왼쪽으로 170도 회전
    circle(100)
    # abs(pos( )) < 1: 터틀이 처음 위치에 근접하면 루프 종료
    if abs(pos( )) < 1: #터틀이 시작 위치 근처에 있으면(거리가 1픽셀 이내이면)종료
        break #루프를 종료
    
end_fill() #도형을 그리는 것이 끝났으므로 채우기를 완료
done() #그래픽 창을 닫지 않고 유지 (그리기 작업이 끝났음을 알림)

import turtle

# 창 설정
screen = turtle.Screen()
screen.bgcolor("black")  # 배경을 검정색으로 설정

# 거북이 설정
t = turtle.Turtle()
t.speed(0)  # 거북이 속도를 최고로 설정
t.width(2)  # 선의 두께 설정

# 색상 목록
colors = ["red", "yellow", "green", "blue", "purple", "orange"]

# 패턴 그리기
for i in range(360):
    t.pencolor(colors[i % 6])  # 색상을 반복해서 사용
    t.forward(i * 3 / 5 + i)  # 선의 길이
    t.left(59)  # 방향 전환

turtle.done()
'''
import turtle

# 터틀 화면 설정
screen = turtle.Screen()
screen.bgcolor("black")  # 배경을 검정색으로 설정

# 터틀 객체 생성
t = turtle.Turtle()
t.speed(0)  # 가장 빠른 속도로 설정
t.width(2)  # 선 굵기 설정

# 색상 목록 (여러 색을 사용해 그라데이션 효과를 줄 수 있음)
colors = ["red", "yellow", "green", "blue", "purple", "orange"]

# 나선형 패턴 그리기
for i in range(360):
    t.pencolor(colors[i % 6])  # 색상 변경
    t.forward(i * 3 / 10 + i)  # 조금씩 더 멀리 이동
    t.left(59)  # 일정 각도로 회전

# 터틀 종료
t.hideturtle()
turtle.done()























































































