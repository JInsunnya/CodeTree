n = int(input())

for _ in range(2):  # 두 개의 블록을 출력
    for _ in range(n):
        print("*" * n)  # n개의 '*' 출력
    print()  # 블록 사이에 한 줄 띄우기

# n = int(input())

# for _ in range(2):
#     for _ in range(n):
#         for _ in range(n):
#             print("*", end="")
#         print("")