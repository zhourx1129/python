import numpy as np
def SelectSort(li):
    for i in range(len(li)-1):
        # min_num = i
        for j in range(i+1,len(li)):
            if li[j] < li[i]:
                li[j],li[i] = li[i],li[j]
        print(li)

li = np.arange(100)
np.random.shuffle(li)
# li = [9,5,3,7,6,8,1,2,4]
SelectSort(li)