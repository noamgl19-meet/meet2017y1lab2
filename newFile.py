Python 3.5.2 (default, Nov 17 2016, 17:05:23) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> 
[DEBUG ON]
>>> 
[DEBUG OFF]
>>> type(259-33.0)
<class 'float'>
>>> type(4)
<class 'int'>
>>> type(string)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    type(string)
NameError: name 'string' is not defined
>>> type('4')
<class 'str'>
>>> type('four')
<class 'str'>
>>> type(5/2.0)
<class 'float'>
>>> type(12> 2*5)
<class 'bool'>
>>> type(color+3)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    type(color+3)
NameError: name 'color' is not defined
>>> type('color'*4)
<class 'str'>
>>> "color"*4
'colorcolorcolorcolor'
>>> "color"/4
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    "color"/4
TypeError: unsupported operand type(s) for /: 'str' and 'int'
>>> "color"^
SyntaxError: invalid syntax
>>> "color"**2
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    "color"**2
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
>>> color = blue
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    color = blue
NameError: name 'blue' is not defined
>>> color = 'blue'
>>> type(color+5)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    type(color+5)
TypeError: Can't convert 'int' object to str implicitly
>>> 
