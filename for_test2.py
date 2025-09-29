#제어문 연습(중첩 if문) - 놀이동산 요금계산
# 주간, 야간, 대인, 소인 요금 구분하기
#주간 대인 50000 주산소인 40000
#야간 대인 30000 야간소인 20000
#출력 결과: 당신의 입장료는 OOO원입니다
'''
k = int(input('구분: 1. 주간 2. 야간?'))
m = int(input('대상: 1. 대인 2. 소인?'))

if k ==1: #주간
    if m==1: #대인
        pay = 50000
    else: #소인
        pay = 40000
else: # 야간
    if m==1:
        pay = 30000
    else:
        pay = 20000

print(f"당신의 입장료는 {pay}원 입니다")


# for반복문
# 2. 리스트 변수를 이용한 반복문
fruit = ['mango', 'apple', 'orange', 'kiwi', 'banana']
count = 0
#print(fruit[2])

for i in fruit:
    count +=1 #count = count +1
    print(count,". ",i)


n = [0,1,2,3,4]
for i in n:
    print(i+1,". 안녕하세요")


food = ("치킨", "삼겹살", "피자", "햄버거", "초밥", "스테이크")

print(type(food))

for f in food:
    print(f)

# 리스트 변수안에 있는 정수 값이 홀수 인지 짝수인지 판별하는 코드를 작성하시오

#OO는 짝수입니다 or OO는 홀수입니다

number = [273,103,5,32,65,9,72,880,99,58]

for n in number:
    if n %2 ==0:
        print(f"{n}은 짝수입니다") #print(n, "은 짝수입니다")
    else:
        print(f"{n}은 홀수입니다")


number = [273,103,5,32,65,9,72,880,99,58]

for n in number:
    print(f" {n}은 {len(str(n))}자리수 입니다")
'''
#5명의 정보처리 기능사 자격증 필기 점수가 리스트에 담겨있습니다.
#이때 각 점수가 합격 점수인지 불합격 점수인지 판별하여 출력하시오.(60점 이상 합격)
#98점으로 합격입니다.
#44점으로 불합격입니다.

score_list = [98,58,65,78,44]
count = 0
total = 0 # 합격한 친구들의 총점
i = 0 # 합격한 친구들의 인원 수
for score in score_list:
    count += 1
    if score >=60:
        total +=score
        i +=1
        print(f"{count}번 학생은 {score}점으로 합격입니다")
    else:
        print(f"{count}번 학생은 {score}점으로 불합격입니다")

print(f"총점은 {total}점 입니다")
#print(sum(score_list))

# 합격한 친구들의 평균 점수를 구하세요
#합격생의 평균은 80.33점 입니다
print(f"합격한 친구들의 총점은 {total}점 입니다")
print(f"합격한 친구들의 평균은 {round(total/i,2)}점 입니다")












































































































































































