from tkinter import *
import GenSafety
import PowerToolQuiz
import HandToolQuiz

class HomeClass:
    def __init__(self):
        window = Tk()
        Background = PhotoImage(file = "Images/MainTitlePage.gif")
        BackgroundL = Label(window, image = Background)
        BackgroundL.place(x=0,y=0,relwidth = 1, relheight=1)
        window.title("Safety Quiz")
        window.geometry("1000x800")
        window.resizable(False, False)


        GSButton = PhotoImage(file = "Images/GSButton.gif")
        PTButton = PhotoImage(file = "Images/PTButton.gif")
        HTButton = PhotoImage(file = "Images/HTButton.gif")

        Button(image = GSButton, command = self.GenSafetyFunc, highlightbackground="#38761d", borderwidth=0).place(x=260, y=600, anchor = CENTER)
        Button(image = PTButton, command = self.PowToolSafetyFunc, highlightbackground="#38761d", borderwidth=0).place(x=500, y=600, anchor = CENTER)
        Button(image = HTButton, command = self.HanToolSafetyFunc, highlightbackground="#38761d", borderwidth=0).place(x=750, y=600, anchor = CENTER)

        window.mainloop()

    def GenSafetyFunc(self):
        GenSafety.GSQuiz()
    def PowToolSafetyFunc(self):
        PowerToolQuiz.PTQuiz()
    def HanToolSafetyFunc(self):
        HandToolQuiz.HTQuiz()


HomeClass()


"""
problem 1 problem would not work, the was an error saying it could not find module Tkinter. This is because to use Tkinter you have to use a lower case t to call it so it would be tkinter
method prior knowledge
Solution: change all Tkinter to tkinter

problem 2: not really a problem but more suggestion, change the name of Background variables to be more detailed on what they mean or at least add comments because it was hard to understand
what you were doing with them

"""
