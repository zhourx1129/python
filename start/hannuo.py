
def move(A,C):
    print(f"{A}-->{C}",end='  ')

def hannuo(n,A,B,C):
    if(n==1):
        move(A,C)
    else:
        hannuo(n-1,A,C,B)
        move(A,C)
        hannuo(n-1,B,A,C)

if __name__ == '__main__':
    n = int(input("请输入一个数"))
    hannuo(n,'A','B','C')