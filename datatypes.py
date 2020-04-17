#datatypes in python
"""
1)Numeric
     i)int
     ii)float
     iii)complex
     iv)bool

2)string
3)None(Null)
4)List
5)Tuple
6)Set
7)Dictionary(Maps)
"""
a = None;      #none/null
print(a, type(a))

#numeric datatypes
#int
a = 15
print(type(a))
#float
a = 2.5
print(type(a))
#complex
a = 1+2j
print(type(a))

#converting from one type to another
a = 50.584
a = int(a)
print(a, type(a))

a = float(a)
print(a, type(a))

a = 12
b = 16
c = complex(a)
print(c)

c = complex(a, b)
print(c)
#bool
a, b = 15, 16
print(a>b)

a = True
b = False

print(int(a))
print(int(b))
print(bool(0))
print(bool(2))

#list
lst = [26,8,56,864,6]
print(lst, type(lst))

#tuple
tup = (12,486,86,46)
print(tup, type(tup))

#set
sets = {468,456,456}
print(sets, type(sets))

#dictionary
dic = {47:"deepak"}
print(dic, type(dic))

#string
string = "Deepak"
print(string, type(string))

#range(final) starting from 0  or range(start, final)
print(range(10), type(range(10)))

print(list(range(10)))

#range also took 3 parameters
a = list(range(2, 20, 3))
print(a)

#dictionary

