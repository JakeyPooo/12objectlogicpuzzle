import numpy as np
import random as r
from tkinter import *
import tkinter.messagebox

measureCount = 0
theObjects = np.array([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
flag = 0
while flag < 1:
    theObjects[r.randrange(0, 12)] = r.randrange(1, 4)
    for i in range(0, 12):
        if (theObjects[i] != 2):
            ansObj = theObjects[i]
            flag = 1

def groupSum(x):
    sum = 0
    for i in range(len(x)):
        sum += theObjects[int(x[i]) - 1]
    return(sum)
def popUp():
    print(theObjects)  #TEST
    popUp = Toplevel()
    popUp.title("Object Selection")
    #popUp.geometry("400x400")
    popUp.configure(bg='light green')

    global answer, answerWeight
    answer = IntVar(popUp)
    answerWeight = IntVar(popUp)
    rows = 4
    cols = 3
    count = 0
    for i in range(rows):
        popUp.columnconfigure(i, weight=1, minsize=10)
        popUp.rowconfigure(i, weight=1, minsize=5)
        for j in range(cols):
            image = objImages[count]
            count = count + 1
            Checkbutton(popUp, variable=answer, onvalue=count, indicatoron=False,
                        selectcolor='light blue', offrelief=FLAT, bd=1, image=image,
                        bg='light green', anchor=CENTER).grid(row=i, column=j, padx= 5, pady = 5)

    btnLighter = Checkbutton(popUp, image=imgLighter, variable=answerWeight, onvalue=1, indicatoron=False,
                             bg='light green', selectcolor='light blue', bd=1, offrelief=FLAT)
    btnLighter.grid(row=5, column=0, padx= 5, pady = 5)
    btnHeavier = Checkbutton(popUp, image=imgHeavier, variable=answerWeight, onvalue=3, indicatoron=False,
                             bg='light green', selectcolor='light blue', bd=1, offrelief=FLAT)
    btnHeavier.grid(row=5, column=2, padx= 5, pady = 5)
    btnCheck = Button(popUp, bg='light green', relief='flat', image=btnCheckAnswer, command=checkAnswer)
    btnCheck.grid(row=5, column=1, padx= 5, pady = 5)
def checkAnswer():
    global theObjects, ansObj
    ans = answer.get()
    ans = ans - 1
    ansW = answerWeight.get()
    if(theObjects[ans] == ansW):
        msgBox = "Congratulations!"
        msgAns = "That's correct!"
    else:
        msgBox = "Try again!"
        msgAns = "Sorry, that's incorrect."
    tkinter.messagebox.showinfo(msgBox, msgAns)
    exit()
def var_Get():
    group1 = var_G1.get().split(' ')
    group2 = var_G2.get().split(' ')
    var_G1.set('')
    var_G2.set('')
    sumGroup1 = groupSum(group1)
    sumGroup2 = groupSum(group2)
    print(f' {group1}')
    print(f' {group2}')
    print(f'sumGroup1: {sumGroup1}')
    print(f'sumGroup2: {sumGroup2}')
    print('button pressed')
    if (sumGroup1 > sumGroup2):
        print('group1 > group2')
        addOn = (f'\n{group1} > {group2}')
        previouslyMeasured = prevMeas + addOn
        scaleG1Bigger = PhotoImage(file=r"C:\Users\ander\OneDrive\Pictures\12ObjectsGroup1BiggerScale.png")
        label.configure(image=scaleG1Bigger)
        label.photo = scaleG1Bigger
        previousLabel.configure(text=previouslyMeasured)
    elif (sumGroup1 < sumGroup2):
        print(type(group1))
        print('group1 < group2')
        addOn = (f"{group1} < {group2}")
        previouslyMeasured = prevMeas + addOn
        print(type(previouslyMeasured))
        scaleG2Bigger = PhotoImage(file=r"C:\Users\ander\OneDrive\Pictures\12ObjectsGroup2BiggerScale.png")
        label.configure(image=scaleG2Bigger)
        label.photo = scaleG2Bigger
        previousLabel.configure(text=previouslyMeasured)
    else:
        print('group1 = group2')
        addOn = (f"{group1} = {group2}")
        previouslyMeasured = prevMeas + addOn
        scaleEqual = PhotoImage(file=r"C:\Users\ander\OneDrive\Pictures\12ObjectsEqualScale.png")
        label.configure(image=scaleEqual)
        label.photo = scaleEqual
        previousLabel.configure(text=previouslyMeasured)
def btnPress():
    global measureCount
    measureCount = measureCount + 1
    if measureCount > 2:
        guessButton = PhotoImage(file=r"C:\Users\ander\OneDrive\Pictures\12ObjectsGuessButton.png")
        btnMeasure.configure(image=guessButton, command=popUp)
        btnMeasure.photo = guessButton
    var_Get()

gui = Tk(className="12Objects - LogicPuzzle")
gui.geometry("640x480")
gui.configure(bg='light blue')

object1 = PhotoImage(file=r"C:\Users\ander\OneDrive\Pictures\12ObjectsRock1.png")
object2 = PhotoImage(file=r"C:\Users\ander\OneDrive\Pictures\12ObjectsRock2.png")
object3 = PhotoImage(file=r"C:\Users\ander\OneDrive\Pictures\12ObjectsRock3.png")
object4 = PhotoImage(file=r"C:\Users\ander\OneDrive\Pictures\12ObjectsRock4.png")
object5 = PhotoImage(file=r"C:\Users\ander\OneDrive\Pictures\12ObjectsRock5.png")
object6 = PhotoImage(file=r"C:\Users\ander\OneDrive\Pictures\12ObjectsRock6.png")
object7 = PhotoImage(file=r"C:\Users\ander\OneDrive\Pictures\12ObjectsRock7.png")
object8 = PhotoImage(file=r"C:\Users\ander\OneDrive\Pictures\12ObjectsRock8.png")
object9 = PhotoImage(file=r"C:\Users\ander\OneDrive\Pictures\12ObjectsRock9.png")
object10 = PhotoImage(file=r"C:\Users\ander\OneDrive\Pictures\12ObjectsRock10.png")
object11 = PhotoImage(file=r"C:\Users\ander\OneDrive\Pictures\12ObjectsRock11.png")
object12 = PhotoImage(file=r"C:\Users\ander\OneDrive\Pictures\12ObjectsRock12.png")
Rocks = PhotoImage(file=r"C:\Users\ander\OneDrive\Pictures\RockArrangement.png")
btnCheckAnswer = PhotoImage(file=r"C:\Users\ander\OneDrive\Pictures\12ObjectsCheckAnswer.png")
imgLighter = PhotoImage(file=r"C:\Users\ander\OneDrive\Pictures\12ObjectsLighter.png")
imgHeavier = PhotoImage(file=r"C:\Users\ander\OneDrive\Pictures\12ObjectsHeavier.png")

initialScale = PhotoImage(file = r"C:\Users\ander\OneDrive\Pictures\12ObjectsEqualScale.png")
label = Label(gui, bg='light blue', image = initialScale)
label.place(relx=0.5, rely=0.56, anchor=CENTER)


obj1 = Label(gui, bg='light blue', image = Rocks)
obj1.place(relx=0, rely=1, anchor='sw')


prevMeas = 'Previously Measured:\n'
previousLabel = Label(gui, bg='light blue', text=prevMeas)
previousLabel.place(relx=0.825, rely=0.75, anchor=CENTER)

titleBlock = PhotoImage(file = r"C:\Users\ander\OneDrive\Pictures\12ObjectsTitleBlock.png")
tLabel = Label(gui, bg='light blue', image = titleBlock)
tLabel.place(relx=0.5, rely=0.125, anchor=CENTER)

btnImage = PhotoImage(file = r"C:\Users\ander\OneDrive\Pictures\12ObjectsButton.png")
btnMeasure = Button(gui, bg='light blue', image = btnImage, relief = 'flat')
btnMeasure.place(relx=0.5, rely=0.925, anchor=CENTER)
btnMeasure.configure(command=btnPress)


objImages = [object1, object2, object3, object4, object5, object6,
             object7, object8, object9, object10, object11, object12]
'''
rows = 4
cols = 3
count = 0
for i in range(rows):
    for j in range(cols):
        frame = Frame(master=gui, relief=RAISED, borderwidth=1)
        image = objImages[count]
        count = count + 1
        frame.grid(row=i, column=j)
        btn = Checkbutton(master=frame, onvalue=count, indicatoron=False,
                    selectcolor='light green', offrelief=FLAT, bd=1, image=image,
                    bg='light blue')
        btn.place(relx=0.025, rely=0.52, anchor='w')
'''

var_G1 = StringVar()
var_G2 = StringVar()
entryG1 = Entry(gui, bg='white', textvariable=var_G1, width=15)
entryG1.place(relx=0.025, rely=0.52, anchor='w')
entryG2 = Entry(gui, bg='white', textvariable=var_G2, width=15)
entryG2.place(relx=0.975, rely=0.52, anchor='e')

msgIntro = "Welcome!"
msgInfo = "Hi there! This is my first GUI application all made in Python!\n\n" \
          "A little how-to to get you started on using this application:\n" \
          "1. To measure objects, simply just type the object number into the" \
          " desired entry box.\n" \
          "2. If you want to enter multiple objects into an entry box, separate" \
          " each number by a space, no other character will work! eg. 1 5 8 9\n" \
          "3. After your 3 uses of the scale, press the GUESS button and it will" \
          " and it will bring up another window where you will guess the object" \
          " and its weight using the minus or plus sign.\n\n" \
          "It's that simple! Hope you enjoy!"
tkinter.messagebox.showinfo(msgIntro, msgInfo)

gui.mainloop()