'''import random
l=['rock','paper','scissors']
c1=0
c2=0
for i in range(10):
   a=random.choice(l)
   b=input('enter your choice')
   print(a)
   if b.lower()=='paper' and a=='rock':
       c1+=1
   elif b.lower()=='scissors' and a=='paper':
       c1+=1
   elif b.lower()=='rock' and a=='scissors':
       c1+=1
   elif b.lower()=='scissors' and a=='rock':
       c2+=1
   elif b.lower()=='rock' and a=='paper':
       c2+=1
   elif b.lower()=='paper' and a=='scissors':
       c2+=1
   elif b.lower()==a:
        print('draw')
if c1>c2:
    print('you won')
elif c1==c2:
   print('draw')
else:
    print('computer won')'''



    
    
