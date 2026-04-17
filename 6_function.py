def hello():
    print('Hello World!')

hello()

def hello4(greeting, *names):
    for name in names:
        print(greeting, name)

hello4('안녕', '진', '슈가', '제이홉', 'RM', '지민')

def function(first, second, third):
    return first + second + third

print(function(3, 5, 7))
print(function(first=3, second=5,third=7))
print(function(second=5, third=7, first=3))

def function1(first=1, second=3, third=5):
    return first + second + third

print(function1())
print(function1(1))
print(function1(first=1, second=5))

def function2(first, second, third=5):
    return first + second + third

print(function2(1, 2))
print(function2(1, second=5))
print(function2(second=5, first=2))

def function():
    return 1, "Hello", True

a, b, c = function()
print(a, b, c)
a = function()
print(a)

def ret_list():
    return [1, 2]

l = ret_list()
print(l)
n1, n2 = ret_list()
print(n1, n2)
n1, _ = ret_list()
print(n1)

def divide(n1, n2):
    res1 = n1 // n2
    res2 = n1 % n2
    return res1, res2

d = divide(17, 4)
print(d)
n1, n2 = d
print(n1, n2)
n1, _ = divide(25, 6)
print(n1)