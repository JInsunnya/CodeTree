n=int(input())

for i in range(2,n):
    if n%i!=0:
        print("P")
    else:
        print("C")
    break


# n = int(input())
# satisfied = True

# for i in range(1, n+1):
#     if i % 1 == 0 and i % n+1 == 0:
#         satisfied = True
#     else:
#         satisfied = False

# if satisfied == True:
#     print("P")
# else:
#     print("C")