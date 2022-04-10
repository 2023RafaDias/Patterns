n = list(input())
total = 0
count = 0
for i in range(0,len(n)):
    try:
        n[i] = int(n[i])
        total += n[i]
        count += 1
    except ValueError:
        n = n
print(total/count)
