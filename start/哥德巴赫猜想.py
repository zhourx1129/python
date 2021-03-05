#哥德巴赫猜想：输入一个大于6的偶数写出他的两个余数因子 比如18=11+7    18=13+5
from sys import exit   # 退出命令的库
num = int(input("请输入一个大于6的偶数"))

#判断是否满足条件，如果不满足提示退出
if num % 2 != 0 or num <6:
    print("输入有误，请按要求输入！")
    exit()
#判断是否为质素
# def prime(number):
#     flag = False
#     for i in range(2,int(number**0.5+1)):
#         if number % i != 0:
#             flag = True
#         else:
#             flag = False
#             break
#     if flag:
#         return number
#         # print("是质素")

def prime(number):
    for i in range(2,number+1):
       if number % i == 0:
           break
    if i >= number:
        return number
        # print("是质素")


for num1 in range(2,num//2):
    num2 = num - num1
    i = prime(num1)
    j = prime(num2)
    if i and j:
        print(num1,num2)
# prime(num)