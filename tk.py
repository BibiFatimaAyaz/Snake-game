#import tkinter as tk
#gui=tk.Tk()
#  print("Game Start")

#btn=tk.Button(gui,text="START")
#btn.place(x=300,y=90)
import turtle as t
from random import randint

class MyTurtle(t.Turtle) :

    def __init__(self,**args) :
        t.Turtle.__init__(self,**args)

    def mygoto(self,x,y) :
        t1.goto(x,y)
        print (x,y)

    def randonics(self,x,y) :
        self.left(randint(90,270))

def minegoto(x,y) :
    print (x,y)
    t1.goto(x,y)
    wt=t.Screen()
t1=MyTurtle()
wt.register_shape("big",((0,0),(30,0),(30,30),(0,30)))
t1.shape("big")
wt.onclick(t1.mygoto,btn=1)
wt.onclick(minegoto,btn=2)
t1.onclick(t1.randonics,btn=3)
t1.goto(100,100)

t.mainloop()