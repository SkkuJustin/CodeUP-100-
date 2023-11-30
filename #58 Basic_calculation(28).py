# 둘 다 거짓일 경우에만 참 출력하기

a,b = map(int,input().split())

c = bool(a)
d = bool(b)

print(not(c or d))