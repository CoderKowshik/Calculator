from tkinter import*
import math
obj=Tk()
obj.geometry("500x500")
obj.title("Calculator")
var=StringVar()
def zero():
    a=str(var.get())
    var.set(a+"0")
def one():
    a=str(var.get())
    var.set(a+"1")
def two():
    a=str(var.get())
    var.set(a+"2")
def three():
    a=str(var.get())
    var.set(a+"3")
def four():
    a=str(var.get())
    var.set(a+"4")
def five():
    a=str(var.get())
    var.set(a+"5")
def six():
    a=str(var.get())
    var.set(a+"6")
def seven():
    a=str(var.get())
    var.set(a+"7")
def eight():
    a=str(var.get())
    var.set(a+"8")
def nine():
    a=str(var.get())
    var.set(a+"9")
global op
global n1

class operator:
    def add(self):
        self.op="+"
        self.n1=int(var.get())
        var.set("0")
    def sub(self):
        self.op="-"
        self.n1=int(var.get())
        var.set("0")
    def mul(self):
        self.op="x"
        self.n1=int(var.get())
        var.set("0")
    def div(self):
        self.op="/"
        self.n1=int(var.get())
        var.set("0")
    def ac(self):
        self.op="0"
        var.set("0")
ob=operator()
class equal:
    def eql(self):
        if(ob.op=="+"):
            n2=int(var.get())
            var.set(ob.n1+n2)
        if(ob.op=="-"):
            n2=int(var.get())
            var.set(ob.n1-n2)
        if(ob.op=="x"):
            n2=int(var.get())
            var.set(ob.n1*n2)
        if(ob.op=="/"):
            n2=int(var.get())
            var.set(ob.n1/n2)
        
ob2=equal()
result=Entry(obj,textvariable=var).place(x=10,y=3)
b0=Button(obj,text="0",command=zero).place(x=75,y=94)
b1=Button(obj,text="7",command=seven).place(x=5,y=34)
b2=Button(obj,text="8",command=eight).place(x=25,y=34)
b3=Button(obj,text="9",command=nine).place(x=50,y=34)
b4=Button(obj,text="4",command=four).place(x=5,y=64)
b5=Button(obj,text="5",command=five).place(x=25,y=64)
b6=Button(obj,text="6",command=six).place(x=50,y=64)
b7=Button(obj,text="1",command=one).place(x=5,y=94)
b8=Button(obj,text="2",command=two).place(x=25,y=94)
b9=Button(obj,text="3",command=three).place(x=50,y=94)
b10=Button(obj,text="+",command=ob.add).place(x=75,y=64)
b11=Button(obj,text="-",command=ob.sub).place(x=75,y=34)
b12=Button(obj,text="x",command=ob.mul).place(x=105,y=34)
b13=Button(obj,text="/",command=ob.div).place(x=105,y=64)
b14=Button(obj,text="=",command=ob2.eql).place(x=105,y=94)
b15=Button(obj,text="AC",command=ob.ac).place(x=135,y=94)
obj.mainloop()
