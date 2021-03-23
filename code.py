Coding:

def swapList(newList):
    size = len(newList)
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp
    return newList
a=int(input())
newList = list(input().split())
b=swapList(newList)
for i in range(0,a-1):
    print(b[i],end=" ")
print(b[a-1])
