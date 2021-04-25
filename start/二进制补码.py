# 完成相加函数
def add(list1):
    result = 0
    for i in range(len(list1)):
        temp = int(list1[i]) * 2 ** (len(list1)-1-i)
        result += temp
    return result
# 补码函数
def complement(list1):
    for i in range(len(list1)):
        if list1[i] != '0':
            list1[i] = '0'
        else:
            list1[i] = '1'
# 程序开始处
n = input()
if len(n) != 32:
    n = input("请输入32位二进制整数")
list1 = list(n)
# 负数
if list1[0] == '1':
    # 取反
    complement(list1)
    # 求得结果后+1
    sum = -(add(list1)+1)
else:
    sum = add(list1)

print(sum)
