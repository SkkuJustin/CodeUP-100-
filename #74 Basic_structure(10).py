# 문자 1개 입력받아 알파벳 출력하기

n = ord(input()) # 문자를 유니코드 숫자로 변환
t = ord('a')

while t<=n :
    print(chr(t), end = ' ')
    t = t+1