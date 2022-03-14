import pandas


var = [4,5,6,7]
print(type(var))
print(var)

b=pandas.Series(var)
print(type(b))
print(b)
a = sum(b)
print(a)
