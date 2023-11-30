# 월 입력받아 계절 출력하기

n = int(input())

if n//3 == 1 :
    print("spring") # 몫이 1인 3,4,5월은 봄 출력
elif n//3 == 2 :
    print("summer") # 몫이 2인 6,7,8월은 여름 출력
elif n//3 == 3 :
    print("fall") # 몫이 3인 9,10,11월은 가을 출력
else :
    print("winter") # 몫이 나머지인 12,1,2월은 겨울 출력