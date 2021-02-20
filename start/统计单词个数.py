str = input("请输入单词\n")
count = 0
str = str.title()  #首字母大写
str = str.strip()  #去除两边空格
for string in str:
    if 'Z' >= string >= 'A':
        count += 1
print(count)