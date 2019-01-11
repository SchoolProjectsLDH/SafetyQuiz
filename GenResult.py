from sys import version_info
if version_info.major == 2:
    from Tkinter import *
elif version_info.major == 3:
    from tkinter import *
def ReturnMark(ans):
    #Variables
    backgroundcolour = "#460000"#Background color set with hex
    correct = 0.0 #Variable to store the amount of correct answers
    saves=open("saves","a")#Saves file for recording mark

    #Creating tkinter window
    ResWindow=Tk()#Declaring tkinter window with alias ResWindow
    ResWindow.title("Result")#Setting title of window
    ResWindow.geometry("1000x800")#Size of window (1000px by 800px)
    ResWindow.resizable(False,False)#Make it non-resizable

    #Creating window canvas
    canvas = Canvas(ResWindow, width = 1000, height = 800)#Creating overlay canvas for freedom of placeement
    canvas.create_rectangle(0, 0, 1000, 8000, fill = backgroundcolour)#Placing canvas over window (10X scale factor)
    canvas.pack(side = "top", fill = "both", expand = True)#compiles canvas for the top left side of window and fills to window

    #Window content
    Label(canvas,text="Your Result",font=("Helvetica",30),bg= backgroundcolour,fg="white").place(x=500,y=25,anchor=CENTER)#Title
    for iteration in range(0,len(ans)):#Count correct answers
        if ans[iteration] == True:#If the CheckCorrect has "True" it means that question was correct
            correct += 1#Add one to correct answers
    mark = (correct/10)*100#Calculating percentage mark
    text = str(mark) + "%"#Text for the saves file
    Label(canvas,text="You got {} out of 10 correct".format(int(correct)),font=("Helvetica",20),bg=backgroundcolour,fg="white").place(x=500,y=200, anchor=CENTER) #Tell user how many questions they got right
    Label(canvas,text="{}{}".format(mark,"%"),font=("Helvetica",60),fg="white",bg=backgroundcolour).place(x=500,y=350, anchor = CENTER)#Tell user their percentage mark
    #Special info for the users reference later
    Label(canvas,text="Open the home window which is minimized below to choose another category.\n Keep this window open for later reference.",font=("Helvetica",15),bg=backgroundcolour,fg="white").place(x=500,y=700,anchor=CENTER)

    #Saving to file
    saves.write("General Safety Quiz: {}".format(text) + "\n")#Write to the saves file
    saves.close()#Closes file

    #End of program
    ResWindow.mainloop()
