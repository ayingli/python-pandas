x = '我是一个字符串'
y = "我也是一个字符串"
z = """我还是一个字符串"""


#字符串str用单引号(' ')或双引号(" ")括起来

#使用反斜杠(\)转义特殊字符。
s = 'Yes,he doesn\'t'

#如果你不想让反斜杠发生转义，
#可以在字符串前面添加一个r，表示原始字符串
print('C:\some\name')

print('C:\\some\\name')

print(r'C:\some\name')

#反斜杠可以作为续行符，表示下一行是上一行的延续。
s = "abcd\
efg"
print(s)

#还可以使用"""..."""或者'''...'''跨越多行

s = """
Hello I am fine!
Thinks.
"""
print(s)
