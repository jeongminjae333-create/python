#summary.py
'''
1. 주석처리 # ''' '''   '' '' '' '' '' '' p134
2. 변수    p63
3. 문자열함수 p74 len() max() min() lower() upper() split()
4. input() 키보드로부터 입력
    =>  num = int(input("정수하나를 입력하세요: "))


    a = 10
    => str(a) => 10이 문자열을 바뀐다 캐스트 연산자

5. 리스트 변수
    여러개의 값 저장, 다른 자료형 저장 가능, [ ],변경 추가 삽입 삭제

    color = ["red", "green", "black"]
    값 추가 color.append.(" oragne")
    값 삽입 color.insert(1,"blue")
    값 삭제 remove() pop() del () # del color[2]

6. 이스케이프 문자 진달래꽃 실습  \ 사용
7. 연산자 p113
    산술연산자 + - * / // %
    비교연산자 > <>= <= == !=
    논리연산자 and or not
    대입연산자 = 
8. range(시작값,끝값,증감) 함수 p77
    range(5,20,3)      => 5 8 11 14 17
9.함수 p158 내장함수 사용자정의함수 라이브러리함수
   사용자정의함수 def 호출

   def sum(a,b):
       return a+b

   result = sum(44, 15) #인수 

10. 파일처리 

#----------------
#홀짝 판별 프로그램 작성
num = int(input("한개의 정수 입력: "))

if num % 2 == 0: 
   print("짝수입니다")
else:
   print("홀수입니다")

#구구단 출력
for i in range(4):
    for j in range(6):
        print(8)
'''
#
num = 0
while True:
    num += 1
    print(num)
    if num >= 5:
        break

# global 변수 

num = 3

def func(n):
    #global num 
    num = n * 3

func(num)
print(num) #9


































































































































