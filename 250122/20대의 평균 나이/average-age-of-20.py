cnt = 0
sum = 0

while True:
    ag = int(input())
    if ag // 10 == 2:
        sum += ag
        cnt += 1
    else:
        break

print(f"{sum / cnt:.2f}")