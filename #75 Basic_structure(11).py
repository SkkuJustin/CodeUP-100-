# 정수 1개 입력 받아 0부터 해당 수까지 출력하기
# 4를 입력하면 --> 0 1 2 3 4 출력

n = int(input())

t = 0
while t <= n :
    print(t, end = ' ')
    t += 1