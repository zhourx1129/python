def SelectSort(li):
    for i in range(len(li)-1):
        min_num = i
        for j in range(i+1,len(li)):
            if li[j] < li[min_num]:
                li[j],li[min_num] = li[min_num],li[j]
        print(li)

li = [9,5,3,7,6,8,1,2,4]
SelectSort(li)