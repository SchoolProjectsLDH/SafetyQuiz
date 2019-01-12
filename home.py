from sys import version_info
if version_info.major == 2:
    from Tkinter import *
elif version_info.major == 3:
    from tkinter import *


import GenSafety #imports the module GenSafety
import PowerToolQuiz #same as import GenSafety
import HandToolQuiz #same as import GenSafety
window = Tk() #creaetes TK Window called window
class HomeClass: #creates a class called Home Class
    def __init__(self):
        BackgroundImage = PhotoImage(file = "Images/MainTitlePage.gif") #creates a variable called background image and sets it to the Main Title Page gif
        BackgroundLabel = Label(window, image = BackgroundImage) #creates a label called backgroundlabel on the window and sets it to an image (background image)
        BackgroundLabel.place(x=0,y=0,relwidth = 1, relheight=1) #placing the backgroundlabel on the screen
        window.title("Safety Quiz") #sets the title of the window as safety quiz
        window.geometry("1000x800") #sets the dimensions of the window
        window.resizable(False, False) #makes it not resizable/ can't change size
        GSButton = PhotoImage(file = "Images/GSButton.gif") #creates a variable called GSButton and sets it to the image of the GS Button
        PTButton = PhotoImage(file = "Images/PTButton.gif") #same as GSButton, but for the PTButton
        HTButton = PhotoImage(file = "Images/HTButton.gif") #same as GSButton, but for HTButton
        QTButton = PhotoImage(file = "Images/QuitButton.gif") #same as GSButton, but for QTButton
        Button(image = GSButton, command = self.GenSafetyFunc, highlightbackground="black", borderwidth=0).place(x=260, y=600, anchor = CENTER) #creates a button using the image stored in GSButton and uses the function GenSafetyFunc
        Button(image = PTButton, command = self.PowToolSafetyFunc, highlightbackground="black", borderwidth=0).place(x=500, y=600, anchor = CENTER) #same as previous button, but for the uses the PTButton and PowerToolSafetyFunc
        Button(image = HTButton, command = self.HanToolSafetyFunc, highlightbackground="black", borderwidth=0).place(x=750, y=600, anchor = CENTER) #same as previous button, but uses HT/HandToolSafety
        Button(image = QTButton, command = self.QuitQuiz, highlightbackground="black", borderwidth=0).place(x=900, y=75, anchor = CENTER) #same as previous button, but uses the lines assoicated with quit
        window.mainloop()

    def GenSafetyFunc(self): #creates a function called GenSafetyFunc
        canvas1 = Canvas(window, width = 200, height = 50) #creates a canvas that is 200 by 50
        canvas1.place(x=260,y=600,anchor=CENTER) #place the canvas in the center of the window
        canvas1.create_rectangle(0, 0, 200, 50, fill = "black") #creats a black rectange
        window.iconify() #minimizes window (puts in task bar)
        GenSafety.GSQuiz() #calls the function GSQuiz
    def PowToolSafetyFunc(self): #same as the GenSafety Function, but calls PTQuiz instead
        canvas2 = Canvas(window, width = 244, height = 50)
        canvas2.place(x=500,y=600,anchor=CENTER)
        canvas2.create_rectangle(0, 0, 244, 50, fill = "black")
        window.iconify()
        PowerToolQuiz.PTQuiz()
    def HanToolSafetyFunc(self):#same as the GenSafety Function, but calls HTQuiz instead
        canvas3 = Canvas(window, width = 224, height = 50)
        canvas3.place(x=750,y=600,anchor=CENTER)
        canvas3.create_rectangle(0, 0, 224, 50, fill = "black")
        window.iconify()
        HandToolQuiz.HTQuiz()
    def QuitQuiz(self): #creates a function called QuitQuiz
        window.destroy() #destroys the window
        exit() #cloeses the program


HomeClass() #calls HomeClass
