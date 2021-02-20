for i in range(100,1000):
    gewei = i % 10
    shiwei = i % 100 // 10
    baiwei = i // 100
    if gewei+shiwei*10+baiwei*100 == gewei**3+shiwei**3+baiwei**3:
        print(i)
        