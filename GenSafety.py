from sys import version_info
import GenResult
if version_info.major == 2:
    from Tkinter import *
elif version_info.major == 3:
    from tkinter import *

def GSQuiz():
    choices = ["Yes", "Clean", "Push Stick", "No", "Unplug", "False", "Permission", "XXX", "Certificate", "Never!"]
    CheckCorrect = [False,False,False,False,False,False,False,False,False,False]
    GSWindow = Tk()
    GSWindow.title("General Safety Quiz")
    GSWindow.geometry("1000x800")
    GSWindow.resizable(False,False)

    mycanvas = Canvas(GSWindow, width = 1000, height = 800)
    mycanvas.create_rectangle(0, 0, 1000, 8000, fill = "#38761d")
    mycanvas.pack(side = "top", fill = "both", expand = True)

    #title
    title=Label(mycanvas,text="General Safety",font=("Helvetica",30),bg="#38761d",fg="white").place(x=500,y=25, anchor = CENTER)

    #wordbank
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

    def strike(selected):
        op1=mycanvas.create_text(choicePos[0][choices.index(selected)],choicePos[1][choices.index(selected)])
        for iteration in range(0,10):
            if WordChoice1.get() != choices[iteration] and WordChoice2.get() != choices[iteration] and WordChoice3.get() != choices[iteration] and WordChoice4.get() != choices[iteration] and WordChoice5.get() != choices[iteration] and WordChoice6.get() != choices[iteration] and WordChoice7.get() != choices[iteration] and WordChoice8.get() != choices[iteration] and WordChoice9.get() != choices[iteration] and WordChoice10.get() != choices[iteration]:
                mycanvas.create_text(choicePos[0][choices.index(choices[iteration])],choicePos[1][choices.index(choices[iteration])],text=choices[choices.index(choices[iteration])],font=('Helvetica', 15),fill="white")
        op1=mycanvas.create_text(choicePos[0][choices.index(selected)],choicePos[1][choices.index(selected)],text=choices[choices.index(selected)],font=('Helvetica', 15,"overstrike"),fill="red")

    #QUESTION 1---
    text_canvas = mycanvas.create_text(25, 325, anchor = "nw", font=('Helvetica', 15), fill="white")
    mycanvas.itemconfig(text_canvas, text="Q1: Minor injuries do not need to be reported. ->")
    WordChoice1 = StringVar(GSWindow)
    WordChoice1.set('Answer Here')
    WordDropdown1 = OptionMenu(mycanvas, WordChoice1, *choices).place(x=350,y=320)
    def change_dropdown1(*args):
        strike(WordChoice1.get())
        if WordChoice1.get() == "False" or WordChoice1.get() == "No" or WordChoice1.get() == "Never!":
            CheckCorrect[0] = True
        else:
            CheckCorrect[0] = False
    WordChoice1.trace('w', change_dropdown1)

    #QUESTION 2---
    text_canvas = mycanvas.create_text(25, 365, anchor = "nw", font=('Helvetica', 15), fill="white")
    mycanvas.itemconfig(text_canvas, text="Q2: If you are uncertain about something in the shop, it is okay to ask a peer. ->")
    WordChoice2 = StringVar(GSWindow)
    WordChoice2.set('Answer Here')
    WordDropdown2 = OptionMenu(mycanvas, WordChoice2, *choices).place(x=545,y=360)
    def change_dropdown2(*args):
        strike(WordChoice2.get())
        if WordChoice2.get()=="Yes" or WordChoice2.get()=="True":
            CheckCorrect[1]=True
        else:
            CheckCorrect[1]==False
    WordChoice2.trace('w', change_dropdown2)

    #QUESTION 3---
    text_canvas = mycanvas.create_text(25, 405, anchor = "nw", font=('Helvetica', 15), fill="white")
    mycanvas.itemconfig(text_canvas, text="Q3: Always get                                            from the instructor before using the drill press.")
    WordChoice3 = StringVar(GSWindow)
    WordChoice3.set('Answer Here')
    WordDropdown3 = OptionMenu(mycanvas, WordChoice3, *choices).place(x=140,y=400)
    def change_dropdown3(*args):
        strike(WordChoice3.get())
        if WordChoice3.get()=="Permission":
            CheckCorrect[2]=True
        else:
            CheckCorrect[2]=False
    WordChoice3.trace('w', change_dropdown3)

    #QUESTION 4---
    text_canvas = mycanvas.create_text(25, 445, anchor = "nw", font=('Helvetica', 15), fill="white")
    mycanvas.itemconfig(text_canvas, text="Q4: Students are not allowed to use equipment without having a safety                                       for that equipment")
    WordChoice4 = StringVar(GSWindow)
    WordChoice4.set('Answer Here')
    WordDropdown4 = OptionMenu(mycanvas, WordChoice4, *choices).place(x=490,y=440)
    def change_dropdown4(*args):
        strike(WordChoice4.get())
        if WordChoice4.get()=="Certificate":
            CheckCorrect[3]=True
        else:
            CheckCorrect[3]=False
    WordChoice4.trace('w', change_dropdown4)

    #QUESTION 5---
    text_canvas = mycanvas.create_text(25, 485, anchor = "nw", font=('Helvetica', 15), fill="white")
    mycanvas.itemconfig(text_canvas, text="Q5: Use a                                         when cutting small pieces on a bandsaw.")
    WordChoice5 = StringVar(GSWindow)
    WordChoice5.set('Answer Here')
    WordDropdown5 = OptionMenu(mycanvas, WordChoice5, *choices).place(x=100,y=480)
    def change_dropdown5(*args):
        strike(WordChoice5.get())
        if WordChoice5.get()=="Push Stick":
            CheckCorrect[4]=True
        else:
            CheckCorrect[4]=False
    WordChoice5.trace('w', change_dropdown5)


    #QUESTION 6---
    text_canvas = mycanvas.create_text(25, 525, anchor = "nw", font=('Helvetica', 15), fill="white")
    mycanvas.itemconfig(text_canvas, text="Q6: After use,                                        and return the tool to its proper place")
    WordChoice6 = StringVar(GSWindow)
    WordChoice6.set('Answer Here')
    WordDropdown6 = OptionMenu(mycanvas, WordChoice6, *choices).place(x=120,y=520)
    def change_dropdown6(*args):
        strike(WordChoice6.get())
        if WordChoice6.get()=="Clean":
            CheckCorrect[5]=True
        else:
            CheckCorrect[5]=False
    WordChoice6.trace('w', change_dropdown6)


    #QUESTION 7---
    text_canvas = mycanvas.create_text(25, 565, anchor = "nw", font=('Helvetica', 15), fill="white")
    mycanvas.itemconfig(text_canvas, text="Q7: This is a filler text")
    WordChoice7 = StringVar(GSWindow)
    WordChoice7.set('Answer Here')
    WordDropdown7 = OptionMenu(mycanvas, WordChoice7, *choices).place(x=490,y=560)
    def change_dropdown7(*args):
        strike(WordChoice7.get())
        if WordChoice7.get()=="XXX":
            CheckCorrect[6]=True
        else:
            CheckCorrect[6]=False
    WordChoice7.trace('w', change_dropdown7)


    #QUESTION 8---
    text_canvas = mycanvas.create_text(25, 605, anchor = "nw", font=('Helvetica', 15), fill="white")
    mycanvas.itemconfig(text_canvas, text="Q8: It is okay to bring a drink into the shop as long as none of the equipment is running. ->")
    WordChoice8 = StringVar(GSWindow)
    WordChoice8.set('Answer Here')
    WordDropdown8 = OptionMenu(mycanvas, WordChoice8, *choices).place(x=615,y=600)
    def change_dropdown8(*args):
        strike(WordChoice8.get())
        if WordChoice8.get()=="No" or WordChoice8.get()=="False" or WordChoice8.get()=="Never!":
            CheckCorrect[7]=True
        else:
            CheckCorrect[7]=False
    WordChoice8.trace('w', change_dropdown8)


    #QUESTION 9---
    text_canvas = mycanvas.create_text(25, 645, anchor = "nw", font=('Helvetica', 15), fill="white")
    mycanvas.itemconfig(text_canvas, text="Q9: Once you have received your equipment certification you may use the equipment any time without permission. ->")
    WordChoice9 = StringVar(GSWindow)
    WordChoice9.set('Answer Here')
    WordDropdown9 = OptionMenu(mycanvas, WordChoice9, *choices).place(x=785,y=640)
    def change_dropdown9(*args):
        strike(WordChoice9.get())
        if WordChoice9.get()=="No"or WordChoice9.get()=="False" or WordChoice9.get()=="Never!":
            CheckCorrect[8]=True
        else:
            CheckCorrect[8]=False
    WordChoice9.trace('w', change_dropdown9)


    #QUESTION 10---
    text_canvas = mycanvas.create_text(25, 685, anchor = "nw", font=('Helvetica', 15), fill="white")
    mycanvas.itemconfig(text_canvas, text="Q10:                                       the tool/machine before replacing broken, dull or damaged bits or blades.")
    WordChoice10 = StringVar(GSWindow)
    WordChoice10.set('Answer Here')
    WordDropdown10 = OptionMenu(mycanvas, WordChoice10, *choices).place(x=65,y=680)
    def change_dropdown10(*args):
        strike(WordChoice10.get())
        if WordChoice10.get()=="Unplug":
            CheckCorrect[9]=True
        else:
            CheckCorrect[9]=False
    WordChoice10.trace('w', change_dropdown10)

    #SUBMITBUTTON---
    def GetResult():
        GSWindow.destroy()
        GenResult.ReturnMark(CheckCorrect)
    Button(mycanvas, text="Submit Answers", command=GetResult).place(x=850,y=700)

    GSWindow.mainloop()
