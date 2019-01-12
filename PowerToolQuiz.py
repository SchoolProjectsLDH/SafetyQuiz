import PowResult
from sys import version_info
if version_info.major == 2:
    from Tkinter import *
elif version_info.major == 3:
    from tkinter import *

def PTQuiz():
    #SEE GENSAFETY.PY FOR DETAILED COMMENTS----
    #------------------------------------------
    #Variables and list
    WordChoice=[]
    WordDropDown=[]
    answer=[["Jewelery"],["Long"],["Kickbacks"],["Angular"],["Front"],["Side"],["Speed"],["Grab"],["Pull"],["Machine"],["Waste"],["Lock Out"],["Break"],["Bind"]]
    cross=[]
    lPos=[[],[],[],[]]
    dbPos=[[],[]]
    backgroundcolour = "#0D6108"
    choices = ["Side","Angular","Machine","Grab","Long","Waste","Pull","Bind","Lock Out","Front","Break","Kickbacks","Jewelery","Speed"]
    CheckCorrect = [False,False,False,False,False,False,False,False,False,False,False,False,False,False]

    #creating the window
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

    #creates a box for the wordbank
    side1=PTcanvas.create_line(25,75,25,250,width="3",fill="white") #creates the verticle left line using the function create_line and sets it to be 3 wide and white
    side2=PTcanvas.create_line(25,250,975,250,width="3",fill="white")
    side3=PTcanvas.create_line(975,250,975,75,width="3",fill="white")
    side4=PTcanvas.create_line(975,75,25,75,width="3",fill="white")


    #places the options (words) inside the box
    for x in range (len(choices)):
        op=PTcanvas.create_text(xPos,yPos,text=choices[x],font=('Helvetica', 15),fill="white")
        for y in range (4):
            lPos[y].append(bbox[y])
        xPos=xPos+185
        if x==4: #if 4 words are written on the screen it will go to the next line
            xPos=125 #resets xPos to 125
            yPos=150 #goes to the next line by setting yPos to 150
        if x==9: #checks to see if there are 4 words written in the second level, if there is it will go to the third line
            xPos=125
            yPos=200
    for x in range(len(choices)):
        cross.append("")

    #Function called when word is selected
    def strike(selected):
        sIndex=choices.index(selected)
        if (cross[sIndex]==""):
            cross[sIndex]=PTcanvas.create_line(lPos[0][sIndex],(lPos[1][sIndex]+lPos[3][sIndex])/2,lPos[2][sIndex],(lPos[1][sIndex]+lPos[3][sIndex])/2,width='3',fill='white')

        for iteration in range(len(choices)):
            if WordChoice[0].get() != choices[iteration] and WordChoice[1].get() != choices[iteration] and WordChoice[2].get() != choices[iteration] and WordChoice[3].get() != choices[iteration] and WordChoice[4].get() != choices[iteration] and WordChoice[5].get() != choices[iteration] and WordChoice[6].get() != choices[iteration] and WordChoice[7].get() != choices[iteration] and WordChoice[8].get() != choices[iteration] and WordChoice[9].get() != choices[iteration] and WordChoice[10].get() != choices[iteration] and WordChoice[11].get() != choices[iteration]  and WordChoice[12].get() != choices[iteration] and WordChoice[13].get() != choices[iteration]and cross[iteration]!="":
                PTcanvas.delete(cross[iteration]) #destroys the the line on the screen
                cross[iteration]="" #resets cross at that word to be blank

    #Creating constant positions for questions
    def boxPositioning(x,y,text,bDB,bDB2,skip,skip2):
        space=5
        qxPos=x
        qyPos=y
        used=False #creates a variable called used and sets it to false (checks to determine if the drop box is created )
        used2=False #same as used, but is for if there is 2 dropdowns for one questions
        tCount=0
        tCount2=0
        for word in text.split(" "):
            question=PTcanvas.create_text(qxPos,qyPos,text=word, anchor = "nw", font=('Helvetica', 15), fill="white")
            qbox=PTcanvas.bbox(question)
            qxPos=qbox[2]+space
            if (skip!=0 or skip2!=0):
                if(str(word)==str(bDB)and skip!=0):
                    #checks to see if the word the for loop is on now is equal to one of the target words and if it has to be skipped
                    tCount+=1 #adds one to tCount
                if(str(word)==str(bDB2) and skip2!=0):
                    #same as the previous if statement, but for the second one
                    tCount2+=1

            if (str(word) == str(bDB) and used==False and tCount==skip):
                #checks to see if the the word the for loop is on is equal to one of the target words, if the drop box has not been used and it has skipped enough words
                dbPos[0].append(qbox[2]+space)
                dbPos[1].append(qbox[1])
                used=True
            if (str(word)==str(bDB2) and used2==False and tCount2==skip2):
                dbPos[0].append(qbox[2]+space)
                dbPos[1].append(qbox[1])
                used2=True

    #Procedure to create dropboxes
    for x in range(len(choices)):
        WordChoice.append(StringVar(PTWindow))
        WordChoice[x].set('Answer Here')
        WordDropDown.append("")
    def dBox(num):
        WordDropDown[num]=OptionMenu(PTcanvas,WordChoice[num],*choices).place(x=dbPos[0][num],y=dbPos[1][num])
        def changeDropDown(*args):
            strike(WordChoice[num].get())
            if WordChoice[num].get()==answer[num]:
                CheckCorrect[num]=True
            else:
                CheckCorrect[num]=False
        WordChoice[num].trace('w',changeDropDown)

    #QUESTIONS---
    q=["Q1: Remove all                           and tie back                           hair","Q2: Watch for                           when cutting small pieces","Q3: When making                           cuts ensure the blade has adequate clearance","Q4: Always operate the drill press from the                           ,never from the                           ","Q5: Check for the proper                           , drill size and material you are working on","Q6: Never attempt to                           a piece if it slips from the clamp","Q7: Never                           or force a jammed piece through the equipment. Shut the                           off","Q8: When cutting with the band saw, the blade should cut on the                           side of the work piece ","Q9: Use the                           when changing blades","blade to                           or                           "]
    after=["all","for","making","the","proper","to","Never","the","the","to"]
    after2=["back","none","none","the","none","none", "the","none","none","or"] #same as the after list
    skip=[0,0,0,2,0,0,0,3,0,0] #creates a list called skip to hold the number of times the after words must be skip in each question
    skip2=[0,0,0,3,0,0,2,0,0,0] #same as skip, but for after2
    dyPos=285 #creates a variable called dyPOs (Dropbox y position) to hold the y position of the drop box

    for x in range (len(q)): #creates a for loop that loops the number of questions
        boxPositioning(25,dyPos,q[x],after[x],after2[x],skip[x],skip2[x]) #See boxpositioning function
        dyPos=dyPos+40 #adds 40 to the current dyPos
        if x ==6: #checks to see if it is on question 7 (placed 6 previous questions)
            text_canvas = PTcanvas.create_text(25, 565, anchor = "nw", font=('Helvetica', 15), fill="white")
            PTcanvas.itemconfig(text_canvas, text="and dislodge the piece")
            dyPos=605
        elif x==8:
            text_canvas = PTcanvas.create_text(25, 685, anchor = "nw", font=('Helvetica', 15), fill="white")
            PTcanvas.itemconfig(text_canvas, text="Q10: When using the band saw, plan your cuts carefully. Saw curves gravdually. Sudden twist will cause the" )
            dyPos=725
    for x in range(len(choices)):
        dBox(x)


    #SUBMITBUTTON---
    def GetResult():
        PTWindow.destroy()
        PowResult.ReturnMark(CheckCorrect)
    Button(PTcanvas, text="Submit Answers", command=GetResult).place(x=850,y=720)
    PTWindow.mainloop()
