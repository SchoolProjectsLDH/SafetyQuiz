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
