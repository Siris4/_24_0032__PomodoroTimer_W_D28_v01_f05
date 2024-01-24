from tkinter import *

#Dr. Toma, the tomato:

# ---------------------------- CONSTANTS ------------------------------- #
#Colors (in Hex code):
#in layered order from outer-most to inner-most color layers: window background > canvas background >
PINK = "#ED7B7B"
RED = "#E7305B"
GREEN = "#9BDEAC"
YELLOW = "#EBE76C"
ORANGE = "#F0B86E"
PURPLE = "#836096"

#Fonts:
FONT_NAME = "Courier"

#Integers (variable numbers):
WORK_MIN = 50
SHORT_BREAK_MIN = 10
LONG_BREAK_MIN = 30

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()  #either get ahold of the tkinter Module, then the Tk() Class, OR if using a lot of Classes (which we will be doing in this program), then we will just use the .Tk() Class from importing tkinter
#set the title of the window:
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)   #this ACTUALLY ADDS to the original width and height of the original 421x518 window. It won't take AWAY, or keep it the same size, it ADDS to the x and y lengths. So (padx=40, pady=40) would be a total window size of 461x558 pixels.  # https://colorhunt.co/palette/ebe76cf0b86eed7b7b836096 for bg=background_color_of_choice (without using "", because )

fg=GREEN #foreground

checkmark_string = "✔"    #checkmark string version obtained from wikipedia:  https://en.wikipedia.org/wiki/Check_mark

canvas = Canvas(width=430, height=496, bg=YELLOW, highlightthickness=0)  #variable canvas is created from the Canvas Widget  # width and height ar in pixel. # bg=background_color_for_canvas (not using "", since YELLOW is a variable name.  # highlightthickness=0 will get rid of the white line.

#Grid layout will be 3 columns wide and 5 rows down:

# Timer label:
label = Label(text="This is old text")
label.config(text="Timer")
label.grid(column=1, row=0)

#############

tomato_img = PhotoImage(file="tomato4.png") #Also add the image=(PhotoImage datatype Class of tkinter), in order to read through a file and get ahold of a photo at a certain location.  (use Absolute File path, if in another dir). #Also will need to provide a variable name to store this image to (not the Class, but a different variable name of choice, like 'tomato_img'.), then place it after the 'image=' part of the next line:
canvas.create_image(215, 248, image=tomato_img)  #add my image to it, x and y (which are implied, inside) is needed in the (). Because we want the image to be placed right in the center of the window, we divide the dimensions in half, for both, and place those numbers in the paren(). #Also add the image=(PhotoImage datatype Class of tkinter), in order to read through a file and get ahold of a photo at a certain location. Also add the variable after the 'image=' part.
canvas.create_text(214, 305, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))   #this code line needs to be placed before/above we .pack() it. # the implied x and y value are the *args; text="text_here" is the keyword arguments (**kwargs)
canvas.grid(column=1, row=1)   #to actually put it on the screen. Pack is okay for now, til we have to add more components. (changed to grid() )

#############

label = Label(text="This is old text")
label.config(text="Timer")
label.grid(column=1, row=0)





window.mainloop()
