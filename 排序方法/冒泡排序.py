def BubbleSort(li):
    for i in range(len(li)):
        for j in range(len(li)-1-i):
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]
        print(li)

li = [9,5,3,7,6,8,1,2,4]
BubbleSort(li)
