type(10)

print(1/2)
print(5//3)
print(5**3)
print(20%3)

print('Hello' + 'World!')
print('Hello'*2)

num=4
print(num)
num *= 3
print(num)
num/= 3
print(num)
num**= 2
print(num)

print('Hello' < 'World!')
print('홍길동' != '허균')

print(True and False)
print(True or False)
print(not False)
print(5 < 6 and True)

age = 20
name = '홍길동'
print(name, age)
print('이름은', name, '나이는', age)
print('이름은 ' + name + '나이는 ' + str(age))

str1 = "{}".format(10)
print(str1)

str2 = "{}과 {}".format(10, 20)
print(str2)

num1 = 10
num2 = 20
str3 = "{}x{}={}".format(num1, num2, num1*num2)
print(str3)

str4 = '이름은 {} 나이는 {}'.format(name, age)
print(str4)
str5 = '이름은 {0} 나이는 {1}'.format(name, age)
print(str5)
print('이름은 {1} 나이는 {0}'.format(age, name))

str7 = '이름은 {:s} 나이는 {:d}'.format(name, age)
print(str7)
print('pi = {:f}'.format(3.141592))
print('pi = {:10f}'.format(3.141592))
print('pi = {:5.2f}'.format(3.141592))
print('pi = {:.2f}'.format(3.141592))

print('이름은 %s 나이는 %d'%(name, age))
print('이름은 %s 나이는 %5d'%(name, age))
print('pi = %f'%3.141592)

scores = [30, 50, 90, 89, 56, 87]
score0 = scores[0]
print(score0)
print(scores[5])
print(scores[0])
print(scores[-1]) # 역순은 -1부터 존재함

scores[1] = 100
print(scores)
#scores[6] = 400 #범위 밖의 값으로 에러 발생

scores.append(99)
scores.append('Hello')
print(scores)

scores.insert(1, 33)
scores.insert(2, 'World')
print(scores)

list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9, 10]
print(list1 + list2)
print(list1 * 3)

scores = [30, 50, 90, 89, 56, 87, 45]
length = len(scores)
print('scores의 길이는 {}입니다.'.format(length))

bts = ["진", "슈가", "제이홉", "RM", "지민", "뷔", "정국"]
print('bts의 멤버는 {}명 입니다.'.format(len(bts)))

numbers = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 10]

numbers1 = numbers[0:4]
print(numbers1)
print(numbers[:4])
print(numbers[7:11])
print(numbers[7:])
print(numbers[:])

#range([start], stop, [step])
r1 = range(1, 10, 1)
print(r1)

r2 = range(10, 20, 2)
print(r2)

r3 = range(10, 1)
print(r3)

r4 = range(10, 0, -1)
print(r4)

r5 = range(10, 0, -2)
print(r5)

list1 = list(range(10))
print(list1)
list2 = list(range(1, 10))
print(list2)
list3 =list(range(1, 10, 2))
print(list3)
list4 = list(range(10, 0, -1))
print(list4)

student = ('전정국', '인공지능학과', 3, 175,3, 3.5, True)
print(student)
print(student[0])
car = ('Tesla', 'model3', 'red', 500)
print(car)

range1 = range(10)
tuple1 = tuple(range1)
print(tuple1)
range2 = range(-5, 15, 2)
print(tuple(range2))

input('프롬프트 문자열')

age = input('나이를 입력하시오')
print(age)
num = 3
diff = input('변화량을 입력하시오')
#print(num + diff) #입력받은 값은 문자열로 반환하기 때문에 타입이 맞지 않아 에러 반환

print(num + int(diff))