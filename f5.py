n = list(input())
n2 = []
for i in range(0,len(n)):
    try:
        n[i] = int(n[i])
        n[i] *= n[i]
        n2.append(n[i])
    except ValueError:
        n = n
        
print(n2)

