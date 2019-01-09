from sys import version_info
if version_info.major == 2:
    from Tkinter import *
elif version_info.major == 3:
    from tkinter import *
def ReturnHTMark(ans):
    backgroundcolour = "#3A3A8E"
    correct = 0.0
    saves=open("saves","a")
    ResHTWindow=Tk()
    ResHTWindow.title("Result")
    ResHTWindow.geometry("1000x800")
    ResHTWindow.resizable(False,False)
    HTRcanvas = Canvas(ResHTWindow, width = 1000, height = 800)
    HTRcanvas.create_rectangle(0, 0, 1000, 8000, fill = backgroundcolour)
    HTRcanvas.pack(side = "top", fill = "both", expand = True)
    Label(HTRcanvas,text="Your Result",font=("Helvetica",30),bg=backgroundcolour,fg="white").place(x=500,y=50,anchor=CENTER)
    for iteration in range(0,len(ans)):
        if ans[iteration] == True:
            correct += 1
    mark = (correct/10)*100
    text = str(mark) + "%"
    Label(HTRcanvas,text="You got {} out of 10 correct".format(int(correct)),font=("Helvetica",20),bg=backgroundcolour,fg="white").place(x=500,y=200, anchor=CENTER)
    Label(HTRcanvas,text="{}{}".format(mark,"%"),font=("Helvetica",60),fg="white",bg=backgroundcolour).place(x=500,y=350, anchor = CENTER)
    Label(HTRcanvas,text="Open the home window which is minimized below to choose another category.\n Keep this window open for later reference.",font=("Helvetica",15),bg=backgroundcolour,fg="white").place(x=500,y=700,anchor=CENTER)
    saves.write("Hand Tool Quiz: {}".format(str(text)) + "\n")
    saves.close()


    ResHTWindow.mainloop()
