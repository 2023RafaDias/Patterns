n = input()
nArray = []
for i in range(0,len(n)):
    try:
        int(n[i])
        nArray.append(int(n[i]))
    except ValueError:
        n = n
print(nArray)

count = 0
while count != len(nArray):
    for i in range (nArray[count],-1,-1):
        print(nArray[count], end = " ")
        nArray[count] -= 1
    count += 1
    print(" ")
