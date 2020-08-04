import random
ans=random.randint(1,100)
while True:
    number=int(input('請輸入數字:'))
    if number>100 or number<0:
        print('輸入錯誤')
    elif number>ans:
        print('小一點')
    elif number<ans:
        print('大一點')
    else:
        print('Bingo!')
        break 
