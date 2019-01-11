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
    WordChoice=[]#Holds the choices for the words
    WordDropDown=[]#Special array for the dropdown
    answer=[["False","No","Never!"],["Yes","True"],["Permission"],["Certificate"],["Push Stick"],["Clean"],["Safety Glasses"],["No","False","Never!"],["No","False","Never!"],["Unplug"]]#Possible answers for each dropdown
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
    side1=mycanvas.create_line(25,75,25,250,width="3",fill="white")#Creating the 4 borders of wordbank
    side2=mycanvas.create_line(25,250,975,250,width="3",fill="white")
    side3=mycanvas.create_line(975,250,975,75,width="3",fill="white")
    side4=mycanvas.create_line(975,75,25,75,width="3",fill="white")

    #Mapping strikethrough for wordbank
    for x in range (len(choices)):#Go over all the choices in the dropdown
        op=mycanvas.create_text(xPos,yPos,text=choices[x],font=('Helvetica', 15),fill="white")#Placing the words in the wordbank
        bbox=mycanvas.bbox(op)#Mapping the location of the word
        for y in range (4):#Moving up so that the words are evenly spaced
            lPos[y].append(bbox[y])
        xPos=xPos+185#Move over right 185px
        if x==4:#If it is the 5th word then reset the x position and move down
            xPos=125#Resetting coords
            yPos=175
    for x in range(len(choices)):#Holds position for the strikethrough lines
        cross.append("")#Starts off empty (Nothing striked yet)

    #Function for crossing out words in bank
    def strike(selected):
        sIndex=choices.index(selected)#Search for the selected word in choices list and set it as the index
        if(cross[sIndex]==""):#Only if there is no strikethrough line
            #Crosses off the selected word
            cross[sIndex]=mycanvas.create_line(lPos[0][sIndex],(lPos[1][sIndex]+lPos[3][sIndex])/2,lPos[2][sIndex],(lPos[1][sIndex]+lPos[3][sIndex])/2,width='3',fill='white')
        deselect=[]
        for iteration in range(len(choices)):#Go through all choices again (length)
            #Only if it is not selected in any dropdown
            if WordChoice[0].get() != choices[iteration] and WordChoice[1].get() != choices[iteration] and WordChoice[2].get() != choices[iteration] and WordChoice[3].get() != choices[iteration] and WordChoice[4].get() != choices[iteration] and WordChoice[5].get() != choices[iteration] and WordChoice[6].get() != choices[iteration] and WordChoice[7].get() != choices[iteration] and WordChoice[8].get() != choices[iteration] and WordChoice[9].get() != choices[iteration] and cross[iteration]!="":
                #Remove the strikethrough
                mycanvas.delete(cross[iteration])
                cross[iteration]=""#Reset the crossed off list

    #Creating constant positions for questions
    def boxPositioning(x,y,text,bDB):
        space=5#Sets the space between the beggining word and the dropdown left side
        qxPos=x#Question's x position
        qyPos=y#Question's y position
        used=False#Initializing with the state as empty
        for word in text.split(" "):#Splite the strike into individual words
            question=mycanvas.create_text(qxPos,qyPos,text=word, anchor = "nw", font=('Helvetica', 15), fill="white")#Places the questions on the canvas
            qbox=mycanvas.bbox(question)#Maps question location
            qxPos=qbox[2]+space#Spaces out the words
            if (str(word) == str(bDB) and used==False):#If the word has not been placed yet
                dbPos[0]=qbox[2]+space#Give it a position
                dbPos[1]=qbox[1]
                used=True#Set it as used

    for x in range(len(choices)):
        WordChoice.append(StringVar(GSWindow))#StringVar for the dropdown (enables use of widgets)
        WordChoice[x].set('Answer Here')#Set initial text
        WordDropDown.append("")#Add the dropdown to list

    #Procedure to create dropboxes
    def dBox(num):
        WordDropDown[num]=OptionMenu(mycanvas,WordChoice[num],*choices).place(x=dbPos[0],y=dbPos[1])#Declaring the dropbox as an optionmenu syntax
        def change_DropDown (*args):#Function calls when a dropdown is changed
            strike(WordChoice[num].get())#strikethrough the word that was choces
            for x in range (len(answer[num])):#Iterate through words and check if it is correct
                if WordChoice[num].get()==answer[num][x]:#If the indexed answer in teh correct positions equal what the user chose
                    #Set as correct
                    CheckCorrect[num] = True
                    print("Correct")
                    print(CheckCorrect)
                    break#End for loop
                else:
                    CheckCorrect[num] = False#If none of the cells are equal to chosen word, the user got it wrong
                    print(CheckCorrect)
                    print("Incorrect")
        WordChoice[num].trace('w',change_DropDown)#Observer for the dropdowns, this line catches when the user switches their choice

    #----------------------------------
    #START OF QUESTIONS------

    #Placing question one at (25,325) with dropdown anchor '->' !!See boxPositioning function for more detail
    dyPos=325
    #list of all question in the category
    q=["Q1: Minor injuries do not need to be reported. -> ","Q2: If you are uncertain about something in the shop, it is okay to ask a peer. ->","Q3: Always get                           from the instructor before using the drill press.","Q4: Students are not allowed to use equipment without having a safety                          for that equipment","Q5: Use a                          when cutting small pieces on a bandsaw.","Q6: After use,                          and return the tool to its proper place","Q7: When using a machine you should always wear","Q8: It is okay to bring a drink into the shop as long as none of the equipment is running. ->"," permission. ->","Q10:                          the tool/machine before replacing broken, dull or damaged bits or blades."]
    after=["->","->","get","safety","a","use,","wear","->","->","Q10:"]#Separators for the questions (Used to give constant positions to the dropdowns)
    for x in range (len(q)):#Go through all the questions
        if x==8:#If it is on the ninth question
            text_canvas = mycanvas.create_text(25, 645, anchor = "nw", font=('Helvetica', 15), fill="white")#Give the word a special location
            mycanvas.itemconfig(text_canvas, text="Q9: Once you have received your equipment certification you may use the equipment any time without" )
            dyPos=685
        boxPositioning(25,dyPos,q[x],after[x])#Place the question on the canvas
        dBox(x)
        dyPos=dyPos+40#Interval through the positions for the questions

    #SUBMITBUTTON---
    def GetResult():#Function to get the answers and display mark
        GSWindow.destroy()#Ends question window
        GenResult.ReturnMark(CheckCorrect)#Creates result window (See GenSafety.py)
    Button(mycanvas, text="Submit Answers", command=GetResult).place(x=850,y=755)#Button for submitting answers, calls function GetResult

    #End of program
    GSWindow.mainloop()
