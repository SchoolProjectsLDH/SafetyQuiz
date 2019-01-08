import PowResult
from sys import version_info
if version_info.major == 2:
    from Tkinter import *
elif version_info.major == 3:
    from tkinter import *

def PTQuiz():
    choices = ["Jewelery","Long","Kickbacks","Angular","Front","Side","Speed","Grab","Pull","Machine","Waste","Lock Out","Break","Bind"]
    CheckCorrect = [False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    PTWindow=Tk()
    PTWindow.title("Power Tool Quiz")
    PTWindow.geometry("1000x800")
    PTWindow.resizable(False,False)
    PTcanvas = Canvas(PTWindow, width = 1000, height = 800)
    PTcanvas.create_rectangle(0, 0, 1000, 8000, fill = "black")
    PTcanvas.pack(side = "top", fill = "both", expand = True)

    #title
    title=Label(PTcanvas,text="Power Tool Safety",font=("Helvetica",30),bg="black",fg="white").place(x=500,y=25, anchor= CENTER)

    #WordBank
    xPos=125
    yPos=100
    choicePos=[[],[]]
    side1=PTcanvas.create_line(25,75,25,250,width="3",fill="white")
    side2=PTcanvas.create_line(25,250,975,250,width="3",fill="white")
    side3=PTcanvas.create_line(975,250,975,75,width="3",fill="white")
    side4=PTcanvas.create_line(975,75,25,75,width="3",fill="white")
    for x in range (0,5):
        op1=PTcanvas.create_text(xPos,yPos,text=choices[x],font=('Helvetica', 15),fill="white")
        choicePos[0].append(xPos)
        choicePos[1].append(yPos)
        xPos=xPos+185
    xPos = 125
    yPos = 175
    for x in range (5,10):
        op1=PTcanvas.create_text(xPos,yPos,text=choices[x],font=('Helvetica', 15),fill="white")
        choicePos[0].append(xPos)
        choicePos[1].append(yPos)
        xPos=xPos+185
    xPos = 125
    yPos = 220
    for x in range(10,14):
        op1=PTcanvas.create_text(xPos,yPos,text=choices[x],font=('Helvetica', 15),fill="white")
        choicePos[0].append(xPos)
        choicePos[1].append(yPos)
        xPos=xPos+185

    #Highlighting selected words function
    def strike(selected):
        op1=PTcanvas.create_text(choicePos[0][choices.index(selected)],choicePos[1][choices.index(selected)])
        for iteration in range(0,14):
            if WordChoice1.get() != choices[iteration] and WordChoice2.get() != choices[iteration] and WordChoice3.get() != choices[iteration] and WordChoice4.get() != choices[iteration] and WordChoice5.get() != choices[iteration] and WordChoice6.get() != choices[iteration] and WordChoice7.get() != choices[iteration] and WordChoice8.get() != choices[iteration] and WordChoice9.get() != choices[iteration] and WordChoice10.get() != choices[iteration] and WordChoice11.get() != choices[iteration] and WordChoice12.get() != choices[iteration] and WordChoice13.get() != choices[iteration] and WordChoice14.get() != choices[iteration]:
                PTcanvas.create_text(choicePos[0][choices.index(choices[iteration])],choicePos[1][choices.index(choices[iteration])],text=choices[choices.index(choices[iteration])],font=('Helvetica', 15),fill="white")
        op1=PTcanvas.create_text(choicePos[0][choices.index(selected)],choicePos[1][choices.index(selected)],text=choices[choices.index(selected)],font=('Helvetica', 15),fill="red")



    dbPos=[[],[]]
    def boxPositioning(x,y,text,bDB,bDB2,skip,skip2):
        space=5
        qxPos=x
        qyPos=y
        q1="Q1: Minor injuries do not need to be reported. -> "
        used=False
        used2=False
        tCount=0
        tCount2=0
        for word in text.split(" "):

            question=PTcanvas.create_text(qxPos,qyPos,text=word, anchor = "nw", font=('Helvetica', 15), fill="white")
            qbox=PTcanvas.bbox(question)
            qxPos=qbox[2]+space
            if (skip!=0 or skip2!=0):
                if(str(word)==str(bDB)and skip!=0):
                    tCount+=1
                if(str(word)==str(bDB2) and skip2!=0):
                    tCount2+=1

            if (str(word) == str(bDB) and used==False and tCount==skip):
                dbPos[0].append(qbox[2]+space)
                dbPos[1].append(qbox[1])
                used=True
            if (str(word)==str(bDB2) and used2==False and tCount2==skip2):
                dbPos[0].append(qbox[2]+space)
                dbPos[1].append(qbox[1])
                used2=True


    #QUESTION 1---
    boxPositioning(25,285,"Q1: Remove all                           and tie back                           hair","all","back",0,0)
    WordChoice1 = StringVar(PTWindow)
    WordChoice1.set('Answer Here')
    WordDropdown1 = OptionMenu(PTcanvas, WordChoice1, *choices).place(x=dbPos[0][0],y=dbPos[1][0])
    def change_dropdown1(*args):
        strike(WordChoice1.get())
        if WordChoice1.get() == "Jewelery":
            CheckCorrect[0] = True
        else:
            CheckCorrect[0] = False
    WordChoice1.trace('w', change_dropdown1)

    #QUESTION 1 box 2---
    WordChoice2 = StringVar(PTWindow)
    WordChoice2.set('Answer Here')
    WordDropdown2 = OptionMenu(PTcanvas, WordChoice2, *choices).place(x=dbPos[0][1],y=dbPos[1][1])
    def change_dropdown2(*args):
        strike(WordChoice2.get())
        if WordChoice2.get()=="Long":
            CheckCorrect[1]=True
        else:
            CheckCorrect[1]==False
    WordChoice2.trace('w', change_dropdown2)


    #QUESTION 2---
    boxPositioning(25,325,"Q2: Watch for                           when cutting small pieces","for","none",0,0)
    WordChoice3 = StringVar(PTWindow)
    WordChoice3.set('Answer Here')
    WordDropdown3 = OptionMenu(PTcanvas, WordChoice3, *choices).place(x=dbPos[0][2],y=dbPos[1][2])
    def change_dropdown3(*args):
        strike(WordChoice3.get())
        if WordChoice3.get()=="Kickbacks":
            CheckCorrect[2]=True
        else:
            CheckCorrect[2]=False
    WordChoice3.trace('w', change_dropdown3)

    #QUESTION 3---
    boxPositioning(25,365,"Q3: When making                           cuts ensure the blade has adequate clearance","making","none",0,0)
    WordChoice4 = StringVar(PTWindow)
    WordChoice4.set('Answer Here')
    WordDropdown4 = OptionMenu(PTcanvas, WordChoice4, *choices).place(x=dbPos[0][3],y=dbPos[1][3])
    def change_dropdown4(*args):
        strike(WordChoice4.get())
        if WordChoice4.get()=="Angular":
            CheckCorrect[3]=True
        else:
            CheckCorrect[3]=False
    WordChoice4.trace('w', change_dropdown4)

    #QUESTION 4---
    boxPositioning(25,405,"Q4: Always operate the drill press from the                           ,never from the                           ","the","the",2,3)
    text_canvas = PTcanvas.create_text(25, 405, anchor = "nw", font=('Helvetica', 15), fill="white")
    WordChoice5 = StringVar(PTWindow)
    WordChoice5.set('Answer Here')
    WordDropdown5 = OptionMenu(PTcanvas, WordChoice5, *choices).place(x=dbPos[0][4],y=dbPos[1][4])
    def change_dropdown5(*args):
        strike(WordChoice5.get())
        if WordChoice5.get()=="Front":
            CheckCorrect[4]=True
        else:
            CheckCorrect[4]=False
    WordChoice5.trace('w', change_dropdown5)

    WordChoice6 = StringVar(PTWindow)
    WordChoice6.set('Answer Here')
    WordDropdown6 = OptionMenu(PTcanvas, WordChoice6, *choices).place(x=dbPos[0][5],y=dbPos[1][5])
    def change_dropdown6(*args):
        strike(WordChoice6.get())
        if WordChoice6.get()=="Side":
            CheckCorrect[5]=True
        else:
            CheckCorrect[5]=False
    WordChoice6.trace('w', change_dropdown6)


    #QUESTION 5---
    boxPositioning(25,445,"Q5: Check for the proper                           , drill size and material you are working on","proper","none",0,0)
    WordChoice7 = StringVar(PTWindow)
    WordChoice7.set('Answer Here')
    WordDropdown7 = OptionMenu(PTcanvas, WordChoice7, *choices).place(x=dbPos[0][6],y=dbPos[1][6])
    def change_dropdown7(*args):
        strike(WordChoice7.get())
        if WordChoice7.get()=="Speed":
            CheckCorrect[6]=True
        else:
            CheckCorrect[6]=False
    WordChoice7.trace('w', change_dropdown7)


    #QUESTION 6---
    boxPositioning(25,485,"Q6: Never attempt to                           a piece if it slips from the clamp","to","none",0,0)

    WordChoice8 = StringVar(PTWindow)
    WordChoice8.set('Answer Here')
    WordDropdown8 = OptionMenu(PTcanvas, WordChoice8, *choices).place(x=dbPos[0][7],y=dbPos[1][7])
    def change_dropdown8(*args):
        strike(WordChoice8.get())
        if WordChoice8.get()=="Grab":
            CheckCorrect[7]=True
        else:
            CheckCorrect[7]=False
    WordChoice8.trace('w', change_dropdown8)


    #QUESTION 7---
    boxPositioning(25,525,"Q7: Never                           or force a jammed piece through the equipment. Shut the                           off and dislodge the","Never", "the",0,2)
    text_canvas = PTcanvas.create_text(25, 565, anchor = "nw", font=('Helvetica', 15), fill="white")
    PTcanvas.itemconfig(text_canvas, text="piece")
    WordChoice9 = StringVar(PTWindow)
    WordChoice9.set('Answer Here')
    WordDropdown9 = OptionMenu(PTcanvas, WordChoice9, *choices).place(x=dbPos[0][8],y=dbPos[1][8])
    def change_dropdown9(*args):
        strike(WordChoice9.get())
        if WordChoice9.get()=="Pull":
            CheckCorrect[8]=True
        else:
            CheckCorrect[8]=False
    WordChoice9.trace('w', change_dropdown9)
    WordChoice10 = StringVar(PTWindow)
    WordChoice10.set('Answer Here')
    WordDropdown10 = OptionMenu(PTcanvas, WordChoice10, *choices).place(x=dbPos[0][9],y=dbPos[1][9])
    def change_dropdown10(*args):
        strike(WordChoice10.get())
        if WordChoice10.get()=="Machine":
            CheckCorrect[9]=True
        else:
            CheckCorrect[9]=False
    WordChoice10.trace('w', change_dropdown10)


    #QUESTION 8---
    boxPositioning(25,605,"Q8: When cutting with the band saw, the blade should cut on the                           side of the work piece ","the","none",3,0)
    WordChoice11 = StringVar(PTWindow)
    WordChoice11.set('Answer Here')
    WordDropdown11 = OptionMenu(PTcanvas, WordChoice11, *choices).place(x=dbPos[0][10],y=dbPos[1][10])
    def change_dropdown11(*args):
        strike(WordChoice11.get())
        if WordChoice11.get()=="Waste":
            CheckCorrect[10]=True
        else:
            CheckCorrect[10]=False
    WordChoice11.trace('w', change_dropdown11)


    #QUESTION 9---
    boxPositioning(25,645,"Q9: Use the                           when changing blades","the","none",0,0)
    WordChoice12 = StringVar(PTWindow)
    WordChoice12.set('Answer Here')
    WordDropdown12 = OptionMenu(PTcanvas, WordChoice12, *choices).place(x=dbPos[0][11],y=dbPos[1][11])
    def change_dropdown12(*args):
        strike(WordChoice12.get())
        if WordChoice12.get()=="Lock Out":
            CheckCorrect[11]=True
        else:
            CheckCorrect[11]=False
    WordChoice12.trace('w', change_dropdown12)
    boxPositioning(25,725,"blade to                           or                           ","to","or",0,0)
    text_canvas = PTcanvas.create_text(25, 685, anchor = "nw", font=('Helvetica', 15), fill="white")

    #QUESTION 10---
    PTcanvas.itemconfig(text_canvas, text="Q10: When using the band saw, plan your cuts carefully. Saw curves gravdually. Sudden twist will cause the" )
    WordChoice13 = StringVar(PTWindow)
    WordChoice13.set('Answer Here')
    WordDropdown13 = OptionMenu(PTcanvas, WordChoice13, *choices).place(x=dbPos[0][12],y=dbPos[1][12])
    def change_dropdown13(*args):
        strike(WordChoice13.get())
        if WordChoice13.get()=="Break" or WordChoice13.get()=="Bind":
            CheckCorrect[12]=True
        else:
            CheckCorrect[12]=False
    WordChoice13.trace('w', change_dropdown13)

    WordChoice14 = StringVar(PTWindow)
    WordChoice14.set('Answer Here')
    WordDropdown14 = OptionMenu(PTcanvas, WordChoice14, *choices).place(x=dbPos[0][13],y=dbPos[1][13])
    def change_dropdown14(*args):
        strike(WordChoice14.get())
        if WordChoice14.get()=="Bind" or WordChoice13.get()=="Break":
            CheckCorrect[13]=True
        else:
            CheckCorrect[13]=False
    WordChoice14.trace('w', change_dropdown14)

    #SUBMITBUTTON---
    def GetResult():
        PTWindow.destroy()
        PowResult.ReturnMark(CheckCorrect)
    Button(PTcanvas, text="Submit Answers", command=GetResult).place(x=850,y=720)
    PTWindow.mainloop()
