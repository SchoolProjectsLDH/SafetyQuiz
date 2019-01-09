from sys import version_info
if version_info.major == 2:
    from Tkinter import *
elif version_info.major == 3:
    from tkinter import *
import HandToolResult

def HTQuiz():
    cross=[]
    lPos=[[],[],[],[]] #letter position
    backgroundcolour = "#3A3A8E"
    dbPos=[[],[]]
    choices = ["Sharp", "Grab", "False", "Offset Screwdriver", "Face", "Robertson", "True", "Yes", "Drawer", "Glancing"]
    CheckCorrect = [False,False,False,False,False,False,False,False,False,False]
    HTWindow=Tk()
    HTWindow.title("Hand Tool Quiz")
    HTWindow.geometry("1000x800")
    HTWindow.resizable(False,False)

    HTcanvas = Canvas(HTWindow, width = 1000, height = 800)
    HTcanvas.create_rectangle(0, 0, 1000, 8000, fill = backgroundcolour)
    HTcanvas.pack(side = "top", fill = "both", expand = True)

    #title
    title=Label(HTcanvas,text="Hand Tools",font=("Helvetica",30),bg=backgroundcolour,fg="white").place(x=500,y=25, anchor = CENTER)

    #wordbank
    xPos=125
    yPos=100
    choicePos=[[],[]]
    side1=HTcanvas.create_line(25,75,25,250,width="3",fill="white")
    side2=HTcanvas.create_line(25,250,975,250,width="3",fill="white")
    side3=HTcanvas.create_line(975,250,975,75,width="3",fill="white")
    side4=HTcanvas.create_line(975,75,25,75,width="3",fill="white")

    #xsPos ysPos xePos yePos
    #s is start e is end
    for x in range (len(choices)):
        op=HTcanvas.create_text(xPos,yPos,text=choices[x],font=('Helvetica', 15),fill="white")
        bbox=HTcanvas.bbox(op)
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
        if(cross[sIndex]==""):
            cross[sIndex]=HTcanvas.create_line(lPos[0][sIndex],(lPos[1][sIndex]+lPos[3][sIndex])/2,lPos[2][sIndex],(lPos[1][sIndex]+lPos[3][sIndex])/2,width='3',fill='white')

        for iteration in range(0,10):
            if WordChoice1.get() != choices[iteration] and WordChoice2.get() != choices[iteration] and WordChoice3.get() != choices[iteration] and WordChoice4.get() != choices[iteration] and WordChoice5.get() != choices[iteration] and WordChoice6.get() != choices[iteration] and WordChoice7.get() != choices[iteration] and WordChoice8.get() != choices[iteration] and WordChoice9.get() != choices[iteration] and WordChoice10.get() != choices[iteration] and cross[iteration]!="":
                HTcanvas.delete(cross[iteration])
                cross[iteration]=""


    def boxPositioning(x,y,text,bDB):
        space=5
        qxPos=x
        qyPos=y
        q1="Q1: Minor injuries do not need to be reported. -> "
        used=False

        for word in text.split(" "):
            question=HTcanvas.create_text(qxPos,qyPos,text=word, anchor = "nw", font=('Helvetica', 15), fill="white")
            qbox=HTcanvas.bbox(question)
            qxPos=qbox[2]+space
            if (str(word) == str(bDB) and used==False):
                dbPos[0]=qbox[2]+space
                dbPos[1]=qbox[1]
                used=True

    #QUESTION 1---
    boxPositioning(25, 325,"Q1: You should use a long throat clamp instead of a deep throat clamp. ->","->")
    WordChoice1 = StringVar(HTWindow)
    WordChoice1.set('Answer Here          ')
    WordDropdown1 = OptionMenu(HTcanvas, WordChoice1, *choices).place(x=dbPos[0],y=dbPos[1])
    def change_dropdown1(*args):
        strike(WordChoice1.get())
        if WordChoice1.get() == "False" or WordChoice1.get() == "No":
            CheckCorrect[0] = True
        else:
            CheckCorrect[0] = False

    WordChoice1.trace('w', change_dropdown1)

    #QUESTION 2---
    boxPositioning(25, 365,"Q2: Without padding, a clamp can leave marks on your work ->","->")
    WordChoice2 = StringVar(HTWindow)
    WordChoice2.set('Answer Here          ')
    WordDropdown2 = OptionMenu(HTcanvas, WordChoice2, *choices).place(x=dbPos[0],y=dbPos[1])
    def change_dropdown2(*args):
        strike(WordChoice2.get())
        if WordChoice2.get()=="Yes" or WordChoice2.get()=="True":
            CheckCorrect[1]=True
        else:
            CheckCorrect[1]==False
    WordChoice2.trace('w', change_dropdown2)

    #QUESTION 3---
    boxPositioning(25, 405,"Q3: We store C clamps in the                               .","the")
    WordChoice3 = StringVar(HTWindow)
    WordChoice3.set('Answer Here          ')
    WordDropdown3 = OptionMenu(HTcanvas, WordChoice3, *choices).place(x=dbPos[0],y=dbPos[1])
    def change_dropdown3(*args):
        strike(WordChoice3.get())
        if WordChoice3.get()=="Drawer":
            CheckCorrect[2]=True
        else:
            CheckCorrect[2]=False
    WordChoice3.trace('w', change_dropdown3)

    #QUESTION 4---
    boxPositioning(25, 445,"Q4: For hammers, you should use the                               to hit an object","the")
    WordChoice4 = StringVar(HTWindow)
    WordChoice4.set('Answer Here          ')
    WordDropdown4 = OptionMenu(HTcanvas, WordChoice4, *choices).place(x=dbPos[0],y=dbPos[1])
    def change_dropdown4(*args):
        strike(WordChoice4.get())
        if WordChoice4.get()=="Face":
            CheckCorrect[3]=True
        else:
            CheckCorrect[3]=False
    WordChoice4.trace('w', change_dropdown4)

    #QUESTION 5---
    boxPositioning(25, 485,"Q5: For a hammer, You should avoid                               blows when hitting an object.","avoid")
    WordChoice5 = StringVar(HTWindow)
    WordChoice5.set('Answer Here          ')
    WordDropdown5 = OptionMenu(HTcanvas, WordChoice5, *choices).place(x=dbPos[0],y=dbPos[1])
    def change_dropdown5(*args):
        strike(WordChoice5.get())
        if WordChoice5.get()=="Glancing":
            CheckCorrect[4]=True
        else:
            CheckCorrect[4]=False
    WordChoice5.trace('w', change_dropdown5)

    #QUESTION 6---
    boxPositioning(25, 525,"Q6: The square head screwdriver is called a:","a:")
    WordChoice6 = StringVar(HTWindow)
    WordChoice6.set('Answer Here          ')
    WordDropdown6 = OptionMenu(HTcanvas, WordChoice6, *choices).place(x=dbPos[0],y=dbPos[1])
    def change_dropdown6(*args):
        strike(WordChoice6.get())
        if WordChoice6.get()=="Robertson":
            CheckCorrect[5]=True
        else:
            CheckCorrect[5]=False
    WordChoice6.trace('w', change_dropdown6)

    #QUESTION 7---
    boxPositioning(25, 565,"Q7: You should use an                               in tight areas","an")
    WordChoice7 = StringVar(HTWindow)
    WordChoice7.set('Answer Here          ')
    WordDropdown7 = OptionMenu(HTcanvas, WordChoice7, *choices).place(x=dbPos[0],y=dbPos[1])
    def change_dropdown7(*args):
        strike(WordChoice7.get())
        if WordChoice7.get()=="Offset Screwdriver":
            CheckCorrect[6]=True
        else:
            CheckCorrect[6]=False
    WordChoice7.trace('w', change_dropdown7)

    #QUESTION 8---
    boxPositioning(25, 605,"Q8: You should use a                               blade when cutting","a")
    WordChoice8 = StringVar(HTWindow)
    WordChoice8.set('Answer Here          ')
    WordDropdown8 = OptionMenu(HTcanvas, WordChoice8, *choices).place(x=dbPos[0],y=dbPos[1])
    def change_dropdown8(*args):
        strike(WordChoice8.get())
        if WordChoice8.get()=="Sharp":
            CheckCorrect[7]=True
        else:
            CheckCorrect[7]=False
    WordChoice8.trace('w', change_dropdown8)

    #QUESTION 9---
    boxPositioning(25, 645,"Q9: Do not                               a falling knife","not")
    WordChoice9 = StringVar(HTWindow)
    WordChoice9.set('Answer Here          ')
    WordDropdown9 = OptionMenu(HTcanvas, WordChoice9, *choices).place(x=dbPos[0],y=dbPos[1])
    def change_dropdown9(*args):
        strike(WordChoice9.get())
        if WordChoice9.get()=="Grab":
            CheckCorrect[8]=True
        else:
            CheckCorrect[8]=False
    WordChoice9.trace('w', change_dropdown9)

    #QUESTION 10---
    boxPositioning(25, 685,"Q10: You can leave hot glue guns unattended if unplugged. ->","->")
    WordChoice10 = StringVar(HTWindow)
    WordChoice10.set('Answer Here          ')
    WordDropdown10 = OptionMenu(HTcanvas, WordChoice10, *choices).place(x=dbPos[0],y=dbPos[1])
    def change_dropdown10(*args):
        strike(WordChoice10.get())
        if WordChoice10.get()=="Yes" or WordChoice10.get()=="True":
            CheckCorrect[9]=True
        else:
            CheckCorrect[9]=False
    WordChoice10.trace('w', change_dropdown10)

    #SUBMITBUTTON---
    def GetHTResult():
        HTWindow.destroy()
        HandToolResult.ReturnHTMark(CheckCorrect)
    Button(HTcanvas, text="Submit Answers", command=GetHTResult).place(x=850,y=700)
    HTWindow.mainloop()
