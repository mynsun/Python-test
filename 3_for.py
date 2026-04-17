for i in range(10):
    print('Hello World!')

for i in range(1, 10):
    print('Hello World!', i)

for i in range(10, 0, -1):
    print(i)

print('----------')

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in list1:
    print(num)

fruits = ('apple', 'orange', 'grape')
for fruits in fruits:
    print(fruits)

tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for num in tuple1:
    print(num)

str_count = input('반복할 횟수를 입력하세요: ')
count = int(str_count)

for i in range(count):
    print('Hello, World!', i)

for i in range(10):
    for fruits in fruits:
        print(i, fruits)

str_dan = input('출력할 단수를 입력해주세요: ')
dan = int(str_dan)

for i in range(1, 10):
    #print(dan, 'x', i, '=', dan*i)
    print('{} x {} = {}'.format(dan, i, dan*i))
print('----------')

for i in range(1, 10):
    for j in range(1, 10):
        print('{} x {} = {}'.format(i, j, i*j))
    print('----------')

for i in range(0, 11):
    if i % 2 != 0:
        print(i)
        continue