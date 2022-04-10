n = list(input())
maximum = 0
for i in range(0,len(n)):
    try:
        n[i] = int(n[i])
        if n[i] > maximum:
            maximum = n[i]
    except ValueError:
        n = n
print(maximum)
