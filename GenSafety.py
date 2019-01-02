from sys import version_info
import GenResult
if version_info.major == 2:
    from Tkinter import *
elif version_info.major == 3:
    from tkinter import *

def GSQuiz():
    choices = ["True", "Yes", "Permission", "Certificate", "Push Stick", "Clean", "XXX", "No", "False", "Unplug"]
    CheckCorrect = [False,False,False,False,False,False,False,False,False,False]
    print("GenSafety quiz")
    GSWindow = Tk()
    GSWindow.title("General Safety Quiz")
    GSWindow.geometry("1000x800")
    GSWindow.resizable(False,False)

    mycanvas = Canvas(GSWindow, width = 1000, height = 800)
    mycanvas.create_rectangle(0, 0, 1000, 8000, fill = "#38761d")
    mycanvas.pack(side = "top", fill = "both", expand = True)

    #title
    title=Label(mycanvas,text="General Safety",font=("Helvetica",30),bg="#38761d",fg="white")
    title.place(x=350,y=10)

    #alternate wordbank
    xPos=125
    yPos=100
    choicePos=[[],[]]
    side1=mycanvas.create_line(25,75,25,250,width="3",fill="white")
    side2=mycanvas.create_line(25,250,975,250,width="3",fill="white")
    side3=mycanvas.create_line(975,250,975,75,width="3",fill="white")
    side4=mycanvas.create_line(975,75,25,75,width="3",fill="white")
    for x in range (0,5):
        op1=mycanvas.create_text(xPos,yPos,text=choices[x],font=('Helvetica', 15),fill="white")
        choicePos[0].append(xPos)
        choicePos[1].append(yPos)
        xPos=xPos+185
    xPos = 125
    yPos = 175
    for x in range (5,10):
        op1=mycanvas.create_text(xPos,yPos,text=choices[x],font=('Helvetica', 15),fill="white")
        choicePos[0].append(xPos)
        choicePos[1].append(yPos)
        xPos=xPos+185


    for y in range(len(choicePos[0])):
        print(choicePos[0][y],",", choicePos[1][y])

    def strike(selected):
        for iteration in range(0,10):
            if WordChoice1.get() != choices[iteration] and WordChoice2.get() != choices[iteration] and WordChoice3.get() != choices[iteration] and WordChoice4.get() != choices[iteration] and WordChoice5.get() != choices[iteration] and WordChoice6.get() != choices[iteration] and WordChoice7.get() != choices[iteration] and WordChoice8.get() != choices[iteration] and WordChoice9.get() != choices[iteration] and WordChoice10.get() != choices[iteration]:
                mycanvas.create_text(choicePos[0][choices.index(choices[iteration])],choicePos[1][choices.index(choices[iteration])],text=choices[choices.index(choices[iteration])],font=('Helvetica', 15),fill="white")
        op1=mycanvas.create_text(choicePos[0][choices.index(selected)],choicePos[1][choices.index(selected)],text=choices[choices.index(selected)],font=('Helvetica', 15),fill="red")

    #QUESTION 1---
    text_canvas = mycanvas.create_text(25, 325, anchor = "nw", font=('Helvetica', 15), fill="white")
    mycanvas.itemconfig(text_canvas, text="Q1: Minor injuries do not need to be reported. ->")
    WordChoice1 = StringVar(GSWindow)
    WordChoice1.set('Answer Here')
    WordDropdown1 = OptionMenu(mycanvas, WordChoice1, *choices).place(x=350,y=320)
    def change_dropdown1(*args):
        print( WordChoice1.get() )
        strike(WordChoice1.get())
        if WordChoice1.get() == "False" or WordChoice1.get() == "No":
            CheckCorrect[0] = True
            print(CheckCorrect)
        else:
            CheckCorrect[0] = False
            print(CheckCorrect)

    WordChoice1.trace('w', change_dropdown1)


    #QUESTION 2---
    text_canvas = mycanvas.create_text(25, 365, anchor = "nw", font=('Helvetica', 15), fill="white")
    mycanvas.itemconfig(text_canvas, text="Q2: If you are uncertain about something in the shop, it is okay to ask a peer. ->")
    WordChoice2 = StringVar(GSWindow)
    WordChoice2.set('Answer Here')
    WordDropdown2 = OptionMenu(mycanvas, WordChoice2, *choices).place(x=545,y=360)
    def change_dropdown2(*args):
        print( WordChoice2.get() )
        strike(WordChoice2.get())
    WordChoice2.trace('w', change_dropdown2)


    #QUESTION 3---
    text_canvas = mycanvas.create_text(25, 405, anchor = "nw", font=('Helvetica', 15), fill="white")
    mycanvas.itemconfig(text_canvas, text="Q3: Always get                                            from the instructor before using the drill press.")
    WordChoice3 = StringVar(GSWindow)
    WordChoice3.set('Answer Here')
    WordDropdown3 = OptionMenu(mycanvas, WordChoice3, *choices).place(x=140,y=400)
    def change_dropdown3(*args):
        print( WordChoice3.get() )
        strike(WordChoice3.get())
    WordChoice3.trace('w', change_dropdown3)

    #QUESTION 4---
    text_canvas = mycanvas.create_text(25, 445, anchor = "nw", font=('Helvetica', 15), fill="white")
    mycanvas.itemconfig(text_canvas, text="Q4: Students are not allowed to use equipment without having a safety                                       for that equipment")
    WordChoice4 = StringVar(GSWindow)
    WordChoice4.set('Answer Here')
    WordDropdown4 = OptionMenu(mycanvas, WordChoice4, *choices).place(x=490,y=440)
    def change_dropdown4(*args):
        print( WordChoice4.get() )
        strike(WordChoice4.get())
    WordChoice4.trace('w', change_dropdown4)

    #QUESTION 5---
    text_canvas = mycanvas.create_text(25, 485, anchor = "nw", font=('Helvetica', 15), fill="white")
    mycanvas.itemconfig(text_canvas, text="Q5: Use a                                         when cutting small pieces on a bandsaw.")
    WordChoice5 = StringVar(GSWindow)
    WordChoice5.set('Answer Here')
    WordDropdown5 = OptionMenu(mycanvas, WordChoice5, *choices).place(x=100,y=480)
    def change_dropdown5(*args):
        print( WordChoice5.get() )
        strike(WordChoice5.get())
    WordChoice5.trace('w', change_dropdown5)


    #QUESTION 6---
    text_canvas = mycanvas.create_text(25, 525, anchor = "nw", font=('Helvetica', 15), fill="white")
    mycanvas.itemconfig(text_canvas, text="Q6: After use,                                        and return the tool to its proper place")
    WordChoice6 = StringVar(GSWindow)
    WordChoice6.set('Answer Here')
    WordDropdown6 = OptionMenu(mycanvas, WordChoice6, *choices).place(x=120,y=520)
    def change_dropdown6(*args):
        print( WordChoice6.get() )
        strike(WordChoice6.get())
    WordChoice6.trace('w', change_dropdown6)


    #QUESTION 7---
    text_canvas = mycanvas.create_text(25, 565, anchor = "nw", font=('Helvetica', 15), fill="white")
    mycanvas.itemconfig(text_canvas, text="Q7: This is a filler text")
    WordChoice7 = StringVar(GSWindow)
    WordChoice7.set('Answer Here')
    WordDropdown7 = OptionMenu(mycanvas, WordChoice7, *choices).place(x=490,y=560)
    def change_dropdown7(*args):
        print( WordChoice7.get() )
        strike(WordChoice7.get())
    WordChoice7.trace('w', change_dropdown7)


    #QUESTION 8---
    text_canvas = mycanvas.create_text(25, 605, anchor = "nw", font=('Helvetica', 15), fill="white")
    mycanvas.itemconfig(text_canvas, text="Q8: It is okay to bring a drink into the shop as long as none of the equipment is running. ->")
    WordChoice8 = StringVar(GSWindow)
    WordChoice8.set('Answer Here')
    WordDropdown8 = OptionMenu(mycanvas, WordChoice8, *choices).place(x=615,y=600)
    def change_dropdown8(*args):
        print( WordChoice8.get() )
        strike(WordChoice8.get())
    WordChoice8.trace('w', change_dropdown8)


    #QUESTION 9---
    text_canvas = mycanvas.create_text(25, 645, anchor = "nw", font=('Helvetica', 15), fill="white")
    mycanvas.itemconfig(text_canvas, text="Q9: Once you have received your equipment certification you may use the equipment any time without permission. ->")
    WordChoice9 = StringVar(GSWindow)
    WordChoice9.set('Answer Here')
    WordDropdown9 = OptionMenu(mycanvas, WordChoice9, *choices).place(x=785,y=640)
    def change_dropdown9(*args):
        print( WordChoice9.get() )
        strike(WordChoice9.get())
    WordChoice9.trace('w', change_dropdown9)


    #QUESTION 10---
    text_canvas = mycanvas.create_text(25, 685, anchor = "nw", font=('Helvetica', 15), fill="white")
    mycanvas.itemconfig(text_canvas, text="Q10:                                       the tool/machine before replacing broken, dull or damaged bits or blades.")
    WordChoice10 = StringVar(GSWindow)
    WordChoice10.set('Answer Here')
    WordDropdown10 = OptionMenu(mycanvas, WordChoice10, *choices).place(x=65,y=680)
    def change_dropdown10(*args):
        print( WordChoice10.get() )
        strike(WordChoice10.get())
    WordChoice10.trace('w', change_dropdown10)

    #SUBMITBUTTON---
    def GetResult():
        GSWindow.destroy()
        GenResult.ReturnMark(CheckCorrect)
    #SubButton = PhotoImage(file = "Images/Submit.gif") --Not working
    Button(mycanvas, text="Submit Answers", command=GetResult).place(x=850,y=700)

    GSWindow.mainloop()
