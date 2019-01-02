from sys import version_info
if version_info.major == 2:
    from Tkinter import *
elif version_info.major == 3:
    from tkinter import *

def PTQuiz():
    print("Power tool quiz")
    PTWindow=Tk()
    PTWindow.title("Power Tool Quiz")
    PTWindow.geometry("1000x800")
    PTWindow.resizable(False,False)
    PTWindow.mainloop()
