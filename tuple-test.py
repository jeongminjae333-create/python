# 컨테이너변수(시퀀스 자료형) 
# 리스트변수[] 튜프변수() 딕셔너리변수{} 문자형
# 리스트변수의 특징 - 여러개의 값, 수정, []

# 튜플변수 () 여러개의 값, 변경안됨, ()
t1 = (1,2,3) #튜플변수 생성
print(type(t1))

t2 = tuple(range(10))
print(t2)
list1 = list(range(10))
print(list1)

color = ('red', 'green', 'blue')
#color.append('yellow') 값 추가 불가
print(color[1]) #green출력 
print(color[1:])
print(t2[5::5])
print(t2[50::-5])


t1 = t1+t2
print(t1)

print("red" in color)

print("orange" not in color)

fruit =("사과", "포도", "멜론") #패킹(묶기)

(f1,f2,f3) = fruit #언패킹(풀기)
print(type(f1))

number = (1,2,3,4,5,6,7,8,9,10)
(n1, *ot,n10)=number
print(ot)
print(n1)
print(n10)

#딕셔너리 {} 
dic={'kor':80, 'eng':92, 'mat':77}
print(dic)
print(dic['kor'])

print('mat' in dic)
dic.setdefault('music',100)#새로운값 입력 

print(dic)
dic.pop('eng') #값삭제 pop
print(dic)
del dic['kor'] #값삭제 del
print(dic)
dic.clear()
print(dic)
