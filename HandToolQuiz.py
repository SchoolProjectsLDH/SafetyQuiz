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
            if WordChoice[0].get() != choices[iteration] and WordChoice[1].get() != choices[iteration] and WordChoice[2].get() != choices[iteration] and WordChoice[3].get() != choices[iteration] and WordChoice[4].get() != choices[iteration] and WordChoice[5].get() != choices[iteration] and WordChoice[6].get() != choices[iteration] and WordChoice[7].get() != choices[iteration] and WordChoice[8].get() != choices[iteration] and WordChoice[9].get() != choices[iteration] and cross[iteration]!="":
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
    WordChoice=[]
    WordDropDown=[]
    answer=[["False"],["Yes","True"],["Drawer"],["Face"],["Glancing"],["Robertson"],["Offset Screwdriver"],["Sharp"],["Grab"],["Yes","True"]]
    for x in range(len(choices)):
        WordChoice.append(StringVar(HTWindow))
        WordChoice[x].set('Answer Here          ')
        WordDropDown.append("")
    def dBox(num):
        num=num-1
        WordDropDown[num]=OptionMenu(HTcanvas, WordChoice[num], *choices).place(x=dbPos[0],y=dbPos[1])
        def changeDropDown (*args):
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
    q=["Q1: You should use a long throat clamp instead of a deep throat clamp. ->","Q2: Without padding, a clamp can leave marks on your work ->","Q3: We store C clamps in the                               .","Q4: For hammers, you should use the                               to hit an object","Q5: For a hammer, You should avoid                               blows when hitting an object.","Q6: The square head screwdriver is called a:","Q7: You should use an                               in tight areas","Q8: You should use a                               blade when cutting","Q9: Do not                               a falling knife","Q10: You can leave hot glue guns unattended if unplugged. ->"]
    after=["->","->","the","the","avoid","a:","an","a","not","->"]
    qyPos=325
    #QUESTION 1---
    for x in range (len(q)):
        boxPositioning(25,qyPos,q[x],after[x])
        dBox(x+1)
        qyPos=qyPos+40

    #SUBMITBUTTON---
    def GetHTResult():
        HTWindow.destroy()
        HandToolResult.ReturnHTMark(CheckCorrect)
    Button(HTcanvas, text="Submit Answers", command=GetHTResult).place(x=850,y=700)
    HTWindow.mainloop()
