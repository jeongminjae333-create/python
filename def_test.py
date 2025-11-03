#def_test.py
#함수 일정한 동작을 수행하는 코드의 집합 호출 재사용
#1. 내장함수 print() imput() max() range()....
#2. 사용자 정의 함수 내가 
#3. 라이브러리 함수 Import tutle random 남이
'''
def hello():
    print("안녕하세요")
    print("인평자동차고등학교")
    print("정민재입니다.")

hello()

#호출(Call)로 실행 재사용
def hi(name): #매개변수
    print(f"hi~~!!!{name}야!!!")

hi("카리나") #인수
hi("아이유")
hi("최서림")
hi("한예준")

#두수를 더하는 함수
def add(x,y):
    print(f"{x}+{y} = {x+y}")

a =int(input("덧셈에 필요한 첫번째 수: "))
b =int(input("덧셈에 필요한 두번째 수: "))
add(a,b)



def 안녕(name1,name2,name3):
    print("안녕하세요",name2)
    print("안녕하세요",name3)
    print("안녕하세요",name1)


안녕("예준", "경효", "서림") #인수3개



#두수를 더하는 계산기 
def add(x,y):
    return x+y #반환값

a =int(input("덧셈에 필요한 첫번째 수: "))
b =int(input("덧셈에 필요한 두번째 수: "))
result = add(a,b)
print(f"{a}와{b}를 더한값은 {result}입니다")
'''
#사칙연산 계산기

def add_num(x,y): #덧셈
    return x+y

def sub_num(x,y): #뺄셈
    return x-y

def mul_num(x,y): #곱셈
    return x*y

def div_num(x,y): #나눗셈
    return x//y

print("###사칙연산 계산기###")
a =int(input("연산에 필요한 첫번째 수: "))
b =int(input("연산에 필요한 두번째 수: "))

op_code = input("연산자를 선택하세요(+,-,*,//): ")


if op_code == "+":
    result = add_num(a,b)
    print(f"{a}와 {b}의 합은 {result}입니다.")
elif op_code == "-":
    result = sub_num(a,b)
    print(f"{a}와 {b}의 차는 {result}입니다.")
elif op_code == "*":
    result = mul_num(a,b)
    print(f"{a}와 {b}의 곱은 {result}입니다.")
else:
    result = div_num(a,b)
    print(f"{a}와 {b}의 몫은 {result}입니다.")







































