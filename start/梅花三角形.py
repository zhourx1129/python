rows = int(input("请输入要打印的行数"))
for i in range(rows):
    print(" " * ((rows-i) * 2),end='')
    print("* " * (2*i+1))
