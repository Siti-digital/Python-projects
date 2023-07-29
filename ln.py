import math
import tkinter
from tkinter import*
class log():
    x=1
    for i in range(0,100):
        print("log base e:-",x,"=",math.log(x))
        x=x+1
root=Tk()
lab=Label(root,text=log)
lab.pack()
