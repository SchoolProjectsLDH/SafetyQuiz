from sys import version_info
if version_info.major == 2:
    from Tkinter import *
elif version_info.major == 3:
    from tkinter import *
def ReturnMark(ans):
    correct = 0.0
    saves=open("saves","a")
    print("Result")
    ResWindow=Tk()
    ResWindow.title("Result")
    ResWindow.geometry("1000x800")
    ResWindow.resizable(False,False)
    canvas = Canvas(ResWindow, width = 1000, height = 800)
    canvas.create_rectangle(0, 0, 1000, 8000, fill = "black")
    canvas.pack(side = "top", fill = "both", expand = True)
    Label(canvas,text="Your Result",font=("Helvetica",30),bg="black",fg="white").place(x=500,y=25,anchor=CENTER)
    for iteration in range(0,len(ans)):
        if ans[iteration] == True:
            correct += 1
    mark = (correct/10)*100
    text = str(mark) + "%"
    Label(canvas,text="You got {} out of 10 correct".format(int(correct)),font=("Helvetica",20),bg="black",fg="white").place(x=500,y=200, anchor=CENTER)
    Label(canvas,text="{}{}".format(mark,"%"),font=("Helvetica",60),fg="white",bg="black").place(x=400,y=350)
    Label(canvas,text="Open the home window which is minimized below to choose another category. Keep this window open for later reference.",font=("Helvetica",15),bg="black",fg="white").place(x=500,y=700,anchor=CENTER)
    print(ans)
    saves.write("General Safety Quiz: {}".format(str(text)) + "\n")
    saves.close()
    ResWindow.mainloop()
