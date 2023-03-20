from cmdformatter import *
import time

ScreenFlush()
write("Hello World!" , color=CMD_RED , end="\n")
x= "We will use some built-in modules and libraries and some custom codes as well. Let's first have a quick look over how Python represents color codes.In the Python programming language, text can be represented using different colors. There are very simple to use Python libraries for colors and formatting in the terminal. The programmer gets better responses by printing colored texts.Let's see some useful examples to color text in Python."
write(x, colorList=CMD_ALL,  cyclic=True, totalTime= 3)
