# 실수 2개 입력받아 나눈 결과 계산하기

a,b = map(float,input().split())
c = a/b

print(format(c,".3f")) #소수점 셋쨰자리까지 반올림해서 출력