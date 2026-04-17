import datetime #import 키워드를 사용해서 모듈을 추가

today = datetime.date.today()
print(today)

now = datetime.datetime.now()
print(now)

print(now.year)
print(now.month)
print(now.day)

dir(datetime)

import datetime as dt # as를 사용해서 별칭 지정

today = dt.date.today()
print(today)

now = dt.datetime.now()
print(now)

know = now + dt.timedelta(hours=9)
print(know)

time_diff = know - now
print(time_diff)

from datetime import datetime, date

xmas1 = datetime(2023, 12, 25, 0, 0, 0)
print(xmas1)

xmas2 = date(2023, 12, 15)
print(xmas2)

import time

print(time.time())

local_time = time.localtime(time.time())
str_time = time.strftime('%Y-%m-%d %H:%M:%S', local_time)
print(str_time)

import random
print(random.random()) # 0~1미만의 실수 난수 발생
print(random.randrange(1, 7)) #1~6까지의 정수 난수 발생
print(random.randint(1, 7)) #1~7까지의 정수 난수 발생
list1 = [1,2,3,4,5,6,7,8,9,10]
random.shuffle(list1) # list의 아이템 순서를 바꿈
print(list1)
print(random.choice(list1)) # list의 아이템 중 하나를 임의로 선택
print(random.sample(list1, 5)) # list의 아이템 중 5개의 아이템을 임의로 선택

import random

set1 = set()
while len(set1) < 6:
    set1.add(random.randint(1, 45))

print(set1)
result = sorted(set1)
print(type(result))
print(result)

list1 = list(range(1, 46))
random.shuffle(list1)
result = list1[0:6]
result.sort()
print(result)

list1 = list(range(1, 46))
result = random.sample(list1, 6)
result.sort()
print(result)

import os
dir(os)

print(os.sep)
cur_dir = os.getcwd()
print(cur_dir)
test_dir = os.path.join(cur_dir, 'test')

print(test_dir)

print(os.path.exists(test_dir))
if not os.path.exists(test_dir):
    os.mkdir(test_dir)
print(os.path.exists(test_dir))