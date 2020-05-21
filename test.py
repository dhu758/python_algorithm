from  datetime import datetime as dt
year=dt.today().year
your_year=int(input('태어난 년도를 입력하시오: '))
age=year-your_year+1
if 20>age>=17:
    print(age,'살은 고등학생입니다.')
elif 27>age>=20:
    print(age,'살은 대학생입니다.')
else:
    print(age,'살은 학생이 아닙니다.')