str = input("请输入一个字符串")

lis = list(str)
n = len(lis)
for i in range(n//2):
    if lis[i] != lis[n-1-i]:
        print("%s不是回文"%str)
        exit()
print("%s是回文"%str)






