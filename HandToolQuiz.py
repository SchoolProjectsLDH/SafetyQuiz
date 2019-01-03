from sys import version_info
if version_info.major == 2:
    from Tkinter import *
elif version_info.major == 3:
    from tkinter import *
import HandToolResult
def HTQuiz():
    print("Hand Tool quiz")
    choices = ["Sharp", "Grab", "False", "Offset Screwdriver", "Face", "Robertson", "True", "Yes", "Drawer", "Glancing"]
    CheckCorrect = [False,False,False,False,False,False,False,False,False,False]
    HTWindow=Tk()
    HTWindow.title("Hand Tool Quiz")
    HTWindow.geometry("1000x800")
    HTWindow.resizable(False,False)

    HTcanvas = Canvas(HTWindow, width = 1000, height = 800)
    HTcanvas.create_rectangle(0, 0, 1000, 8000, fill = "#38761d")
    HTcanvas.pack(side = "top", fill = "both", expand = True)

    #title
    title=Label(HTcanvas,text="Hand Tools",font=("Helvetica",30),bg="#38761d",fg="white").place(x=500,y=10, anchor = CENTER)

    xPos=125
    yPos=100
    choicePos=[[],[]]
    side1=HTcanvas.create_line(25,75,25,250,width="3",fill="white")
    side2=HTcanvas.create_line(25,250,975,250,width="3",fill="white")
    side3=HTcanvas.create_line(975,250,975,75,width="3",fill="white")
    side4=HTcanvas.create_line(975,75,25,75,width="3",fill="white")
    for x in range (0,5):
        op1=HTcanvas.create_text(xPos,yPos,text=choices[x],font=('Helvetica', 15),fill="white")
        choicePos[0].append(xPos)
        choicePos[1].append(yPos)
        xPos=xPos+185
    xPos = 125
    yPos = 175
    for x in range (5,10):
        op1=HTcanvas.create_text(xPos,yPos,text=choices[x],font=('Helvetica', 15),fill="white")
        choicePos[0].append(xPos)
        choicePos[1].append(yPos)
        xPos=xPos+185


    def strike(selected):
        op1=HTcanvas.create_text(choicePos[0][choices.index(selected)],choicePos[1][choices.index(selected)])
        for iteration in range(0,10):
            if WordChoice1.get() != choices[iteration] and WordChoice2.get() != choices[iteration] and WordChoice3.get() != choices[iteration] and WordChoice4.get() != choices[iteration] and WordChoice5.get() != choices[iteration] and WordChoice6.get() != choices[iteration] and WordChoice7.get() != choices[iteration] and WordChoice8.get() != choices[iteration] and WordChoice9.get() != choices[iteration] and WordChoice10.get() != choices[iteration]:
                #mycanvas.delete(ALL)
                HTcanvas.create_text(choicePos[0][choices.index(choices[iteration])],choicePos[1][choices.index(choices[iteration])],text=choices[choices.index(choices[iteration])],font=('Helvetica', 15),fill="white")

        """    if WordChoice1.get() != choices[iteration] and WordChoice2.get() != choices[iteration] and WordChoice3.get() != choices[iteration] and WordChoice4.get() != choices[iteration] and WordChoice5.get() != choices[iteration] and WordChoice6.get() != choices[iteration] and WordChoice7.get() != choices[iteration] and WordChoice8.get() != choices[iteration] and WordChoice9.get() != choices[iteration] and WordChoice10.get() != choices[iteration]:
                mycanvas.delete(op1)
                op1=mycanvas.create_text(choicePos[0][choices.index(selected)],choicePos[1][choices.index(selected)],text=choices[choices.index(selected)],font=('Helvetica', 15,),fill="white")"""
        op1=HTcanvas.create_text(choicePos[0][choices.index(selected)],choicePos[1][choices.index(selected)],text=choices[choices.index(selected)],font=('Helvetica', 15,"overstrike"),fill="red")


    #QUESTION 1---
    text_canvas = HTcanvas.create_text(25, 325, anchor = "nw", font=('Helvetica', 15), fill="white")
    HTcanvas.itemconfig(text_canvas, text="Q1: You should use a long throat clamp instead of a deep throat clamp. ->")
    WordChoice1 = StringVar(HTWindow)
    WordChoice1.set('Answer Here          ')
    WordDropdown1 = OptionMenu(HTcanvas, WordChoice1, *choices).place(x=510,y=320)
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
    text_canvas = HTcanvas.create_text(25, 365, anchor = "nw", font=('Helvetica', 15), fill="white")
    HTcanvas.itemconfig(text_canvas, text="Q2: Without padding, a clamp can leave marks on your work ->")
    WordChoice2 = StringVar(HTWindow)
    WordChoice2.set('Answer Here          ')
    WordDropdown2 = OptionMenu(HTcanvas, WordChoice2, *choices).place(x=450,y=360)
    def change_dropdown2(*args):
        print( WordChoice2.get() )
        strike(WordChoice2.get())
        if WordChoice2.get()=="Yes" or WordChoice2.get()=="True":
            CheckCorrect[1]=True
            print(CheckCorrect)
        else:
            CheckCorrect[1]==False
            print(CheckCorrect)
    WordChoice2.trace('w', change_dropdown2)

    #QUESTION 3---
    text_canvas = HTcanvas.create_text(25, 405, anchor = "nw", font=('Helvetica', 15), fill="white")
    HTcanvas.itemconfig(text_canvas, text="Q3: We store C clamps in the                                           .")
    WordChoice3 = StringVar(HTWindow)
    WordChoice3.set('Answer Here          ')
    WordDropdown3 = OptionMenu(HTcanvas, WordChoice3, *choices).place(x=230,y=400)
    def change_dropdown3(*args):
        print( WordChoice3.get() )
        strike(WordChoice3.get())
        if WordChoice3.get()=="Drawer":
            CheckCorrect[2]=True
            print(CheckCorrect)
        else:
            CheckCorrect[2]=False
            print(CheckCorrect)
    WordChoice3.trace('w', change_dropdown3)

    #QUESTION 4---
    text_canvas = HTcanvas.create_text(25, 445, anchor = "nw", font=('Helvetica', 15), fill="white")
    HTcanvas.itemconfig(text_canvas, text="Q4: For hammers, you should use the                                                 to hit an object")
    WordChoice4 = StringVar(HTWindow)
    WordChoice4.set('Answer Here          ')
    WordDropdown4 = OptionMenu(HTcanvas, WordChoice4, *choices).place(x=275,y=440)
    def change_dropdown4(*args):
        print( WordChoice4.get() )
        strike(WordChoice4.get())
        if WordChoice4.get()=="Face":
            CheckCorrect[3]=True
            print(CheckCorrect)
        else:
            CheckCorrect[3]=False
            print(CheckCorrect)
    WordChoice4.trace('w', change_dropdown4)

    #QUESTION 5---
    text_canvas = HTcanvas.create_text(25, 485, anchor = "nw", font=('Helvetica', 15), fill="white")
    HTcanvas.itemconfig(text_canvas, text="Q5: For a hammer, You should avoid                                                 blows when hitting an object.")
    WordChoice5 = StringVar(HTWindow)
    WordChoice5.set('Answer Here          ')
    WordDropdown5 = OptionMenu(HTcanvas, WordChoice5, *choices).place(x=265,y=480)
    def change_dropdown5(*args):
        print( WordChoice5.get() )
        strike(WordChoice5.get())
        if WordChoice5.get()=="Glancing":
            CheckCorrect[4]=True
            print(CheckCorrect)
        else:
            CheckCorrect[4]=False
            print(CheckCorrect)
    WordChoice5.trace('w', change_dropdown5)

    #QUESTION 6---
    text_canvas = HTcanvas.create_text(25, 525, anchor = "nw", font=('Helvetica', 15), fill="white")
    HTcanvas.itemconfig(text_canvas, text="Q6: The square head screwdriver is called a:")
    WordChoice6 = StringVar(HTWindow)
    WordChoice6.set('Answer Here          ')
    WordDropdown6 = OptionMenu(HTcanvas, WordChoice6, *choices).place(x=320,y=520)
    def change_dropdown6(*args):
        print( WordChoice6.get() )
        strike(WordChoice6.get())
        if WordChoice6.get()=="Robertson":
            CheckCorrect[5]=True
            print(CheckCorrect)
        else:
            CheckCorrect[5]=False
            print(CheckCorrect)
    WordChoice6.trace('w', change_dropdown6)

    #QUESTION 7---
    text_canvas = HTcanvas.create_text(25, 565, anchor = "nw", font=('Helvetica', 15), fill="white")
    HTcanvas.itemconfig(text_canvas, text="Q7: You should use an                                                 in tight areas")
    WordChoice7 = StringVar(HTWindow)
    WordChoice7.set('Answer Here          ')
    WordDropdown7 = OptionMenu(HTcanvas, WordChoice7, *choices).place(x=177,y=560)
    def change_dropdown7(*args):
        print( WordChoice7.get() )
        strike(WordChoice7.get())
        if WordChoice7.get()=="Offset Screwdriver":
            CheckCorrect[6]=True
            print(CheckCorrect)
        else:
            CheckCorrect[6]=False
            print(CheckCorrect)
    WordChoice7.trace('w', change_dropdown7)

    #QUESTION 8---
    text_canvas = HTcanvas.create_text(25, 605, anchor = "nw", font=('Helvetica', 15), fill="white")
    HTcanvas.itemconfig(text_canvas, text="Q8: You should use a                                                 blade when cutting")
    WordChoice8 = StringVar(HTWindow)
    WordChoice8.set('Answer Here          ')
    WordDropdown8 = OptionMenu(HTcanvas, WordChoice8, *choices).place(x=175,y=600)
    def change_dropdown8(*args):
        print( WordChoice8.get() )
        strike(WordChoice8.get())
        if WordChoice8.get()=="Sharp":
            CheckCorrect[7]=True
            print(CheckCorrect)
        else:
            CheckCorrect[7]=False
            print(CheckCorrect)
    WordChoice8.trace('w', change_dropdown8)

    #QUESTION 9---
    text_canvas = HTcanvas.create_text(25, 645, anchor = "nw", font=('Helvetica', 15), fill="white")
    HTcanvas.itemconfig(text_canvas, text="Q9: Do not                                                 a falling knife")
    WordChoice9 = StringVar(HTWindow)
    WordChoice9.set('Answer Here          ')
    WordDropdown9 = OptionMenu(HTcanvas, WordChoice9, *choices).place(x=100,y=640)
    def change_dropdown9(*args):
        print( WordChoice9.get() )
        strike(WordChoice9.get())
        if WordChoice9.get()=="Grab":
            CheckCorrect[8]=True
            print(CheckCorrect)
        else:
            CheckCorrect[8]=False
            print(CheckCorrect)
    WordChoice9.trace('w', change_dropdown9)

    #QUESTION 10---
    text_canvas = HTcanvas.create_text(25, 685, anchor = "nw", font=('Helvetica', 15), fill="white")
    HTcanvas.itemconfig(text_canvas, text="Q10: You can leave hot glue guns unattended if unplugged. ->")
    WordChoice10 = StringVar(HTWindow)
    WordChoice10.set('Answer Here          ')
    WordDropdown10 = OptionMenu(HTcanvas, WordChoice10, *choices).place(x=427,y=680)
    def change_dropdown10(*args):
        print( WordChoice10.get() )
        strike(WordChoice10.get())
        if WordChoice10.get()=="Yes" or WordChoice10.get()=="True":
            CheckCorrect[9]=True
            print(CheckCorrect)
        else:
            CheckCorrect[9]=False
            print(CheckCorrect)
    WordChoice10.trace('w', change_dropdown10)

    #SUBMITBUTTON---
    def GetHTResult():
        HTWindow.destroy()
        HandToolResult.ReturnHTMark(CheckCorrect)
    #SubButton = PhotoImage(file = "Images/Submit.gif") --Not working
    Button(HTcanvas, text="Submit Answers", command=GetHTResult).place(x=850,y=700)
    HTWindow.mainloop()
