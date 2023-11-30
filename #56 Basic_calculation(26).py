#참 / 거짓이 서로 다를 때에만 참을 출력하기

a,b = map(int,input().split())

print((bool(a) and bool(not b)) or (bool(not a) and bool(b)))

# 3 0 이나 0 2 인 경우에만 출력해야하므로 위와 같이 (일부 암기 필요)