#for_test.py
import turtle
#제어문 선택문 if 반복문 for while

#for문 실습
#1. 문자열을 이용한 반복문
'''
hi = "안녕하세요"

for ch in hi:
    print(ch,end='')

korea = "사랑하는 우리나라 대한민국"
count = 0
for i in korea:
    count = count+1
    print(count)

#공백을 만나면 다음줄로 개행 

korea = "나는 인평자동차고등학교 AI과 정민지입니다"
for i in korea:
    if i == '' '':
        print()
    else:
        print(i.end='')



#2. range() 반복문

for i in range(10):
    print("안녕",end='')
print("끝")


for i in range(10):
    print(i,end='*')

# 100까지의 수 중 3의 배수 출력
for i in range(1,101):
    print(i,end= '   ')
    if i %10 ==0:
        print()


#for문을 이용하여 23부터 40까지 출력하시오
for i in range(23, 41):
    print(i,end= '   ')
    if i %5 ==0:
        print()
     
#for문을 이용하여 97부터 77까지 출력하시오

for i in range(97,76,-1):
    print(i)
'''
'''
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
'''
#원한는 다각형을 그리는 프로그램

n = int(input("몇각형을 그릴까요?"))
for i in range(n):
    turtle.forward(100)
    turtle.left(360/n)
    j = 360/n
    print(j)











