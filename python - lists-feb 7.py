##var = []
##print(type(var))
##
##

##var =["d","a","g"]
##var[1] = "r"
##print(var)
## idi mutable

##var =["a","s"]
##print(dir(var))

##
##var = ["a","B"]
##var1 = ["c","d"]
##print(var + var1)


##a = ["d","h"]
##b=a   # shallow copy ante oka dantlo vachina change inkoka dantlo automatic ga vacsthundi
##print(a)
##print(b)
##b[0]="v"
##print(a)
##print(b)

##a = ["d","h"]
##b=a[:] #deep copy ante oka dantlo matrame changes untai
##print(a)
##print(b)
##b[0]="v"
##print(a)
##print(b)

##var=["a","s","d"]
##var[0]="v"
##print(var)
##


##var=["a","s","d"]
##var.insert(0,"v")
##print(var)


##var=["a","s","d"]
##var.append("v")
##print(var)


##var=["a","s","d"]
##var.delete("a")
##print(var)




##var=["a","s","d"]
##var.append("v","m")
##print(var)

##var=["a","s","d"]
##var.extend(["v","m"])
##print(var)


##v =["d","f","g","h"]
##v.sort()
##print(v)



##v =["d","f","g","h"]
##v.sort(reverse=True)
##print(v)

##v =["d","f","g","h"]
##output=sorted(v,reverse=True)
##print(output)

##v =["dyyyyy","fee","guuu","h"]
##output=sorted(v,key=len)
##print(output)

##v =["d","f","g","h"]
##v.pop(2)
##print(v)

##v =["d","f","g","h"]
##v.pop()
##print(v)


##v =["d","f","g","h"]
##v.remove("f")
##print(v)

##v =["d","f","g","h"]
##v.clear()
##print(v)

##v =["d","f","g","h"]
##del v
##print(v)

##v =["d","f","g","h"]
##del v[0]
##print(v)

##v =("d","f","g","h")
##print(type(v))



