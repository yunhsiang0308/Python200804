import random
ans=random.randint(1,10)
number=int(input('請輸入數字:'))
if number>10 or number<0:
    print('輸入錯誤')
elif number==ans:
    print('Bingo~')
else:
    print('你猜錯了!')