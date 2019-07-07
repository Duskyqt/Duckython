#####################################################
# I took an example I found online, added some of my own shit, and here it is.




# Import the necessary libraries/modules for the program
# Tkinter is a standard GUI lib for Python
from tkinter import *
# the Array class will be imported because we need arrays.
from array import *

#Define the window using the Tkinter.Tk() , which we got to shorten by importing all of tkinter.
Window = Tk()
#Name the window
Window.title("Simple Calculator")


# Functions go here

#Add to the Memory array
def MemoryAdd():
    #The .append method will take an argument and insert it at the end of an array
    LastMemory.append(expression)

#Remove from the Memory array
def MemoryRemove():
    #This is a little shorthand for deleting the last indice of an array
    LastMemory[:-1]

#Take the last indice of an array and remove it, and set it to the input text.
def MemoryRecall():
    #the .pop method takes the last indice of an array, removes it, and then InputText.set (InputText is the frame we created for the visual of the calculator text, and .set will set the string of the frame to whatever we pass)
    #The "Try" function will attempt the code I want, and if it fails, it will use hte "Except" function instead, its a failsafe for unwanted errors. 
    #In this example, if the LastMemory array is empty, the .pop() method will return an error.
    try:
        InputText.set(LastMemory.pop())
    except:
        InputText.set("")


#This is a funny easter-egg.
def BonerOutput():
    InputText.set("8========D~~~~")
    
# 'ButtonClick' function continuously updates the input field whenever you enters a number
def ButtonClick(item):
    #we need the global called expression so we define it
    global expression
    #We need the global called LastItem so we define it
    global LastItem
    #We are setting the expression using Concatentation, it is a fancy word for joining strings together. example:
    # "My Name Is " + "Casey" is the same as "My Name Is Casey" but we could substitute these absolute values with variables.
    expression = expression + str(item)
    #Store the last item for future feature I forgot to add lol
    LastItem = item
    #Setting the text again
    InputText.set(expression)

# 'ButtonClear' function clears the input field
def ButtonClear():
    global expression
    expression = ""
    InputText.set("")

# 'ButtonEqual' calculates the expression present in input field
def ButtonEqual():
    global expression
    result = str(eval(expression)) # 'eval' function evalutes the string expression directly
    # you can also implement your own function to evalute the expression instead of 'eval' function
    InputText.set(result)
    #Resetting the expression variable to not have unforseen outcomes by setting it to the result, allowing us to continue adding onto the expresison
    #example: If we just did 2 + 2, and then set the result to 4, using the eval() function, if we didnt reset expression, and tried to add 6 + 6, lets say, it woudl actually be 4 + 4 + 6 + 6 becaues the expression variable was still 4 + 4.
    expression = result

# Remove the last item from the text and expression since we made a mistake. 
def ButtonBack():
    global expression
    expression = expression[:-1]
    InputText.set(expression)

# creating a root menu to insert all the sub menus
RootMenu = Menu(Window)
Window.config(menu = RootMenu)

# creating sub menus in the root menu
FileMenu = Menu(RootMenu) # it intializes a new su menu in the root menu
RootMenu.add_cascade(label = "File", menu = FileMenu) # it creates the name of the sub menu
FileMenu.add_command(label = "Clear", command = ButtonClear) # it adds a option to the sub menu 'command' parameter is used to do some action
FileMenu.add_separator() # it adds a line after the 'Open files' option
FileMenu.add_command(label = "Exit", command = Window.quit)

# creting another sub menu
FunctionsMenu = Menu(RootMenu)
RootMenu.add_cascade(label = "Functions", menu = FunctionsMenu)
FunctionsMenu.add_command(label = "Memory+", command = MemoryAdd)
FunctionsMenu.add_command(label = "Memory-", command = MemoryRemove)
FunctionsMenu.add_command(label = "Memory Recall", command = MemoryRecall)

# Boner menu
BonerMenu = Menu(RootMenu)
RootMenu.add_cascade(label = "Boners", menu = BonerMenu)
BonerMenu.add_command(label = "Show me", command = BonerOutput)

Window.geometry("312x324") # size of the Window width:- 500, height:- 375
Window.resizable(0, 0) # this prevents from resizing the Window
Window.title("Calcualtor")

LastItem = ""
LastMemory = []
expression = ""
# 'StringVar()' is used to get the instance of input field
InputText = StringVar()


# creating a frame for the input field
InputFrame = Frame(Window, width = 312, height = 50, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
InputFrame.pack(side = TOP)


# creating a input field inside the 'Frame'
InputField = Entry(InputFrame, font = ('arial', 18, 'bold'), textvariable = InputText, width = 50, bg = "#eee", bd = 0, justify = RIGHT)
InputField.grid(row = 0, column = 0)
InputField.pack(ipady = 10) # 'ipady' is internal padding to increase the height of input field


# creating another 'Frame' for the button below the 'InputFrame'
ButtonFrame = Frame(Window, width = 312, height = 272.5, bg = "grey")
ButtonFrame.pack()


# first row
clear = Button(ButtonFrame, text = "C", fg = "black", width = 21, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: ButtonClear()).grid(row = 0, column = 0, columnspan = 2, padx = 1, pady = 1)
back = Button(ButtonFrame, text = "<--", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: ButtonBack()).grid(row = 0, column = 2, padx = 1, pady = 1)
divide = Button(ButtonFrame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: ButtonClick("/")).grid(row = 0, column = 3, padx = 1, pady = 1)


# second row
seven = Button(ButtonFrame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: ButtonClick(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
eight = Button(ButtonFrame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: ButtonClick(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
nine = Button(ButtonFrame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: ButtonClick(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
multiply = Button(ButtonFrame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: ButtonClick("*")).grid(row = 1, column = 3, padx = 1, pady = 1)


# third row
four = Button(ButtonFrame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: ButtonClick(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
five = Button(ButtonFrame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: ButtonClick(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
six = Button(ButtonFrame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: ButtonClick(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
minus = Button(ButtonFrame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: ButtonClick("-")).grid(row = 2, column = 3, padx = 1, pady = 1)


# fourth row
one = Button(ButtonFrame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: ButtonClick(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
two = Button(ButtonFrame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: ButtonClick(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
three = Button(ButtonFrame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: ButtonClick(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
plus = Button(ButtonFrame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: ButtonClick("+")).grid(row = 3, column = 3, padx = 1, pady = 1)


# fourth row
zero = Button(ButtonFrame, text = "0", fg = "black", width = 21, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: ButtonClick(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
point = Button(ButtonFrame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: ButtonClick(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
equals = Button(ButtonFrame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: ButtonEqual()).grid(row = 4, column = 3, padx = 1, pady = 1)

#This is a method given by the tkinter module that will return us to the top of the file so it doesn't close. 
Window.mainloop()