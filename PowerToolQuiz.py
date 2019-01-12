import PowResult
from sys import version_info
if version_info.major == 2:
    from Tkinter import *
elif version_info.major == 3:
    from tkinter import *

def PTQuiz():
    #Variables and list
    cross=[] # create a list to hold the position the function that creates a line
    lPos=[[],[],[],[]] #lPos stands for letter position and it holds the start and end position of the words in the wordbox (lets us completely crossout the whole word in the word box)
    dbPos=[[],[]] #dbPos stands for drop box position. This list holds the coordinates for the drop box position
    backgroundcolour = "#0D6108" #sets the background colour to a green (hex colour code #0D6108
    choices = ["Side","Angular","Machine","Grab","Long","Waste","Pull","Bind","Lock Out","Front","Break","Kickbacks","Jewelery","Speed"] #creates a list to hold all the options that the user can choose
    CheckCorrect = [False,False,False,False,False,False,False,False,False,False,False,False,False,False] #creates a list called CheckCorrect to hold the value of whether the user got an answer correct or wrong

    #creating the window
    PTWindow=Tk()#creates a master widget (where all the other widges go) called PTWindow and it creates a window
    PTWindow.title("Power Tool Quiz") #sets the title of the window to Power Tool Quiz
    PTWindow.geometry("1000x800") #sets the dimensions of the window to be 1000 wide and 800 high
    PTWindow.resizable(False,False) #makes it so the window cannot change size if you hit the restore or maximize button
    PTcanvas = Canvas(PTWindow, width = 1000, height = 800) #creats a widget that is a canvas called PTCanvas and makes it appear on PTWindow (the master widget) as well as sets the height and width of it
    PTcanvas.create_rectangle(0, 0, 1000, 8000, fill = backgroundcolour) #gives dimension to canvas and sets the background colour of it
    PTcanvas.pack(side = "top", fill = "both", expand = True)#Places the canvas on the master widget PTWindow

    #title
    title=Label(PTcanvas,text="Power Tool Safety",font=("Helvetica",30),bg=backgroundcolour,fg="white").place(x=500,y=25, anchor= CENTER)#creates a label called title that displays text on the canvas (top center of it) saying that you are in the Power Tool Quiz

    #WordBank
    xPos=125 #creates a variable called xPos and sets it to 125 (holds the x Position of the words)
    yPos=100 #same as xPos, but hold y position and sets it to 100

        #creates a box for the wordbank
    side1=PTcanvas.create_line(25,75,25,250,width="3",fill="white") #creates the verticle left line using the function create_line and sets it to be 3 wide and white
    side2=PTcanvas.create_line(25,250,975,250,width="3",fill="white") #creates bottom line same method as above
    side3=PTcanvas.create_line(975,250,975,75,width="3",fill="white") #creates verticle right line same method as above
    side4=PTcanvas.create_line(975,75,25,75,width="3",fill="white") #creates top line same method as above


        #places the options (words) inside the box
    for x in range (len(choices)): #creates a for loop that will loop the length of choices
        op=PTcanvas.create_text(xPos,yPos,text=choices[x],font=('Helvetica', 15),fill="white") #creates a new text widget called op (option) and sets its position to xPos and yPos changing the font Helvetica and making the text white
        bbox=PTcanvas.bbox(op) #creates a list called bbox and sets it to the positions of the words
        for y in range (4): #creats a for loop that loops 4 times
            lPos[y].append(bbox[y]) #appends bbox value in slot y to the list lPos slot y to store the position permanetly
        xPos=xPos+185 #adds 185 to xPos
        if x==4: #if 4 words are written on the screen it will go to the next line
            xPos=125 #resets xPos to 125
            yPos=150 #goes to the next line by setting yPos to 150
        if x==9: #checks to see if there are 4 words written in the second level, if there is it will go to the third line
            xPos=125 #same as checking for 4 words
            yPos=200
    for x in range(len(choices)): #creates a for loop that loops for each word in choices
        cross.append("") #appends "" to cross

    def strike(selected): #create a procedure called strike
        #it will strike out or destrike the word that has been chosen on the wordlist
        print(cross) #prints cross to say that the program has called the this procedure
        sIndex=choices.index(selected) #creates a variable called sIndex and sets it to the slot number of user's choice in the list choices
        if (cross[sIndex]==""): #checks to see if cross at slot sIndex(selected option) is equal to nothing, if it is it will create a line
            cross[sIndex]=PTcanvas.create_line(lPos[0][sIndex],(lPos[1][sIndex]+lPos[3][sIndex])/2,lPos[2][sIndex],(lPos[1][sIndex]+lPos[3][sIndex])/2,width='3',fill='white') #sets cross at slot of the number of the selected option to the command that creates a line and draws a line to strike out the select options

        for iteration in range(len(choices)): #creates a for loop to loop the length of choices (it checks to see if any of the words have been deselected)
            if WordChoice[0].get() != choices[iteration] and WordChoice[1].get() != choices[iteration] and WordChoice[2].get() != choices[iteration] and WordChoice[3].get() != choices[iteration] and WordChoice[4].get() != choices[iteration] and WordChoice[5].get() != choices[iteration] and WordChoice[6].get() != choices[iteration] and WordChoice[7].get() != choices[iteration] and WordChoice[8].get() != choices[iteration] and WordChoice[9].get() != choices[iteration] and WordChoice[10].get() != choices[iteration] and WordChoice[11].get() != choices[iteration]  and WordChoice[12].get() != choices[iteration] and WordChoice[13].get() != choices[iteration]and cross[iteration]!="": #checks to see if any of the words are deselected by checking each dropbox to a word on the word bank and checks to see if cross is not equal to blank
                PTcanvas.delete(cross[iteration]) #destroys the the line on the screen
                cross[iteration]="" #resets cross at that word to be blank

    def boxPositioning(x,y,text,bDB,bDB2,skip,skip2): #creates a procedure called box position that takes in 7 parameters, 2 for positioning, 1 for the question, 2 for drop box location and 2 for how many words to skip
        space=5 #creates a variable called space and sets it to 5 (to space out the words)
        qxPos=x #creates a variable called qxPos (question x position) and sets it to x
        qyPos=y #same as qxPos, but for y
        used=False #creates a variable called used and sets it to false (checks to determine if the drop box is created )
        used2=False #same as used, but is the second one
        tCount=0 #creates a variable called tcount (and set to 0) to count how many times a word has gone by
        tCount2=0 #same as tCount, but the second one
        for word in text.split(" "): #creates a for loop to display the question ( it will loop for every word in the sentence)
            question=PTcanvas.create_text(qxPos,qyPos,text=word, anchor = "nw", font=('Helvetica', 15), fill="white") #creates a variable called question and sets it to the command to create a text that is in the top right corner with the font Helvetica, size 15 and is white
            qbox=PTcanvas.bbox(question) #creates a list called qbox and sets it to the start and end coordinates of the word
            qxPos=qbox[2]+space #sets the new qxPos (start for the next word) to be the end position of the last word + the value of space
            if (skip!=0 or skip2!=0): #checks to see if you have to skip any word
                if(str(word)==str(bDB)and skip!=0): #checks to see if the word the for loop is on now is equal to one of the target words and if it has to be skipped
                    tCount+=1 #adds one to tCount
                if(str(word)==str(bDB2) and skip2!=0): #same as the previous if statement, but for the second one
                    tCount2+=1

            if (str(word) == str(bDB) and used==False and tCount==skip): #checks to see if the the word the for loop is on is equal to one of the target words, if the drop box has not been used and it has skipped enough words
                dbPos[0].append(qbox[2]+space) #appends to dbPos (drop box position) slot 0 to be the end position of the word + the value of space
                dbPos[1].append(qbox[1]) #appends to dbPos in slot 1 to the y position of the word
                used=True #sets used to true
            if (str(word)==str(bDB2) and used2==False and tCount2==skip2): #same thing as the previous if statement
                dbPos[0].append(qbox[2]+space)
                dbPos[1].append(qbox[1])
                used2=True

    WordChoice=[] #creates a list called wordChoice
    WordDropDown=[] #creates a list called WordDropDown
    answer=[["Jewelery"],["Long"],["Kickbacks"],["Angular"],["Front"],["Side"],["Speed"],["Grab"],["Pull"],["Machine"],["Waste"],["Lock Out"],["Break"],["Bind"]] #creates a list called answer and sets it to the answer of each question
    for x in range(len(choices)): #creates a for loops that repeats for the number of words in choices
        WordChoice.append(StringVar(PTWindow)) #appends command StringVar(PTwindow) to Wordchoice for each word
        WordChoice[x].set('Answer Here') #sets WordChoice in slot x to be Answer here
        WordDropDown.append("") #appends blank to WordDrop Down
    def dBox(num): #creates a function called dBox (drop box) that takes in the parameter num
        WordDropDown[num]=OptionMenu(PTcanvas,WordChoice[num],*choices).place(x=dbPos[0][num],y=dbPos[1][num]) #assigns DropBox in selected question to be equal to to the command that makes a drop box and places it in the right position (that was determined in box positioningg)and has the options in the word bank
        def changeDropDown(*args): #creates a procedure called changeDropDown that takes in all the arguments
            strike(WordChoice[num].get()) #calls function strike with the parameter of WordChoice[num].get() (what word the user chose from the dropbox)
            if WordChoice[num].get()==answer[num]: #checks to see if the selected word is equal to the answer
                CheckCorrect[num]=True #if it is it sets CheckCorrect of the dropbox number to be True
            else: #if it is not equal to it
                CheckCorrect[num]=False #sets the checkcorrect of the dropbox number to be False
        WordChoice[num].trace('w',changeDropDown) #changes the dropbox text

    #QUESTION 1---
    q=["Q1: Remove all                           and tie back                           hair","Q2: Watch for                           when cutting small pieces","Q3: When making                           cuts ensure the blade has adequate clearance","Q4: Always operate the drill press from the                           ,never from the                           ","Q5: Check for the proper                           , drill size and material you are working on","Q6: Never attempt to                           a piece if it slips from the clamp","Q7: Never                           or force a jammed piece through the equipment. Shut the                           off","Q8: When cutting with the band saw, the blade should cut on the                           side of the work piece ","Q9: Use the                           when changing blades","blade to                           or                           "] #creates a list q to hold all the questions
    after=["all","for","making","the","proper","to","Never","the","the","to"] #creates a list called after to hold the word that the dropbox comes after
    after2=["back","none","none","the","none","none", "the","none","none","or"] #same as the after list
    skip=[0,0,0,2,0,0,0,3,0,0] #creates a list called skip to hold the number of times the after words must be skip in each question
    skip2=[0,0,0,3,0,0,2,0,0,0] #same as skip, but for after2
    dyPos=285 #creates a variable called dyPOs (Dropbox y position) to hold the y position of the drop box

    for x in range (len(q)): #creates a for loop that loops the number of questions
        boxPositioning(25,dyPos,q[x],after[x],after2[x],skip[x],skip2[x]) #calls procedure boxPositioning and sets it parameters to be the the values in slot x of hte different lists (this places the drop box)

        dyPos=dyPos+40 #adds 40 to the current dyPos
        if x ==6: #checks to see if it is on question 7 (placed 6 previous questions)
            text_canvas = PTcanvas.create_text(25, 565, anchor = "nw", font=('Helvetica', 15), fill="white") #creates a text that is white and helvetica 15 and is at the coordinates 25,565
            PTcanvas.itemconfig(text_canvas, text="and dislodge the piece") #displays the text on the canvas
            dyPos=605 #changes dyPos to be the next line under
        elif x==8: #checks to see if it is on question 9 and does the same thing as if x ==6
            text_canvas = PTcanvas.create_text(25, 685, anchor = "nw", font=('Helvetica', 15), fill="white")
            PTcanvas.itemconfig(text_canvas, text="Q10: When using the band saw, plan your cuts carefully. Saw curves gravdually. Sudden twist will cause the" )
            dyPos=725
    for x in range(len(choices)): #creates a for loop to loop for every question there is
        dBox(x) #calls function dropbox with the parameters x to check each drop box


    #SUBMITBUTTON---
    def GetResult(): #creates a procedure called GetResults with no parameters
        PTWindow.destroy() #destroys the PTWindow
        PowResult.ReturnMark(CheckCorrect) #creates a new Window and displays the mark the user got
    Button(PTcanvas, text="Submit Answers", command=GetResult).place(x=850,y=720) #creates a button in the bottome right corner that says submit answer and uses the GetResult procedure as the event when it is hit
    PTWindow.mainloop() #loops the code associated with PTwindow
