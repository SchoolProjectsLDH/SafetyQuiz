from sys import version_info
import GenResult
if version_info.major == 2:
    from Tkinter import *
elif version_info.major == 3:
    from tkinter import *

def GSQuiz():
    choices = ["Yes", "Clean", "Push Stick", "No", "Unplug", "False", "Permission", "XXX", "Certificate", "Never!"]
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
            yPos=175
    for x in range(len(choices)):
        cross.append("")

    def strike(selected):
        sIndex=choices.index(selected)
        cross[sIndex]=mycanvas.create_line(lPos[0][sIndex],(lPos[1][sIndex]+lPos[3][sIndex])/2,lPos[2][sIndex],(lPos[1][sIndex]+lPos[3][sIndex])/2,width='3',fill='white')

        for iteration in range(0,10):
            if WordChoice1.get() != choices[iteration] and WordChoice2.get() != choices[iteration] and WordChoice3.get() != choices[iteration] and WordChoice4.get() != choices[iteration] and WordChoice5.get() != choices[iteration] and WordChoice6.get() != choices[iteration] and WordChoice7.get() != choices[iteration] and WordChoice8.get() != choices[iteration] and WordChoice9.get() != choices[iteration] and WordChoice10.get() != choices[iteration] and cross[iteration]!="":
                mycanvas.delete(cross[iteration])
    dbPos=[[],[]]
    def boxPositioning(x,y,text,bDB):
        space=5
        qxPos=x
        qyPos=y
        q1="Q1: Minor injuries do not need to be reported. -> "
        used=False

        for word in text.split(" "):

            question=mycanvas.create_text(qxPos,qyPos,text=word, anchor = "nw", font=('Helvetica', 15), fill="white")
            qbox=mycanvas.bbox(question)
            qxPos=qbox[2]+space

            if (str(word) == str(bDB) and used==False):
                dbPos[0]=qbox[2]+space
                dbPos[1]=qbox[1]
                used=True

    #QUESTION 1---
    boxPositioning(25,325,"Q1: Minor injuries do not need to be reported. -> ","->")

    #text_canvas = mycanvas.create_text(25, 325, anchor = "nw", font=('Helvetica', 15), fill="white")
    #mycanvas.itemconfig(text_canvas, text="Q1: Minor injuries do not need to be reported. ->")
    WordChoice1 = StringVar(GSWindow)
    WordChoice1.set('Answer Here')
    WordDropdown1 = OptionMenu(mycanvas, WordChoice1, *choices).place(x=dbPos[0],y=dbPos[1])
    def change_dropdown1(*args):
        print( WordChoice1.get() )
        strike(WordChoice1.get())
        if WordChoice1.get() == "False" or WordChoice1.get() == "No" or WordChoice1.get() == "Never!":
            CheckCorrect[0] = True
            print(CheckCorrect)
        else:
            CheckCorrect[0] = False
            print(CheckCorrect)

    WordChoice1.trace('w', change_dropdown1)


    #QUESTION 2---
    boxPositioning(25,365,"Q2: If you are uncertain about something in the shop, it is okay to ask a peer. ->","->")
    #text_canvas = mycanvas.create_text(25, 365, anchor = "nw", font=('Helvetica', 15), fill="white")
    #mycanvas.itemconfig(text_canvas, text="Q2: If you are uncertain about something in the shop, it is okay to ask a peer. ->")
    WordChoice2 = StringVar(GSWindow)
    WordChoice2.set('Answer Here')
    WordDropdown2 = OptionMenu(mycanvas, WordChoice2, *choices).place(x=dbPos[0],y=dbPos[1])
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
    boxPositioning(25,405,"Q3: Always get                      from the instructor before using the drill press.","get")
    WordChoice3 = StringVar(GSWindow)
    WordChoice3.set('Answer Here')
    WordDropdown3 = OptionMenu(mycanvas, WordChoice3, *choices).place(x=dbPos[0],y=dbPos[1])
    def change_dropdown3(*args):
        print( WordChoice3.get() )
        strike(WordChoice3.get())
        if WordChoice3.get()=="Permission":
            CheckCorrect[2]=True
            print(CheckCorrect)
        else:
            CheckCorrect[2]=False
            print(CheckCorrect)
    WordChoice3.trace('w', change_dropdown3)

    #QUESTION 4---
    boxPositioning(25,445,"Q4: Students are not allowed to use equipment without having a safety                                       for that equipment","safety")
    WordChoice4 = StringVar(GSWindow)
    WordChoice4.set('Answer Here')
    WordDropdown4 = OptionMenu(mycanvas, WordChoice4, *choices).place(x=dbPos[0],y=dbPos[1])
    def change_dropdown4(*args):
        print( WordChoice4.get() )
        strike(WordChoice4.get())
        if WordChoice4.get()=="Certificate":
            CheckCorrect[3]=True
            print(CheckCorrect)
        else:
            CheckCorrect[3]=False
            print(CheckCorrect)
    WordChoice4.trace('w', change_dropdown4)

    #QUESTION 5---
    boxPositioning(25,485,"Q5: Use a                                       when cutting small pieces on a bandsaw.","a")
    WordChoice5 = StringVar(GSWindow)
    WordChoice5.set('Answer Here')
    WordDropdown5 = OptionMenu(mycanvas, WordChoice5, *choices).place(x=dbPos[0],y=dbPos[1])
    def change_dropdown5(*args):
        print( WordChoice5.get() )
        strike(WordChoice5.get())
        if WordChoice5.get()=="Push Stick":
            CheckCorrect[4]=True
            print(CheckCorrect)
        else:
            CheckCorrect[4]=False
            print(CheckCorrect)
    WordChoice5.trace('w', change_dropdown5)


    #QUESTION 6---
    boxPositioning(25,525,"Q6: After use,                                        and return the tool to its proper place","use,")
    WordChoice6 = StringVar(GSWindow)
    WordChoice6.set('Answer Here')
    WordDropdown6 = OptionMenu(mycanvas, WordChoice6, *choices).place(x=dbPos[0],y=dbPos[1])
    def change_dropdown6(*args):
        print( WordChoice6.get() )
        strike(WordChoice6.get())
        if WordChoice6.get()=="Clean":
            CheckCorrect[5]=True
            print(CheckCorrect)
        else:
            CheckCorrect[5]=False
            print(CheckCorrect)
    WordChoice6.trace('w', change_dropdown6)


    #QUESTION 7---
    boxPositioning(25,565,"Q7: This is a filler text","text")
    WordChoice7 = StringVar(GSWindow)
    WordChoice7.set('Answer Here')
    WordDropdown7 = OptionMenu(mycanvas, WordChoice7, *choices).place(x=dbPos[0],y=dbPos[1])
    def change_dropdown7(*args):
        print( WordChoice7.get() )
        strike(WordChoice7.get())
        if WordChoice7.get()=="XXX":
            CheckCorrect[6]=True
            print(CheckCorrect)
        else:
            CheckCorrect[6]=False
            print(CheckCorrect)
    WordChoice7.trace('w', change_dropdown7)


    #QUESTION 8---
    boxPositioning(25,605,"Q8: It is okay to bring a drink into the shop as long as none of the equipment is running. ->","->")
    WordChoice8 = StringVar(GSWindow)
    WordChoice8.set('Answer Here')
    WordDropdown8 = OptionMenu(mycanvas, WordChoice8, *choices).place(x=dbPos[0],y=dbPos[1])
    def change_dropdown8(*args):
        print( WordChoice8.get() )
        strike(WordChoice8.get())
        if WordChoice8.get()=="No" or WordChoice8.get()=="False" or WordChoice8.get()=="Never!":
            CheckCorrect[7]=True
            print(CheckCorrect)
        else:
            CheckCorrect[7]=False
            print(CheckCorrect)
    WordChoice8.trace('w', change_dropdown8)


    #QUESTION 9---
    boxPositioning(25,645,"Q9: Once you have received your equipment certification you may use the equipment any time without permission. ->","->")
    WordChoice9 = StringVar(GSWindow)
    WordChoice9.set('Answer Here')
    WordDropdown9 = OptionMenu(mycanvas, WordChoice9, *choices).place(x=dbPos[0],y=dbPos[1])
    def change_dropdown9(*args):
        print( WordChoice9.get() )
        strike(WordChoice9.get())
        if WordChoice9.get()=="No"or WordChoice9.get()=="False" or WordChoice9.get()=="Never!":
            CheckCorrect[8]=True
            print(CheckCorrect)
        else:
            CheckCorrect[8]=False
            print(CheckCorrect)
    WordChoice9.trace('w', change_dropdown9)


    #QUESTION 10---
    boxPositioning(25,685,"Q10:                                       the tool/machine before replacing broken, dull or damaged bits or blades.","Q10:")
    WordChoice10 = StringVar(GSWindow)
    WordChoice10.set('Answer Here')
    WordDropdown10 = OptionMenu(mycanvas, WordChoice10, *choices).place(x=dbPos[0],y=dbPos[1])
    def change_dropdown10(*args):
        print( WordChoice10.get() )
        strike(WordChoice10.get())
        if WordChoice10.get()=="Unplug":
            CheckCorrect[9]=True
            print(CheckCorrect)
        else:
            CheckCorrect[9]=False
            print(CheckCorrect)
    WordChoice10.trace('w', change_dropdown10)

    #SUBMITBUTTON---
    def GetResult():
        GSWindow.destroy()
        GenResult.ReturnMark(CheckCorrect)
    #SubButton = PhotoImage(file = "Images/Submit.gif") --Not working
    Button(mycanvas, text="Submit Answers", command=GetResult).place(x=850,y=700)

    GSWindow.mainloop()
