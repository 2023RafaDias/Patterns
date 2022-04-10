height,width = map(int,input().split())
lst = []
for a in range(0,height):
    enterRow = []
    for b in range(0,width):
        enter = 0
        if a+1 < height:
            enter += 1
        if b+1 < width:
            enter+= 1
        if a-1 >= 0:
            enter+= 1
        if b-1 >= 0:
            enter+=1
        enterRow.append(enter)
    lst.append(enterRow)
print(lst)        
