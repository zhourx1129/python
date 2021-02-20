# Factorial

num = int(input("请输入一个数字"))

p = 1
s = 0
for i in range(1,num+1):
    p = p * i
    s += p

print("%d的阶乘是%d\n阶乘之和是%d"%(num,p,s))
