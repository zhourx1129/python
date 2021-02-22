def InsertionSort(li):
    n = len(li)
    for i in range(1,n):
        # tem = li[i]
        for j in range(i,0,-1):
            if li[j-1] > li[j]:
                li[j-1],li[j] = li[j],li[j-1]
        print(li)


li = [9,5,3,7,6,8,1,2,4]
InsertionSort(li)