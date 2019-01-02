from sys import version_info
if version_info.major == 2:
    from Tkinter import *
elif version_info.major == 3:
    from tkinter import *


import GenSafety
import PowerToolQuiz
import HandToolQuiz
window = Tk()
class HomeClass:
    def __init__(self):
        BackgroundImage = PhotoImage(file = "Images/MainTitlePage.gif")
        BackgroundLabel = Label(window, image = BackgroundImage)
        BackgroundLabel.place(x=0,y=0,relwidth = 1, relheight=1)
        window.title("Safety Quiz")
        window.geometry("1000x800")
        window.resizable(False, False)


        GSButton = PhotoImage(file = "Images/GSButton.gif")
        PTButton = PhotoImage(file = "Images/PTButton.gif")
        HTButton = PhotoImage(file = "Images/HTButton.gif")
        QTButton = PhotoImage(file = "Images/QuitButton.gif")
        Button(image = GSButton, command = self.GenSafetyFunc, highlightbackground="#38761d", borderwidth=0).place(x=260, y=600, anchor = CENTER)
        Button(image = PTButton, command = self.PowToolSafetyFunc, highlightbackground="#38761d", borderwidth=0).place(x=500, y=600, anchor = CENTER)
        Button(image = HTButton, command = self.HanToolSafetyFunc, highlightbackground="#38761d", borderwidth=0).place(x=750, y=600, anchor = CENTER)
        Button(image = QTButton, command = self.QuitQuiz, highlightbackground="#38761d", borderwidth=0).place(x=900, y=75, anchor = CENTER)
        window.mainloop()

    def GenSafetyFunc(self):
        window.destroy()
        GenSafety.GSQuiz()
    def PowToolSafetyFunc(self):
        window.destroy()
        PowerToolQuiz.PTQuiz()
    def HanToolSafetyFunc(self):
        window.destroy()
        HandToolQuiz.HTQuiz()
    def QuitQuiz(self):
        window.destroy()
        exit()


HomeClass()
