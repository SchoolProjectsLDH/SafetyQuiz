from sys import version_info
if version_info.major == 2:
    from Tkinter import *
elif version_info.major == 3:
    from tkinter import *

saves=open("saves","w")

def ReturnMark(ans):
    correct = 0
    print("Result")
    ResWindow=Tk()
    ResWindow.title("Result")
    ResWindow.geometry("1000x800")
    ResWindow.resizable(False,False)
    canvas = Canvas(ResWindow, width = 1000, height = 800)
    canvas.create_rectangle(0, 0, 1000, 8000, fill = "#38761d")
    canvas.pack(side = "top", fill = "both", expand = True)
    Label(canvas,text="Your Result",font=("Helvetica",30),bg="#38761d",fg="white").place(x=500,y=50,anchor=CENTER)
    for iteration in range(0,len(ans)):
        if ans[iteration] == True:
            correct += 1
    Label(canvas,text="You got {} out of 10 correct".format(correct),font=("Helvetica",20),bg="#38761d",fg="white").place(x=500,y=200, anchor=CENTER)

    mark=(correct/10)*100
    percent=Label(canvas,text="{}{}".format(mark,"%"),font=("Helvetica",60),fg="white",bg="#38761d")
    percent.place(x=400,y=350)
    print(ans)
    ResWindow.mainloop()
    saves.apped(mark)
    saves.close()
    saves.open("saves","r")
    saves.read()
    saves.close()
