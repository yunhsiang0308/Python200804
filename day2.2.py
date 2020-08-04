number=int(input('輸入數字:'))
a=2
while a<number:
    if number%a==0:
        print('非質數')
        break
    a=a+1
if a==number:
    print('是質數')