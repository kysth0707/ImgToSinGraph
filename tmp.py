# k = 16252182913652238420585638837354496
# print(len(str(bin(k))[2:]), str(bin(k)))
def get_binary_value(d, b, c, n):
    # 각 단계 계산
    divisor = 2 ** (b * (c - n + 1))  # 나눗셈 기준값
    shifted = d // divisor           # 데이터 이동
    result = shifted % (2 ** b)      # 해당 데이터 추출
    return result

d=690603722277077361802396436830400872443264495
b=5
c=30
for n in range(1, c+1):
	print(get_binary_value(d, b, c, n+1), int((d-2**(b*(c-n+1))*int(d/2**(b*(c-n+1))))/2**(b*(c-n))))

