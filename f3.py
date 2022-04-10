n = input()
for i in range (0,len(n)):
    try:
        if int(n[i])%2 == 1:
            print(n[i])
    except ValueError:
        n = n
