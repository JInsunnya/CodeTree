numbers = []  # 숫자를 저장할 리스트
satisfied = True  # 초기 상태는 True

# 5개의 숫자를 입력받음
for _ in range(5):
    a = int(input())
    if a % 3 != 0:  # 3의 배수가 아닌 경우
        satisfied = False

# 결과 출력
if satisfied:
    print(1)
else:
    print(0)


# satisfied = True

# while True:
#     a = int(input())
#     if a % 3 != 0:
#         satisfied = False

# if satisfied == True:
#     print(1)
# else:
#     print(0)