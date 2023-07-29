import tkinter
from tkinter import*
root=Tk()
GR=Label(root,text="GOLDEN RATIO")
value=Label(root,text=(1+(5**(1/2)))/2)

last=Label(root,text="Golden Ratio is an irrational number, first descirbed in Euclid's Elements. It's value is found by {√5+1}/2.")
GR.pack()
value.pack()
last.pack()

