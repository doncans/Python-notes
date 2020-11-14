Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import keywords
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import keywords
ModuleNotFoundError: No module named 'keywords'
>>> import keyword
>>> va = 10
>>> v1 = 10
>>> id(va)
140730298236256
>>> id(v1)
140730298236256
>>> def fun():
	va = 30

	
>>> type(fun)
<class 'function'>
>>> id(fun)
2066955836872
>>> va
10
>>> def fun():
	va = 30
	print(va)

	
>>> fun().va
30
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    fun().va
AttributeError: 'NoneType' object has no attribute 'va'
>>> fun()
30
>>> def fun():
	va = 30
	print(va)
	print(id(va))

	
>>> fun()
30
140730298236896
>>> id(va)
140730298236256
>>> 