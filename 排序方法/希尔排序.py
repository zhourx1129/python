import numpy as np
def fun(arr,gap):
    for i in range(len(arr)):
        preIndex = i-gap   #已经排好序的列表
        current = arr[i]  #未排序列表的第一个元素
        while preIndex >= 0 and arr[preIndex] > current:
            arr[preIndex+gap] = arr[preIndex]
            preIndex -= gap
        arr[preIndex+gap] = current
    print(li)

def SheelSort(li):
    gap = len(li) // 2
    while(gap != 0):
        fun(li,gap)
        gap = gap // 2

li = np.arange(15)
np.random.shuffle(li)
print("------------原列表----------")
print(li)
# li = [9,5,3,7, 6,8,1,2, 4]
SheelSort(li)
print("------------修改后----------")
print(li)