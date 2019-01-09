from sys import version_info
import GenResult
if version_info.major == 2:
    from Tkinter import *
elif version_info.major == 3:
    from tkinter import *

def GSQuiz():
    #Variables
    cross=[]#Records if the word has been user or not
    lPos=[[],[],[],[]] #letter position
    dbPos=[[],[]]#Possition of questions and dropdown anchor list
    backgroundcolour = "#460000" #Variable to set background colour
    choices = ["Yes", "Clean", "Push Stick", "No", "Unplug", "False", "Permission", "Safety Glasses", "Certificate", "Never!"]#Declaring the possible choices for the user and answers
    CheckCorrect = [False,False,False,False,False,False,False,False,False,False]#Array to record correct answers

    #Creating tkinter window
    GSWindow = Tk()#Creating a TK window with alias GSWindow
    GSWindow.title("General Safety Quiz")#Setting title of window
    GSWindow.geometry("1000x800")#Making window 1000x800
    GSWindow.resizable(False,False)#Disabling resizability for x and y directions

    #Creating window canvas
    mycanvas = Canvas(GSWindow, width = 1000, height = 800)#Creating a canvas ontop of window to enable the extra atributes and precision X,Y placement
    mycanvas.create_rectangle(0, 0, 1000, 8000, fill = backgroundcolour)#Drawing the background
    mycanvas.pack(side = "top", fill = "both", expand = True)#Placing the canvas from top to bottom (Cover screen)

    #title
    title=Label(mycanvas,text="General Safety",font=("Helvetica",30),bg=backgroundcolour,fg="white").place(x=500,y=20, anchor= CENTER)#Add title to windw, middle top of screen

    #wordbank
    xPos=125#Initializing word starting positions
    yPos=100#See above comment
    choicePos=[[],[]]#Recording location of words
    side1=mycanvas.create_line(25,75,25,250,width="3",fill="white")#Creating the 4 borders of wordbank
    side2=mycanvas.create_line(25,250,975,250,width="3",fill="white")
    side3=mycanvas.create_line(975,250,975,75,width="3",fill="white")
    side4=mycanvas.create_line(975,75,25,75,width="3",fill="white")

    #Mapping strikethrough for wordbank
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

    #Function for crossing out words in bank
    def strike(selected):
        sIndex=choices.index(selected)
        if(cross[sIndex]==""):
            cross[sIndex]=mycanvas.create_line(lPos[0][sIndex],(lPos[1][sIndex]+lPos[3][sIndex])/2,lPos[2][sIndex],(lPos[1][sIndex]+lPos[3][sIndex])/2,width='3',fill='white')
        deselect=[]
        for iteration in range(len(choices)):
            if WordChoice[0].get() != choices[iteration] and WordChoice[1].get() != choices[iteration] and WordChoice[2].get() != choices[iteration] and WordChoice[3].get() != choices[iteration] and WordChoice[4].get() != choices[iteration] and WordChoice[5].get() != choices[iteration] and WordChoice[6].get() != choices[iteration] and WordChoice[7].get() != choices[iteration] and WordChoice[8].get() != choices[iteration] and WordChoice[9].get() != choices[iteration] and cross[iteration]!="":
                mycanvas.delete(cross[iteration])
                cross[iteration]=""

    #Creating constant positions for questions
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


    WordChoice=[]
    WordDropDown=[]
    answer=[["False","No","Never!"],["Yes","True"],["Permission"],["Certificate"],["Push Stick"],["Clean"],["Safety Glasses"],["No","False","Never!"],["No","False","Never!"],["Unplug"]]
    for x in range(len(choices)):
        WordChoice.append(StringVar(GSWindow))
        WordChoice[x].set('Answer Here')
        WordDropDown.append("")
    def dBox(num):
        num=num-1
        WordDropDown[num]=OptionMenu(mycanvas,WordChoice[num],*choices).place(x=dbPos[0],y=dbPos[1])
        def change_DropDown (*args):
            strike(WordChoice[num].get())
            for x in range (len(answer[num])):
                if WordChoice[num].get()==answer[num][x]:
                    CheckCorrect[num] = True
                    print("Correct")
                    print(CheckCorrect)
                    break
                else:
<<<<<<< HEAD
                    multiAnswer.append(0)
            if multiAnswer.count(1)==1:
                CheckCorrect[num]=True
            else:
                CheckCorrect[num]=False
=======
                    CheckCorrect[num] = False
                    print(CheckCorrect)
                    print("Incorrect")
>>>>>>> 4f0298346cb3177895f9aed7de9e7215f60bc6ba
        WordChoice[num].trace('w',change_DropDown)
    #----------------------------------
    #START OF QUESTIONS------

    #QUESTION 1---
    #Placing question one at (25,325) with dropdown anchor '->' !!See boxPositioning function for more detail
    dyPos=325
    q=["Q1: Minor injuries do not need to be reported. -> ","Q2: If you are uncertain about something in the shop, it is okay to ask a peer. ->","Q3: Always get                           from the instructor before using the drill press.","Q4: Students are not allowed to use equipment without having a safety                          for that equipment","Q5: Use a                          when cutting small pieces on a bandsaw.","Q6: After use,                          and return the tool to its proper place","Q7: When using a machine you should always wear","Q8: It is okay to bring a drink into the shop as long as none of the equipment is running. ->"," permission. ->","Q10:                          the tool/machine before replacing broken, dull or damaged bits or blades."]
    after=["->","->","get","safety","a","use,","wear","->","->","Q10:"]
    for x in range (len(q)):
        if x==8:
            text_canvas = mycanvas.create_text(25, 645, anchor = "nw", font=('Helvetica', 15), fill="white")
            mycanvas.itemconfig(text_canvas, text="Q9: Once you have received your equipment certification you may use the equipment any time without" )
            dyPos=685
        boxPositioning(25,dyPos,q[x],after[x])
        dBox(x+1)
        dyPos=dyPos+40

    #SUBMITBUTTON---
    def GetResult():
        GSWindow.destroy()
        GenResult.ReturnMark(CheckCorrect)
    Button(mycanvas, text="Submit Answers", command=GetResult).place(x=850,y=755)

    GSWindow.mainloop()
