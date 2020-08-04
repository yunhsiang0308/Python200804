names=[]
scores=[]
total=0
avg=0
n=int(input('請輸入班級總人數:'))

for a in range(n):
    name=input('請輸入你的名字:')
    score=int(input('請輸入你的分數:'))
    names.append(name)
    scores.append(score)
print(scores)

for i in scores:
    total=total+i
    avg=total/n
print('平均:',avg)

highest=0
lowest=999
for i in scores:
    if i>highest:
        highest=i
print('最高分為:',highest)

for a in scores:
    if lowest>a:
        lowest=a
print('最低分為:',lowest)











