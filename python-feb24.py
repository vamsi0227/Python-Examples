##class A:
##    def fun(self):
##        print("a")
##
##class B(A):
##    def fun(self):
##        print("b")
##
##class C(B):
##    def fun(self):
##        print("c")
##
##class D(C,B):
##    def fun1(self):
##        print("a")
##
##d = D()
##d.fun()


#File Operations.

##file_ob=open("seethamma.txt","w")
##file_ob.write("nannu kshaminchu amma")
##file_ob.close()

##file_ob=open("C:\Users\91832\Downloads\seethamma.txt","w")
##file_ob.write("hi")
##file_ob.close()
##
##
##import tkinter
##from tkinter import filedialog
##import os
##
##folder = filedialog.askdirectory()
##print(folder)
##
##file=os.path.join(folder,"seethamma.txt")
##
##file_ob=open(file,"w")
##file_ob.write("india")
##file_ob.close()


##import tkinter
##from tkinter import filedialog
##import os
##
##folder = filedialog.askdirectory()
##print(folder)
##
##file=os.path.join(folder,"seethamma.txt")
##
##file_ob=open(file,"a")
##file_ob.write("\n")
##file_ob.write(" is my country")
##file_ob.close()




##import tkinter
##from tkinter import filedialog
##import os
##
##root= tkinter.Tk()
##root.withdraw()
##
##folder = filedialog.askdirectory()
##print(folder)
##
##file=os.path.join(folder,"seethamma.txt")
##
##file_ob=open(file,"a")
##file_ob.write("\n")
##file_ob.write(" is my country")
##file_ob.close()

##file_ob=open(file,"w")
##file_ob.write("india)
##file_ob.close()

#Context manager

#w=wiriting a file

##with open("india.txt","w") as file_obj:
##    file_obj.write("this is")

##r-reading a file
##with open("india.txt","r") as file_obj:
##    file_content=file_obj.read()
##    print(file_content)


##with open("india.txt","r") as file_obj:
##    file_content=file_obj.read(5)
##    print(file_content)
##    file_content1=file_obj.read()
##    print(file_content1)


#to read lines
##with open("india.txt","r") as file_obj:
##    file_content=file_obj.readline()
##    print(file_content)
##    file_content1=file_obj.readline()
##    print(file_content1)

###to read lines
##with open("india.txt","r") as file_obj:
##    file_content=file_obj.readlines()
##    print(file_content)

























