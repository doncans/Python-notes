# Python-notes
I) Features:

    1. Easy to understand
    2. High Level Programming language
    3. Interpreted Language
    4. Standard Libraries
    5. Huge Cummunity support
    6. Portable
    7. Extensible
    8. Inegrated 
    
note: Python can used for diffent domain software develoments(like desktop GUI applications, data science, iot, ai, ml, web applications, networking, telecome, storage...etc)
Reserved Words:

and, del, global, not, with, as, elif, if, or, yield, assert, else, import, pass, break, except, in, raise, class, finally,   is, return, continue,  for, lambda, try, def, from, nonlocal, while

Python Data Types:

Numeric: 
        Int, Float, Complex
Dictionary : 
        dict 
sequence Type:
    List, Tuple, String
Set
Boolean

Variable:

A Python variable is a symbolic name that is a reference or pointer to an object. Once an object is assigned to a variable, you can refer to the object by that name. But the data itself is still contained within the object.

a = 10
a reference to the integer object

II) python installation on Windows

https://www.python.org/ftp/python/3.7.4/python-3.7.4-amd64.exe

Click on the Add path check box while installation 

---------------------------------------------------
String:

string is a sequence of characters enclosing with in the single quotes or double quotes like 'hello world' or "hello world"

1> we can access individual characters using index

2> index starts from Zero

st1 = "Hello world"
       012345678910
       
st1[0] = 'H'

st1[1] = 'e'

st1[2] = 'l' ....like that etc..

3>slicing allow to access part of string

syntax:

[start:stop:step]

st1[0:4:1]

'Hell'

st1[0:4:2]

'Hl'

Common string Methods:
    capitalize(), casefold(), center(), lower(), upper(), join(), split(), find(), replace() etc.


