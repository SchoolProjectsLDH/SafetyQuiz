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

        for iteration in range(0,10):
            if WordChoice1.get() != choices[iteration] and WordChoice2.get() != choices[iteration] and WordChoice3.get() != choices[iteration] and WordChoice4.get() != choices[iteration] and WordChoice5.get() != choices[iteration] and WordChoice6.get() != choices[iteration] and WordChoice7.get() != choices[iteration] and WordChoice8.get() != choices[iteration] and WordChoice9.get() != choices[iteration] and WordChoice10.get() != choices[iteration] and cross[iteration]!="":
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

    #----------------------------------
    #START OF QUESTIONS------

    #QUESTION 1---
    #Placing question one at (25,325) with dropdown anchor '->' !!See boxPositioning function for more detail
    boxPositioning(25,325,"Q1: Minor injuries do not need to be reported. -> ","->")
    WordChoice1 = StringVar(GSWindow)#Declaring a dropdown object
    WordChoice1.set('Answer Here')#Initializing text when no word has been chosen
    WordDropdown1 = OptionMenu(mycanvas, WordChoice1, *choices).place(x=dbPos[0],y=dbPos[1])#Placing dropdown object with boxPositioning anchor
    def change_dropdown1(*args):#Function called when dropdown is changed
        strike(WordChoice1.get())#Cross out the chosen word from bank !!See strike function for more information
        if WordChoice1.get() == "False" or WordChoice1.get() == "No" or WordChoice1.get() == "Never!":#Possible correct answers
            CheckCorrect[0] = True#If answer is correct, record it in list for use in result page
        else:
            CheckCorrect[0] = False#When incorrect, mark as false

    WordChoice1.trace('w', change_dropdown1)#Check dropdown's state


    #QUESTION 2--- (See question 1 for comments)
    boxPositioning(25,365,"Q2: If you are uncertain about something in the shop, it is okay to ask a peer. ->","->")
    WordChoice2 = StringVar(GSWindow)
    WordChoice2.set('Answer Here')
    WordDropdown2 = OptionMenu(mycanvas, WordChoice2, *choices).place(x=dbPos[0],y=dbPos[1])
    def change_dropdown2(*args):
        strike(WordChoice2.get())
        if WordChoice2.get()=="Yes" or WordChoice2.get()=="True":
            CheckCorrect[1]=True
        else:
            CheckCorrect[1]==False
    WordChoice2.trace('w', change_dropdown2)


    #QUESTION 3--- (See question 1 for comments)
    boxPositioning(25,405,"Q3: Always get                           from the instructor before using the drill press.","get")
    WordChoice3 = StringVar(GSWindow)
    WordChoice3.set('Answer Here')
    WordDropdown3 = OptionMenu(mycanvas, WordChoice3, *choices).place(x=dbPos[0],y=dbPos[1])
    def change_dropdown3(*args):
        strike(WordChoice3.get())
        if WordChoice3.get()=="Permission":
            CheckCorrect[2]=True
        else:
            CheckCorrect[2]=False
    WordChoice3.trace('w', change_dropdown3)

    #QUESTION 4--- (See question 1 for comments)
    boxPositioning(25,445,"Q4: Students are not allowed to use equipment without having a safety                          for that equipment","safety")
    WordChoice4 = StringVar(GSWindow)
    WordChoice4.set('Answer Here')
    WordDropdown4 = OptionMenu(mycanvas, WordChoice4, *choices).place(x=dbPos[0],y=dbPos[1])
    def change_dropdown4(*args):
        strike(WordChoice4.get())
        if WordChoice4.get()=="Certificate":
            CheckCorrect[3]=True
        else:
            CheckCorrect[3]=False
    WordChoice4.trace('w', change_dropdown4)

    #QUESTION 5--- (See question 1 for comments)
    boxPositioning(25,485,"Q5: Use a                          when cutting small pieces on a bandsaw.","a")
    WordChoice5 = StringVar(GSWindow)
    WordChoice5.set('Answer Here')
    WordDropdown5 = OptionMenu(mycanvas, WordChoice5, *choices).place(x=dbPos[0],y=dbPos[1])
    def change_dropdown5(*args):
        strike(WordChoice5.get())
        if WordChoice5.get()=="Push Stick":
            CheckCorrect[4]=True
        else:
            CheckCorrect[4]=False
    WordChoice5.trace('w', change_dropdown5)


    #QUESTION 6--- (See question 1 for comments)
    boxPositioning(25,525,"Q6: After use,                          and return the tool to its proper place","use,")
    WordChoice6 = StringVar(GSWindow)
    WordChoice6.set('Answer Here')
    WordDropdown6 = OptionMenu(mycanvas, WordChoice6, *choices).place(x=dbPos[0],y=dbPos[1])
    def change_dropdown6(*args):
        strike(WordChoice6.get())
        if WordChoice6.get()=="Clean":
            CheckCorrect[5]=True
        else:
            CheckCorrect[5]=False
    WordChoice6.trace('w', change_dropdown6)


    #QUESTION 7--- (See question 1 for comments)
    boxPositioning(25,565,"Q7: When using a machine you should always wear","wear")
    WordChoice7 = StringVar(GSWindow)
    WordChoice7.set('Answer Here')
    WordDropdown7 = OptionMenu(mycanvas, WordChoice7, *choices).place(x=dbPos[0],y=dbPos[1])
    def change_dropdown7(*args):
        strike(WordChoice7.get())
        if WordChoice7.get()=="Safety Glasses":
            CheckCorrect[6]=True
        else:
            CheckCorrect[6]=False
    WordChoice7.trace('w', change_dropdown7)


    #QUESTION 8--- (See question 1 for comments)
    boxPositioning(25,605,"Q8: It is okay to bring a drink into the shop as long as none of the equipment is running. ->","->")
    WordChoice8 = StringVar(GSWindow)
    WordChoice8.set('Answer Here')
    WordDropdown8 = OptionMenu(mycanvas, WordChoice8, *choices).place(x=dbPos[0],y=dbPos[1])
    def change_dropdown8(*args):
        strike(WordChoice8.get())
        if WordChoice8.get()=="No" or WordChoice8.get()=="False" or WordChoice8.get()=="Never!":
            CheckCorrect[7]=True
        else:
            CheckCorrect[7]=False
    WordChoice8.trace('w', change_dropdown8)


    #QUESTION 9--- (See question 1 for comments)
    text_canvas = mycanvas.create_text(25, 645, anchor = "nw", font=('Helvetica', 15), fill="white")
    mycanvas.itemconfig(text_canvas, text="Q9: Once you have received your equipment certification you may use the equipment any time without" )
    boxPositioning(25,685," permission. ->","->")
    WordChoice9 = StringVar(GSWindow)
    WordChoice9.set('Answer Here')
    WordDropdown9 = OptionMenu(mycanvas, WordChoice9, *choices).place(x=dbPos[0],y=dbPos[1])
    def change_dropdown9(*args):
        strike(WordChoice9.get())
        if WordChoice9.get()=="No"or WordChoice9.get()=="False" or WordChoice9.get()=="Never!":
            CheckCorrect[8]=True
        else:
            CheckCorrect[8]=False
    WordChoice9.trace('w', change_dropdown9)


    #QUESTION 10--- (See question 1 for comments)
    boxPositioning(25,725,"Q10:                          the tool/machine before replacing broken, dull or damaged bits or blades.","Q10:")
    WordChoice10 = StringVar(GSWindow)
    WordChoice10.set('Answer Here')
    WordDropdown10 = OptionMenu(mycanvas, WordChoice10, *choices).place(x=dbPos[0],y=dbPos[1])
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
    Button(mycanvas, text="Submit Answers", command=GetResult).place(x=850,y=755)

    GSWindow.mainloop()
