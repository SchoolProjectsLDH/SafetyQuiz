IMPORTANT NOTE
-
This is a temporary file for listing the problems we have encountered during our project. For a more complete rundown of what happened, see the *issues* tab.

Problems
-
Problem 1: the problem would not work, there was an error saying it could not find module Tkinter. This is because to use Tkinter you have to use a lower case _t_ to call it so it would be tkinter
method prior knowledge

- Solution: change all Tkinter to tkinter

Problem 2: Not really a problem but more suggestion, change the name of Background variables to be more detailed on what they mean or at least add comments because it was hard to understand what you were doing with them

- Solved: I renamed the variables

Problem 3: when creating the window for general safety, it would appear before the main page window and the main page will only open when general safety was closed

- Method: prior knowledge I know that order matters and have done multi-window programs before and if I want it to appear in a certain time I have to put it in an if statement that checks for the condition

 - Solution: move the code for creating a new window into the function being called when the button is pressed so it will only appear then


 Problem 4: forgot how to change background colour
 - method prior knowledge I remembered I did it before so I looked at previous

 - solution: use the command .config(bg="colour")
 - still did not work
 - method trial and error
  - tried different colours
  - made sure I spelt it correctly
  - change lower and upper case b
  tried change to .Background()
  - searched up video and it has to be configure(bg="color)")

change 1: move quit button to top right corner
  - reason because it looks more aesthetically pleasing

problem5: unable to create a Label
method trial and error
- try creating a label before the canvas using GSWindow,
  - did not show
- try canvas using my canvas
  - did not show
-probably because did not save when testing
- tried on a brand new Page
  - first tried label by self using gs window
  - it worked
  -then tried before Canvas using gs window
  - it worked
  - but it pushed it down
  - so i tried after Canvas, but still us GSwindow
  - did not show up
  - I thought that maybe canvas goes over it so I changed it to my Canvas
  - it showed up, but colour was off
  - so I changed color

problem 6: position of the Wordbank
trial and error:
- creating a new word bank by drawing a box and using create_text to add the words
problem7: inputting all the options
- solution: use a for loop to put all the options
problem: was just alignment
problem1: all of them would appear in one spot
reason did not change x or y position
solution: create variables for the x and y pos and add to them each loop
problem 2: would continuously go WordDropdown1
solution: once list gets to certain number it would reset x and go to next column
problem 3: all the second column would be in one spot
reason: because it still is greater than 4 so it is reseting y back to origional
solution change it from >=4 to ==4
problem 4 goes outside box
solution: change 4 to 3
problem: when crossing out the word it would say that it wants a int not a tuple
- trial and error
- print out the outputs
- instead of the index command as a parameter for the list use a variable that is set to the index command value
- realize that I am using the list completely wrong and change it to [][] and not [#,#]
problem rewriting unplug on the selected something
- prior knowledge:
 i copied paste the code from the for loop that prints the words, so it must still have x as its parameters and x is the value of unplug



problem 8: unable to append to saves
- trial and error
- first tried .append, but that is not a command you have to use .write
- tried changing the type of file it is (a,w,r)
- tried printing it
- tried it python ide - it worked
- prior knowledge
  - thought that the code will not get there since it is looping the canvas with canvas.mainloop()
  - since I know order matters maybe it has to be before the aforementioned command to work.
  - so tried putting it before it and it worked

problem 9:
problem not able to delete line on words: reason using wrong canvas


problem 10: unable to get text to show on gsWindow
- miss spelt choices so it was an error
- then got first row to worked
- then had to change the xs in lPos[].append(bbox[]) to ys
- changed t1 to choices in the cross for loop
- changed canvas to mycanvas in cross for loop
all these were causing problems that stopped the program from working

problem 11: putting cross on words
- orgigionally have another thing to create a list called cross that holds all the command to create a list, but problem is how to called (see test for code)
- decided to put the cross in the strike function
first time tried it didn't work, only on the last one because I forgot to replace the x with selected for the variable so it would always do the value of x


problem 12: removing line is deteling other stuff, it says that list is out of index range
- trial and error
  - add check parameters to check to see if the cross is equal to command for a line at that certain iteration
  - unable to do that since it is not a string or something (invalid syntax)
  - filled cross with "" blanks then when time comes to draw line it will go to that certain spot in cross and set it to the command to create the line
  - then add command to see if cross at that certain spot is not equal to a blank, if it isn't it will remove the line

problem 13: false was not showing in word blank
- reason: the if statement to change lines had it so after the 5th word (which would be 6th word in reality) would change to the next line, therefore putting false outside the window and making it invisible

problem 14: unable to import powResults
reason had to had .py at end

problem 15: last couple questions on power doc gave wrong answers even if correct
- reason writing to checkcalling[9] and not its own one
- was giving different parameters to striking then the ones that were required (10 instead of 14 if it was the last question)

problem 16 not getting drop box in right position when did procedure
- reason defingin dpPos in procedure so it is local and the global one is not being written to

problem 17 if 2 words are the same for the last word before the drop box it will choice the last one used so the drop box may bot be in the right spot
- solution: make it so it only does it once
problem 18: multiple the is messing up the program because it doesnt know which one to do
- solution :
  if bDB = text
  if str(word == str bDB
    textCount +=1
    if textCount == 2
    dbPos[#].append=qbox[#]
    found my solution
problem 18: drop box 9 and 11 did not show up
- trial and error
- tried putting 9 as 8, it worked and moved onto the next one
- reason is that only one of them has multiple of the same words
- so it still adding to tCount of the other option making it not equal when it goes to assign dbPos
solution add and skip!=0 in the place where they add to tCount
