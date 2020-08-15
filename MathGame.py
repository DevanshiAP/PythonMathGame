import random
import operator

name=str(input('enter your name: '))
print('welcome ', name)

print("1: easy")
print("2: medium")
inp=int(input('enter your choice: '))

score=0

for i in range(0,15):

    if inp == 1:
        no1=random.randint(0,20)
        no2=random.randint(0,20)
        oper=[('+',operator.add),('-',operator.sub),('*',operator.mul)]
        op, fn = random.choice(oper)
        print("{} {} {}".format(no1, op, no2))
        ans=fn(no1, no2)
        userans=int(input('enter your answer'))
        if userans == ans:
            print("your answer correct")
            score=score+1
        else:
            print("sorry try again")
            print("your score is: {} /15".format(score))
            break

    if inp == 2:
        no1=random.randint(0,50)
        no2=random.randint(0,50)
        oper=[('+',operator.add),('-',operator.sub),('*',operator.mul)]
        op, fn = random.choice(oper)
        print("{} {} {}".format(no1, op, no2))
        ans=fn(no1, no2)
        userans=int(input('enter your answer'))
        if userans == ans:
            print("your answer correct")
            score=score+1
        else:
            print("sorry try again")
            print("your score is: {} / 15".format(score))
            break