lis = []
lis[0] = 0
lis[1] = 1
num = int(input("请输入要查看的个数"))
for i in range(2,num):
    lis[i] = lis[i-1] + lis[i-2]

print(lis)