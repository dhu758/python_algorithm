from random import *
rnum=randint(1,100)
while 1:
    num=int(input('숫자를 입력하시오: '))
    if rnum==num:
        print('정답!!')
        break
    elif num>rnum:
        print('숫자가 너무 큽니다.')
    else:
        print('숫자가 너무 작습니다.')