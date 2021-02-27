import numpy as np

def Quick_Sort(li,left,right):
    tem = li[left]
    while left < right:
        while left < right and li[right] >= tem:
            right -= 1
        li[left] = li[right]
        # print(li,'left')
        while left < right and li[left] <= tem:
            left += 1
        li[right] = li[left]
        # print(li,'right')
    li[left] = tem
    # print(li)
    return left


def QuickSort(li,left,right):
    if left < right:
        mid = Quick_Sort(li,left,right)
        QuickSort(li,left,mid-1)
        QuickSort(li,mid+1,right)

li = np.arange(100)
np.random.shuffle(li)
# li = [9,5,3,7,6,8,1,2,4]
QuickSort(li,0,len(li)-1)
print(li)