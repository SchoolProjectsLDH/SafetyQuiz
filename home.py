from Tkinter import *
import GenSafety
import PowerToolQuiz
import HandToolQuiz

class ButtonsDemo:
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


ButtonsDemo()
