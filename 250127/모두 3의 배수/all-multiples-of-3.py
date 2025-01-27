satisfied = True  

for _ in range(5):
    a = int(input())
    if a % 3 != 0:  
        satisfied = False

if satisfied:
    print(1)
else:
    print(0)