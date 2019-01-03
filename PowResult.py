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
    PTRcanvas = Canvas(ResWindow, width = 1000, height = 800)
    PTRcanvas.create_rectangle(0, 0, 1000, 8000, fill = "#38761d")
    PTRcanvas.pack(side = "top", fill = "both", expand = True)
    Label(PTRcanvas,text="Your Result",font=("Helvetica",30),bg="#38761d",fg="white").place(x=500,y=50,anchor=CENTER)
    for iteration in range(0,len(ans)):
        if ans[iteration] == True:
            correct += 1
    mark = (correct/14)*100
    text = str(round(mark,2)) + "%"
    Label(PTRcanvas,text="You got {} out of 14 correct".format(int(correct)),font=("Helvetica",20),bg="#38761d",fg="white").place(x=500,y=200, anchor=CENTER)
    Label(PTRcanvas,text=text,font=("Helvetica",60),fg="white",bg="#38761d").place(x=400,y=350)
    print(ans)
    saves.write("Power Tool Quiz: {}".format(str(text)) + "\n")
    saves.close()
    ResWindow.mainloop()
