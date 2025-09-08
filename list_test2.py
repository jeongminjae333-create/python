# 리스트 변수 - 여러개의 값을 저장, 값을 변경,[]
'''
score = []
print(score)
print(type(score))

score = [90.2, 78.6, 89.5, 67.8, 60.2, 99.5, 52.8]
#sort() 오름차순 정렬
print(score)

# score를 역순으로 정렬하세요 


h = [5, 4, 9, 2, 7, 3]

#역순정렬하세요

h.sort()
h.reverse()
print(h)
#h.sort(reverse=True)

fruit = ["사과" , "샤인머스캣" , "복숭아" , "바나나" , "딸기"]

fruit.remove("바나나")
print(fruit)
fruit.append("망고")
print(fruit)
fruit.pop(0)
print(fruit)
fruit.insert(2,"딸기")
print(fruit)

#리스트 변수 append(), remove(), insert(), pop(), sort(), reverse()


name_list = ["김건영", "김의준", "김진성", "남명진", "박한올"]
print(name_list)
name_list[2] ="김하성"
print(name_list)
name_list[4] ="백지율"
print(name_list)
#["김건영", "김의준", "김진성", "남명진", "박한올"]
#인덱싱 
print(name_list[0:2])
print(name_list[1:4])
print(name_list[0:5:2]) #김건영 김하성 백지율

print(name_list[1:4:2]) #김의준 남명진
print(len(name_list))

print('남명진' in name_list)

h = [5, 4, 9, 2, 7, 3]
print(7 in h)
print(8 in h)
print(9 not in h)
'''
import random

#random() 난수발생
'''
x = random.random() #0-1사이의 난수 
print(x)

x = [1,2,3,4,5,6,7,8,9]
print(x)
y =random.choice(x)
print(y)
z = random.shuffle(x)
print(x)
z = random.sample(x,2)
print(z)
'''
x = random.randint(1,18)
print(x)
x = random.randint(1,18)
print(x)
x = random.randint(1,18)
print(x)




























