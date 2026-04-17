f=open("test.txt",'r')
text=f.read()
print(text)
f.close()

with open('test.txt', 'r+') as f:
  text = f.read()
  print(text)

with open('test.txt', 'r+') as f:
  lines = f.readlines()
  for line in lines:
    print(line, end="")

text = "안녕하세요.\n파이썬입니다.\n반갑습니다.\n"
with open('test1.txt', 'w') as f:
  f.write(text)

texts = ["안녕하세요.","파이썬입니다.","반갑습니다."]
with open('test1.txt', 'a') as f:
  f.writelines(texts)