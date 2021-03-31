x = 1
y = 2

x + y
x - y
x * y
x / y

#取整
7 // 4
#求余
10 % 4

#乘方
2 ** 3

#一个关于浮点数运算需要注意的地方
a = 4.2
b = 2.1
a + b

(a + b) == 6.3

from decimal import Decimal
a = Decimal('4.2')
b = Decimal('2.1')
a + b

(a + b) == Decimal('6.3')