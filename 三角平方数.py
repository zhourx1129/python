def Square_number(num):
    sum = 0
    for i in range(1, num + 1):
        sum += i
        if sum == num:
            return True
        if sum > num:
            return False


def Trigonometric_number(num):
    temp = int(num ** 0.5)
    if temp * temp == num:
        return True


while True:
    num = int(input())
    if (Trigonometric_number(num) == True and (Square_number(num) == True)) :
        print("YES")
    else:
        print("NO")
    isContinue = input("是否继续Y/N?:>")
    if isContinue.upper() == 'N':
        break
    elif isContinue.upper() == 'Y':
        continue
    else:
        isContinue = input("输入有误,请重新输入Y/N:>")
