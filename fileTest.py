# f=open("count_log.txt",'w',encoding="utf-8")
# for i in range(1,11):
#     data="%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()

# import os
# os.mkdir("log")
import time
from random import *

with open("log/count_log.txt", 'a', encoding="utf-8") as f:
    for i in range(1,11):
        stamp=str(time.time())
        value=str(random()*100000)
        f.write(stamp)
        f.write(value)