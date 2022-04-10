n = input()
total = 0
for i in range (0,len(n)):
    try:
        if int(n[i])%2 == 1:
            total += int(n[i])
    except ValueError:
        n = n
print(total)
