from sys import version_info
if version_info.major == 2:
    from Tkinter import *
elif version_info.major == 3:
    from tkinter import *

def HTQuiz():
    print("Hand Tool quiz")
    HTWindow=Tk()
    HTWindow.title("Hand Tool Quiz")
    HTWindow.geometry("1000x800")
    HTWindow.resizable(False,False)
    HTWindow.mainloop()
