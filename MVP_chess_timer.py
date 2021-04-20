# Python program to illustrate a stop watch 
# using tkinter 
#importing the required libraries 
import tkinter as tkinter 
# note to future self: tkinter is capitalized for python 2, but not for python 3.
  
counterR = 4 * 60 * 60
counterL = 4 * 60 * 60
# the counters are both in the units of "seconds"
running = False
rocker = "L"

def make_string_and_show_two_digits(number):
    if len(str(number)) >= 2:
        return str(number)
    else:
        return "0"+str(number)


def convert_seconds_to_time_format(total_seconds):
    hours = total_seconds // 3600
    minutes = (total_seconds%3600) // 60
    seconds = (total_seconds%3600)%60
    full_timer = make_string_and_show_two_digits(hours)+":"+make_string_and_show_two_digits(minutes)+":"+make_string_and_show_two_digits(seconds)
    return full_timer

def counter_label(label): 
    def count(): 
        if running:
            global rocker
            global counterR 
            global counterL
            global rockerS

            if counterR <=0:             
                rocker = "L"

            if counterL <=0:
                rocker = "R"

            if counterR <= 0 and counterL <= 0:
                rocker = 0

            display=convert_seconds_to_time_format(counterL)+"  "+convert_seconds_to_time_format(counterR) 
  
            label['text']=display   # Or label.config(text=display) 
  
            # label.after(arg1, arg2) delays by  
            # first argument given in milliseconds 
            # and then calls the function given as second argument. 
            # Generally like here we need to call the  
            # function in which it is present repeatedly. 
            # Delays by 1000ms=1 seconds and call count again. 
            label.after(1000, count)  
            if rocker == "R":
                counterR -= 1
            if rocker == "L":
                counterL -= 1
  
    # Triggering the start of the counter. 
    count()
  
# start function of the stopwatch 
def Start(label): 
    global running 
    running=True
    meta_lable['text']=" work           break"
    counter_label(label) 
    start['state']='disabled'
    stop['state']='normal'
    reset['state']='normal'
  
# Stop function of the stopwatch 
def Stop(): 
    global running 
    start['state']='normal'
    stop['state']='disabled'
    reset['state']='normal'
    running = False

# Switch the rocker
def Switch(label): 
    global rocker
    if rocker == "R":
        rocker = "L"
    elif rocker == "L":
        rocker = "R"

# Reset function of the timer
def Reset(label): 
    global counter 
    counter=-1
  
    # If reset is pressed after pressing stop. 
    if running==False:       
        reset['state']='disabled'
        label['text']='Welcome!'
        # reset the counters
        counterR = 4 * 60 * 60
        counterL = 4 * 60 * 60
  
    # If reset is pressed while the stopwatch is running. 
    else:                
        label['text']='Starting...'
  
root = tkinter.Tk() 
root.title("Stopwatch") 
  
# Fixing the window size. 
root.minsize(width=400, height=200) 


label = tkinter.Label(root, text="Welcome!", fg="black", font="Verdana 30 bold") 

meta_lable = tkinter.Label(root, text="", fg="grey", font="Verdana 15 bold") 

meta_lable.pack()
label.pack() 

#this text defines the buttons that call the functions
start = tkinter.Button(root, text='Start',  
width=15, command=lambda:Start(label))

stop = tkinter.Button(root, text='Stop',  
width=15, state='disabled', command=Stop) 

switch = tkinter.Button(root, text='Switch',  
width=15, command=lambda:Switch(label))

reset = tkinter.Button(root, text='Reset', 
 width=15, state='disabled', command=lambda:Reset(label)) 

#this text puts the button in the GUI
start.pack() 
stop.pack()
switch.pack() 
reset.pack() 
root.mainloop() 
