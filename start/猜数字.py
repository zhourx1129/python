import random

result = random.randint(1,100)
num = eval(input("请输入你猜的数字"))
while num != result:
    if num > result:
        print("您猜的数字大了")
        num = eval(input("请您再猜一次:>"))
    else:
        print("您猜的数字小了")
        num = eval(input("请您再猜一次:>"))
else:
    print("恭喜您猜对了")
        









