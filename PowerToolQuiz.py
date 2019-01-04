import PowResult
from sys import version_info
if version_info.major == 2:
    from Tkinter import *
elif version_info.major == 3:
    from tkinter import *

def PTQuiz():
    choices = ["Jewelery","Long","Kickbacks","Angular","Front","Side","Speed","Grab","Pull","Machine","Waste","Lock Out","Break","Bind"]
    CheckCorrect = [False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    print("Power tool quiz")
    PTWindow=Tk()
    PTWindow.title("Power Tool Quiz")
    PTWindow.geometry("1000x800")
    PTWindow.resizable(False,False)
    mycanvas = Canvas(PTWindow, width = 1000, height = 800)
    mycanvas.create_rectangle(0, 0, 1000, 8000, fill = "#38761d")
    mycanvas.pack(side = "top", fill = "both", expand = True)

    #title
    title=Label(mycanvas,text="Power Tool Safety",font=("Helvetica",30),bg="#38761d",fg="white")
    title.place(x=350,y=10)

    #alternate wordbank
        #the box
    xPos=125
    yPos=100
    choicePos=[[],[]]
    side1=mycanvas.create_line(25,75,25,250,width="3",fill="white")
    side2=mycanvas.create_line(25,250,975,250,width="3",fill="white")
    side3=mycanvas.create_line(975,250,975,75,width="3",fill="white")
    side4=mycanvas.create_line(975,75,25,75,width="3",fill="white")
        #printing the words

    cross=[]
    lPos=[[],[],[],[]] #letter position
    #xsPos ysPos xePos yePos
    #s is start e is end
    for x in range (len(choices)):
        op=mycanvas.create_text(xPos,yPos,text=choices[x],font=('Helvetica', 15),fill="white")
        bbox=mycanvas.bbox(op)
        for y in range (4):
            lPos[y].append(bbox[y])
        xPos=xPos+185
        if x==4:
            xPos=125
            yPos=150
        if x==9:
            xPos=125
            yPos=200
    for x in range(len(choices)):
        cross.append("")

    def strike(selected):
        sIndex=choices.index(selected)
        cross[sIndex]=mycanvas.create_line(lPos[0][sIndex],(lPos[1][sIndex]+lPos[3][sIndex])/2,lPos[2][sIndex],(lPos[1][sIndex]+lPos[3][sIndex])/2,width='3',fill='white')

        for iteration in range(0,10):
            if WordChoice1.get() != choices[iteration] and WordChoice2.get() != choices[iteration] and WordChoice3.get() != choices[iteration] and WordChoice4.get() != choices[iteration] and WordChoice5.get() != choices[iteration] and WordChoice6.get() != choices[iteration] and WordChoice7.get() != choices[iteration] and WordChoice8.get() != choices[iteration] and WordChoice9.get() != choices[iteration] and WordChoice10.get() != choices[iteration] and cross[iteration]!="":
                mycanvas.delete(cross[iteration])

    #QUESTION 1---
    text_canvas = mycanvas.create_text(25, 285, anchor = "nw", font=('Helvetica', 15), fill="white")
    mycanvas.itemconfig(text_canvas, text="Q1: Remove all                    and tie back                    hair")
    WordChoice1 = StringVar(PTWindow)
    WordChoice1.set('Answer Here')
    WordDropdown1 = OptionMenu(mycanvas, WordChoice1, *choices).place(x=165,y=280)

    def change_dropdown1(*args):
        print( WordChoice1.get() )
        strike(WordChoice1.get())
        if WordChoice1.get() == "Jewelery":
            CheckCorrect[0] = True
            print(CheckCorrect)
        else:
            CheckCorrect[0] = False
            print(CheckCorrect)

    WordChoice1.trace('w', change_dropdown1)

    #QUESTION 1 box 2---
    WordChoice2 = StringVar(PTWindow)
    WordChoice2.set('Answer Here')
    WordDropdown2 = OptionMenu(mycanvas, WordChoice2, *choices).place(x=390,y=280)
    def change_dropdown2(*args):
        print( WordChoice2.get() )
        strike(WordChoice2.get())

        if WordChoice2.get()=="Long":
            CheckCorrect[1]=True
            print(CheckCorrect)
        else:
            CheckCorrect[1]==False
            print(CheckCorrect)
    WordChoice2.trace('w', change_dropdown2)


    #QUESTION 2---
    text_canvas = mycanvas.create_text(25, 325, anchor = "nw", font=('Helvetica', 15), fill="white")
    mycanvas.itemconfig(text_canvas, text="Q2: Watch for                       when cutting small pieces")
    WordChoice3 = StringVar(PTWindow)
    WordChoice3.set('Answer Here')
    WordDropdown3 = OptionMenu(mycanvas, WordChoice3, *choices).place(x=160,y=320)
    def change_dropdown3(*args):
        print( WordChoice3.get() )
        strike(WordChoice3.get())
        if WordChoice3.get()=="Kickbacks":
            CheckCorrect[2]=True
            print(CheckCorrect)
        else:
            CheckCorrect[2]=False
            print(CheckCorrect)
    WordChoice3.trace('w', change_dropdown3)

    #QUESTION 3---
    text_canvas = mycanvas.create_text(25, 365, anchor = "nw", font=('Helvetica', 15), fill="white")
    mycanvas.itemconfig(text_canvas, text="Q3: When making                        cuts ensure the blade has adequate clearance")
    WordChoice4 = StringVar(PTWindow)
    WordChoice4.set('Answer Here')
    WordDropdown4 = OptionMenu(mycanvas, WordChoice4, *choices).place(x=200,y=360)
    def change_dropdown4(*args):
        print( WordChoice4.get() )
        strike(WordChoice4.get())
        if WordChoice4.get()=="Angular":
            CheckCorrect[3]=True
            print(CheckCorrect)
        else:
            CheckCorrect[3]=False
            print(CheckCorrect)
    WordChoice4.trace('w', change_dropdown4)

    #QUESTION 4---
    text_canvas = mycanvas.create_text(25, 405, anchor = "nw", font=('Helvetica', 15), fill="white")
    #
    mycanvas.itemconfig(text_canvas, text="Q4: Always Operate the drill press from the                       ,never from the                         ")
    WordChoice5 = StringVar(PTWindow)
    WordChoice5.set('Answer Here')
    WordDropdown5 = OptionMenu(mycanvas, WordChoice5, *choices).place(x=425,y=400)
    def change_dropdown5(*args):
        print( WordChoice5.get() )
        strike(WordChoice5.get())
        if WordChoice5.get()=="Front":
            CheckCorrect[4]=True
            print(CheckCorrect)
        else:
            CheckCorrect[4]=False
            print(CheckCorrect)
    WordChoice5.trace('w', change_dropdown5)

    WordChoice6 = StringVar(PTWindow)
    WordChoice6.set('Answer Here')
    WordDropdown6 = OptionMenu(mycanvas, WordChoice6, *choices).place(x=700,y=400)
    def change_dropdown6(*args):
        print( WordChoice6.get() )
        strike(WordChoice6.get())
        if WordChoice6.get()=="Side":
            CheckCorrect[5]=True
            print(CheckCorrect)
        else:
            CheckCorrect[5]=False
            print(CheckCorrect)
    WordChoice6.trace('w', change_dropdown6)

    #QUESTION 6---
    text_canvas = mycanvas.create_text(25, 445, anchor = "nw", font=('Helvetica', 15), fill="white")
    mycanvas.itemconfig(text_canvas, text="Q5: Check for the proper for the proper                      for the drill size and material you are working on")
    WordChoice7 = StringVar(PTWindow)
    WordChoice7.set('Answer Here')
    WordDropdown7 = OptionMenu(mycanvas, WordChoice7, *choices).place(x=380,y=440)
    def change_dropdown7(*args):
        print( WordChoice7.get() )
        strike(WordChoice7.get())
        if WordChoice7.get()=="Speed":
            CheckCorrect[6]=True
            print(CheckCorrect)
        else:
            CheckCorrect[6]=False
            print(CheckCorrect)
    WordChoice7.trace('w', change_dropdown7)

    #QUESTION 7---
    text_canvas = mycanvas.create_text(25, 485, anchor = "nw", font=('Helvetica', 15), fill="white")

    mycanvas.itemconfig(text_canvas, text="Q6: Never attempt to                     a piece if it slips from the clamp")
    WordChoice8 = StringVar(PTWindow)
    WordChoice8.set('Answer Here')
    WordDropdown8 = OptionMenu(mycanvas, WordChoice8, *choices).place(x=220,y=480)
    def change_dropdown8(*args):
        print( WordChoice8.get() )
        strike(WordChoice8.get())
        if WordChoice8.get()=="Grab":
            CheckCorrect[7]=True
            print(CheckCorrect)
        else:
            CheckCorrect[7]=False
            print(CheckCorrect)
    WordChoice8.trace('w', change_dropdown8)


    #QUESTION 8---

    text_canvas = mycanvas.create_text(25, 525, anchor = "nw", font=('Helvetica', 15), fill="white")
    mycanvas.itemconfig(text_canvas, text="Q7: Never                        or force a japped pice through the equiplment. Shut the                      off and dislodge the")
    text_canvas = mycanvas.create_text(25, 565, anchor = "nw", font=('Helvetica', 15), fill="white")
    mycanvas.itemconfig(text_canvas, text="piece")
    WordChoice9 = StringVar(PTWindow)
    WordChoice9.set('Answer Here')
    WordDropdown9 = OptionMenu(mycanvas, WordChoice9, *choices).place(x=125,y=520)
    def change_dropdown9(*args):
        print( WordChoice9.get() )
        strike(WordChoice9.get())
        if WordChoice9.get()=="Pull":
            CheckCorrect[8]=True
            print(CheckCorrect)
        else:
            CheckCorrect[8]=False
            print(CheckCorrect)
    WordChoice9.trace('w', change_dropdown9)
    WordChoice10 = StringVar(PTWindow)
    WordChoice10.set('Answer Here')
    WordDropdown10 = OptionMenu(mycanvas, WordChoice10, *choices).place(x=755,y=520)
    def change_dropdown10(*args):
        print( WordChoice10.get() )
        strike(WordChoice10.get())
        if WordChoice10.get()=="Machine":
            CheckCorrect[9]=True
            print(CheckCorrect)
        else:
            CheckCorrect[9]=False
            print(CheckCorrect)
    WordChoice10.trace('w', change_dropdown10)
    #QUESTION 9---

    text_canvas = mycanvas.create_text(25, 605, anchor = "nw", font=('Helvetica', 15), fill="white")
    mycanvas.itemconfig(text_canvas, text="Q8: When cutting with the band saw, the blade should cut on the                       side of the work piece ")
    WordChoice11 = StringVar(PTWindow)
    WordChoice11.set('Answer Here')
    WordDropdown11 = OptionMenu(mycanvas, WordChoice11, *choices).place(x=595,y=600)
    def change_dropdown11(*args):
        print( WordChoice11.get() )
        strike(WordChoice11.get())
        if WordChoice11.get()=="Waste":
            CheckCorrect[10]=True
            print(CheckCorrect)
        else:
            CheckCorrect[10]=False
            print(CheckCorrect)
    WordChoice11.trace('w', change_dropdown11)


    #QUESTION 10---
    text_canvas = mycanvas.create_text(25, 645, anchor = "nw", font=('Helvetica', 15), fill="white")
    mycanvas.itemconfig(text_canvas, text="Q9:Use the                       when changing blades")
    WordChoice12 = StringVar(PTWindow)
    WordChoice12.set('Answer Here')
    WordDropdown12 = OptionMenu(mycanvas, WordChoice12, *choices).place(x=135,y=640)
    def change_dropdown12(*args):
        print( WordChoice12.get() )
        strike(WordChoice12.get())
        if WordChoice12.get()=="Lock Out":
            CheckCorrect[11]=True
            print(CheckCorrect)
        else:
            CheckCorrect[11]=False
            print(CheckCorrect)
    WordChoice12.trace('w', change_dropdown12)

    text_canvas = mycanvas.create_text(25, 685, anchor = "nw", font=('Helvetica', 15), fill="white")    #SUBMITBUTTON---
    mycanvas.itemconfig(text_canvas, text="Q10When using the band saw, plan your cuts carefully. Saw curves gravdually. Sudden twist will cause the" )
    text_canvas = mycanvas.create_text(25, 725, anchor = "nw", font=('Helvetica', 15), fill="white")
    mycanvas.itemconfig(text_canvas, text="blade to                    or                  ")
    WordChoice13 = StringVar(PTWindow)
    WordChoice13.set('Answer Here')
    WordDropdown13 = OptionMenu(mycanvas, WordChoice13, *choices).place(x=100,y=720)
    def change_dropdown13(*args):
        print( WordChoice13.get() )
        strike(WordChoice13.get())
        if WordChoice13.get()=="Break":
            CheckCorrect[12]=True
            print(CheckCorrect)
        else:
            CheckCorrect[12]=False
            print(CheckCorrect)
    WordChoice13.trace('w', change_dropdown13)

    WordChoice14 = StringVar(PTWindow)
    WordChoice14.set('Answer Here')
    WordDropdown14 = OptionMenu(mycanvas, WordChoice14, *choices).place(x=240,y=720)
    def change_dropdown14(*args):
        print( WordChoice14.get() )
        strike(WordChoice14.get())
        if WordChoice14.get()=="Bind":
            CheckCorrect[13]=True
            print(CheckCorrect)
        else:
            CheckCorrect[13]=False
            print(CheckCorrect)
    WordChoice14.trace('w', change_dropdown14)


    def GetResult():
        PTWindow.destroy()
        PowResult.ReturnMark(CheckCorrect)
    #SubButton = PhotoImage(file = "Images/Submit.gif") --Not working
    Button(mycanvas, text="Submit Answers", command=GetResult).place(x=850,y=720)
    PTWindow.mainloop()
