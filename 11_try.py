str1 = input('피젯수를 입력하시오. ')
str2 = input('젯수를 입력하시오. ')

try:
    num1 = int(str1)
    num2 = int(str2)
    result = num1 / num2
    print('{} / {} = {}'.format(num1, num2, num1/num2))
except:
    print('입력값을 확인하시오.')

str1 = input('피젯수를 입력하시오. ')
str2 = input('젯수를 입력하시오. ')

try:
    num1 = int(str1)
    num2 = int(str2)
    result = num1 / num2
    print('{}  / {} = {}'.format(num1, num2, num1/num2))
except ValueError:
    print('숫자를 입력하시오.')
except ZeroDivisionError:
    print('0으로 나눌수 없습니다.')
except Exception as e:
    print('excpetion:', e)

str1 = input('젯수를 입력하시오.')
str2 = input('피젯수를 입력하시오.')

try:
    num1 = int(str1)
    um2 = int(str2)
    result = num1 / num2
except Exception as e:
    print("excpetion:", e)
else :
    print('{}/{} = {}'.format(num1, num2, num1/num2))

try:
    with open('test11.txt', 'r+') as f:
        text = f.read()
        print(text)
except Exception as e:
    print('파일을 여는 중 예외가 발생했습니다.')