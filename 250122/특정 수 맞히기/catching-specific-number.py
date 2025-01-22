while True:
    i = int(input())
    if i == 25:
        s = "Good"
        print(s)
        break
    elif i < 25:
        s = "Higher"
    else:
        s = "Lower"
    print(s)