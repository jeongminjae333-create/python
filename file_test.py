#file_test.py
#열기모드 r w a x t b
'''
f = open("file.txt","w")
f.write("hello")
f.write("\n")
f.write("2회고사 망함")
f.write("두번째 실행")
f.close()

f = open("file.txt" , "a")
f.write("\n")
f.write("황예준 바보")
f.close()

f = open("file.txt" , "r")
w = f.read(100)
print(w)
f.close()
'''
f = open("live.txt" , "wt")
f.write('''삶이 그대를 속일지라도
슬퍼하거나 노하지 말라~
우울한 날들을 견디면
믿으라 기쁨의 날이 오리니''')
f.close()

#파일 내용앞에 일련번호 붙이기
f = open("live.txt" , "rt")
text = ""
line = 1
while True:
    row = f.readline()
    if not row:
        break
    text += str(line) + ":" + row
    line += 1
f.close()
print(text)
















































































































































































