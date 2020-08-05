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
print('平均:',avg,'分')

highest=0
highest_name=''
lowest=999
lowest_name=''
for i in range (n):
    if scores[i]>highest:
        highest=scores[i]
        highest_name=names[i]
print('最高分為:',highest_name,',',highest,'分')

for a in range (n):
    if scores[a]<lowest:
        lowest=scores[a]
        lowest_name=names[a]
print('最低分為:', lowest_name,',',lowest,'分')

