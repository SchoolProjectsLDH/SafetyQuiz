import PowResult
from sys import version_info
if version_info.major == 2:
    from Tkinter import *
elif version_info.major == 3:
    from tkinter import *

def PTQuiz():
    cross=[]
    lPos=[[],[],[],[]] #letter position
    dbPos=[[],[]]
    backgroundcolour = "#0D6108"
    choices = ["Side","Angular","Machine","Grab","Long","Waste","Pull","Bind","Lock Out","Front","Break","Kickbacks","Jewelery","Speed"]
    CheckCorrect = [False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    PTWindow=Tk()
    PTWindow.title("Power Tool Quiz")
    PTWindow.geometry("1000x800")
    PTWindow.resizable(False,False)
    PTcanvas = Canvas(PTWindow, width = 1000, height = 800)
    PTcanvas.create_rectangle(0, 0, 1000, 8000, fill = backgroundcolour)
    PTcanvas.pack(side = "top", fill = "both", expand = True)

    #title
    title=Label(PTcanvas,text="Power Tool Safety",font=("Helvetica",30),bg=backgroundcolour,fg="white").place(x=500,y=25, anchor= CENTER)

    #WordBank
    xPos=125
    yPos=100
    side1=PTcanvas.create_line(25,75,25,250,width="3",fill="white")
    side2=PTcanvas.create_line(25,250,975,250,width="3",fill="white")
    side3=PTcanvas.create_line(975,250,975,75,width="3",fill="white")
    side4=PTcanvas.create_line(975,75,25,75,width="3",fill="white")

    #xsPos ysPos xePos yePos
    #s is start e is end
    for x in range (len(choices)):
        op=PTcanvas.create_text(xPos,yPos,text=choices[x],font=('Helvetica', 15),fill="white")
        bbox=PTcanvas.bbox(op)
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
        print(cross)
        sIndex=choices.index(selected)
        if (cross[sIndex]==""):
            cross[sIndex]=PTcanvas.create_line(lPos[0][sIndex],(lPos[1][sIndex]+lPos[3][sIndex])/2,lPos[2][sIndex],(lPos[1][sIndex]+lPos[3][sIndex])/2,width='3',fill='white')

        for iteration in range(0,14):
            if WordChoice[0].get() != choices[iteration] and WordChoice[1].get() != choices[iteration] and WordChoice[2].get() != choices[iteration] and WordChoice[3].get() != choices[iteration] and WordChoice[4].get() != choices[iteration] and WordChoice[5].get() != choices[iteration] and WordChoice[6].get() != choices[iteration] and WordChoice[7].get() != choices[iteration] and WordChoice[8].get() != choices[iteration] and WordChoice[9].get() != choices[iteration] and WordChoice[10].get() != choices[iteration] and WordChoice[11].get() != choices[iteration]  and WordChoice[12].get() != choices[iteration] and WordChoice[13].get() != choices[iteration]and cross[iteration]!="":
                PTcanvas.delete(cross[iteration])
                cross[iteration]=""

    def boxPositioning(x,y,text,bDB,bDB2,skip,skip2):
        space=5
        qxPos=x
        qyPos=y
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
    WordChoice=[]
    WordDropDown=[]
    answer=[["Jewelery"],["Long"],["Kickbacks"],["Angular"],["Front"],["Side"],["Speed"],["Grab"],["Pull"],["Machine"],["Waste"],["Lock Out"],["Break"],["Bind"]]
    for x in range(len(choices)):
        WordChoice.append(StringVar(PTWindow))
        WordChoice[x].set('Answer Here')
        WordDropDown.append("")
    def dBox(num):
        WordDropDown[num]=OptionMenu(PTcanvas,WordChoice[num],*choices).place(x=dbPos[0][num],y=dbPos[1][num])
        def changeDropDown(*args):
            strike(WordChoice[num].get())
            for x in range (len(answer[num])):
                if WordChoice[num].get()==answer[num][x]:
                    CheckCorrect[num] = True
                    print("Correct")
                    print(CheckCorrect)
                    print(answer[num][x])
                    break
                else:
                    CheckCorrect[num] = False
                    print(CheckCorrect)
                    print("Incorrect")
                    print(answer[num][x])
        WordChoice[num].trace('w',changeDropDown)

    #QUESTION 1---
    q=["Q1: Remove all                           and tie back                           hair","Q2: Watch for                           when cutting small pieces","Q3: When making                           cuts ensure the blade has adequate clearance","Q4: Always operate the drill press from the                           ,never from the                           ","Q5: Check for the proper                           , drill size and material you are working on","Q6: Never attempt to                           a piece if it slips from the clamp","Q7: Never                           or force a jammed piece through the equipment. Shut the                           off","Q8: When cutting with the band saw, the blade should cut on the                           side of the work piece ","Q9: Use the                           when changing blades","blade to                           or                           "]
    after=["all","for","making","the","proper","to","Never","the","the","to"]
    after2=["back","none","none","the","none","none", "the","none","none","or"]
    skip=[0,0,0,2,0,0,0,3,0,0]
    skip2=[0,0,0,3,0,0,2,0,0,0]
    dyPos=285

    for x in range (len(q)):
        boxPositioning(25,dyPos,q[x],after[x],after2[x],skip[x],skip2[x])

        dyPos=dyPos+40
        if x ==6:
            text_canvas = PTcanvas.create_text(25, 565, anchor = "nw", font=('Helvetica', 15), fill="white")
            PTcanvas.itemconfig(text_canvas, text="and dislodge the piece")
            dyPos=605
        elif x==8:
            text_canvas = PTcanvas.create_text(25, 685, anchor = "nw", font=('Helvetica', 15), fill="white")
            PTcanvas.itemconfig(text_canvas, text="Q10: When using the band saw, plan your cuts carefully. Saw curves gravdually. Sudden twist will cause the" )
            dyPos=725
    for x in range(len(choices)):
        dBox(x)
        #have to be second because there was a problem were it would not print drop boxes after q7. the reason is that there has already been 10 drop boxe that have been creazted for the 10 questions, but there are 14 drop boxes. you can't change the for loop to 14 because there is only 10 questions and you would get an error saying it is out of range so that is why you need a second for loops
        #problem not striking out because I forgot to change the last 4 into [#], before the change it would give an error sayling thatwordhoice# is not defined

    #SUBMITBUTTON---
    def GetResult():
        PTWindow.destroy()
        PowResult.ReturnMark(CheckCorrect)
    Button(PTcanvas, text="Submit Answers", command=GetResult).place(x=850,y=720)
    PTWindow.mainloop()
