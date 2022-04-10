import math
n = input()
nArray = []
for i in range(0,len(n)):
    try:
        int(n[i])
        nArray.append(int(n[i]))
    except ValueError:
        n = n
print(nArray)
print(len(nArray))
division = int(math.sqrt(len(nArray)))
add = division
count = 0
n = 0
while n != len(nArray):
    if nArray[count] == 1:
        state = "true"
    else:
        state = "false"
    for i in range(n,division):
        if i != count and nArray[i]!= 0:
            state = "false"
    count+= add+1
    n += division
    division+= division
print(state)
