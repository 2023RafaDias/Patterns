n = input()
count = 0
for i in range (0,len(n)):
    try:
        if int(n[i])%2 == 1:
            count += i
    except ValueError:
        n = n
print(count)
