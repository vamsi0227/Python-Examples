##class Svcet:
##    v="vamsi"
##    def fun():
##        print("vyshu")
##
##
##print(Svcet.v)
##Svcet.fun()

##class Svcet:
##    v="vamsi"
##    def fun():
##        print("vyshu")
##
##ob=Svcet
##print(ob.v)
##ob.fun()
##
##class Svcet:
##    v="vamsi"
##    def fun(self):
##        print("vyshu")
##
##ob=Svcet()
##print(ob.v)
##ob.fun()



class Svcet:
    """ This is my college"""
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def fun(self):
         print(self.name)
    def new(self):
         print(self.age)    
ab = Svcet("vamsi",23)
ab.fun()
ab.new()
print(ab.__doc__)































