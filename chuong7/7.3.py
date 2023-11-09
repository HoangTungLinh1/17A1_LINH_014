Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=6
>>> S=1+x+(x**3)/3+(x**5)/5
>>> print(S)
1634.2
>>> 
================================ RESTART: Shell ================================
>>> result=1+2
>>> print('result =', result)
result = 3
>>> original_result=result
>>> result=result-1
>>> print('result =',result)
result = 2
>>> original_result=result
>>> result=result*2
>>> original_result=result
>>> print('result =',result)
result = 4
>>> result=result**3
>>> original_result=result
>>> print('result =',result)
result = 64
>>> result=result+8
>>> original_result=result
>>> print('result =',result)
result = 72
>>> result=result%7
>>> original_result=result
>>> print('result =',result)
result = 2
>>> result=result//2
>>> original_result=result
>>> print('result =',result)
result = 1
>>> 
================================ RESTART: Shell ================================
>>> result==5
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    result==5
NameError: name 'result' is not defined
>>> 
============================================================================================================ RESTART: Shell ============================================================================================================
>>> result=5
>>> print('result =',result)
result = 5
>>> result-=1
>>> print('result =',result)
result = 4
>>> result+=3
>>> print('result =',result)
result = 7
>>> result=-result
>>> print('result =',result)
result = -7
>>> result=True
>>> print('not result =',not result)
not result = False
