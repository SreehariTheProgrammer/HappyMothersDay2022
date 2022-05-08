from tkinter import CENTER, TOP
from turtle import *
from numpy import square
import random

bgcolor("black")
speed(-7)
for i in range(120):
    color("cyan")
    circle(i)
    color('orange')
    square(i*0.8)
    right(30)
    forward(30)

write("Happy Mothers Day!", font="Arial 100", align=CENTER)

done()