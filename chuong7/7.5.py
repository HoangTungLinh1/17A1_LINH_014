Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x=10
y=4
print('x =%d.y = %d'%(x,y))
x =10.y = 4
equivelence = x==y
print('x==y is', equivelence)
x==y is False
equivelence = x!=y
print('x!=y is', equivelence)
x!=y is True
equivelence = x>y
print('x>y is', equivelence)
x>y is True
x=8
y=9
print('x =%d.y = %d'%(x,y))
x =8.y = 9
>>> equivelence = x>=y
>>> print('x>=y is', equivelence)
x>=y is False
>>> equivelence = x<y
>>> print('x<y is', equivelence)
x<y is True
>>> equivence = x<=y
>>> print('x<=y is', equivelence)
x<=y is True
>>> 
================================ RESTART: Shell ================================
>>> x=15
>>> y=12
>>> print('Binary of x =', bin(x), ', Binary of y=', bin(y))
Binary of x = 0b1111 , Binary of y= 0b1100
>>> print('x & y =', bin(x & y))
x & y = 0b1100
>>> print('x / y =', bin(x / y))
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print('x / y =', bin(x / y))
TypeError: 'float' object cannot be interpreted as an integer
>>> print('x / y', bin(x / y))
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    print('x / y', bin(x / y))
TypeError: 'float' object cannot be interpreted as an integer
>>> print('x / y=', bin(x | y))
x / y= 0b1111
>>> print('x ^ y =', bin(x ^ y))
x ^ y = 0b11
>>> print('~x =', bin(x~))
SyntaxError: invalid syntax
>>> print('~x =', bin(~x))
~x = -0b10000
>>> print('x << 2=', bin(x << 2))
x << 2= 0b111100
>>> print('y >> 2 =',bin(y>>2))
y >> 2 = 0b11
