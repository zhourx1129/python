import numpy as np
def InsertionSort(arr):
    for i in range(len(arr)):
        preIndex = i-1   #已经排好序的列表
        current = arr[i]  #未排序列表的第一个元素
        while preIndex >= 0 and arr[preIndex] > current:
            arr[preIndex+1] = arr[preIndex]
            preIndex -= 1
        arr[preIndex+1] = current
    return arr

li = np.arange(15)
np.random.shuffle(li)
print("------------原列表----------")
print(li)
print("------------修改后----------")
# li = [9,5,3,7,6,8,1,2,4]
InsertionSort(li)
