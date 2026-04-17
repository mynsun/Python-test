def add(x, y):
    return x + y

f = lambda x, y: x + y

print(add(1, 2))
print(f(1, 2))

f = lambda x: x if x % 3 == 0 else 0
print(f(3))
print(f(4))

nums = [1, 2, 3, 4, 5]
def pow(x):
    return x ** 2
f = lambda x: x**2

print(list(map(pow, nums)))
print(list(map(f, nums)))
print(list(map(lambda x: x**2, nums)))

nums1 = [1, 2, 3, 4, 5]
nums2 = [6, 7, 8, 9, 10]

print(list(map(lambda x, y: x*y, nums1, nums2)))

nums = list(range(1, 11))
print(list(map(lambda x: x*5, nums)))

ages = [18, 19, 39, 12, 43, 13, 21, 25]

def adult_func(age):
    if age >= 19:
        return True
    else:
        return False

for age in filter(adult_func, ages):
    print(age)
print()

for age in filter(lambda age: age >= 19, ages):
    print(age)

adult_ages = list(filter(lambda age: age >= 19, ages))
print(adult_ages)

nums = list(range(1, 11))
result = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, nums)))
print(result)

from functools import reduce

nums = [1, 2, 3, 4]
sum = reduce(lambda x, y: x+y, nums)
print(sum)

mul = reduce(lambda x, y: x*y, nums)
print(mul)

nums = list(range(1, 11))
nums = filter(lambda x: x % 2 == 0, nums)
result = reduce(lambda x, y: x*y, nums)
#또는 result = reduce(lambda x, y: x*y, filter(lambda x: x % 2 == 0, nums))

print(result)

list1 = list(range(1, 10))

list2 = list(map(lambda x: x**2, list1))
print(list2)

list3 = [x**2 for x in list1]
print(list3)
list4 = [x**2 for x in range(1, 10)]
print(list4)

list1 = list(range(1, 10))

list5 = [x**2 for x in list1 if x>5]
print(list5)

list6 = [x**2 for x in range(1, 10) if x%2 == 0]
print(list6)

nums = list(range(1, 11))
list1 = [x**2 for x in nums]
print(list1)

nums = list(range(1, 21))
list2 = [x for x in nums if x % 2 == 0]
print(list2)

list3 = [x for x in nums if x % 3 == 0]
print(list3)

list4 = [x**2 for x in nums if x % 5 == 0]
print(list4)