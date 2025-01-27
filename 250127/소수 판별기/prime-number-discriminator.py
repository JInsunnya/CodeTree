n = int(input())

satis = True

i = 2
while i < n :
    if n % i == 0:
        satis = False
        break
    i += 1

if satis == True:
    print("P")
else:
    print("C")



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