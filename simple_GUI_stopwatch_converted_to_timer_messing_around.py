# Python program to illustrate a stop watch 
# using Tkinter 
#importing the required libraries 
import Tkinter as Tkinter 
# note to future self: Tkinter is capitalized for python 2, but not for python 3.
  
counterR = 20
counterL = 20
running = False
rocker = "R"
def counter_label(label): 
    def count(): 
        if running: 
            global counterR 
            global counterL
            global rocker

            if counterR <=0:             
                rocker = "L"

            if counterL <=0:
                rocker = "R"

            if counterR <= 0 and counterL <= 0:
                rocker = 0

            display=str(counterR)+"  "+str(counterL) 
  
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
  
# Reset function of the stopwatch 
def Reset(label): 
    global counter 
    counter=-1
  
    # If rest is pressed after pressing stop. 
    if running==False:       
        reset['state']='disabled'
        label['text']='Welcome!'
  
    # If reset is pressed while the stopwatch is running. 
    else:                
        label['text']='Starting...'
  
root = Tkinter.Tk() 
root.title("Stopwatch") 
  
# Fixing the window size. 
root.minsize(width=200, height=130) 
label = Tkinter.Label(root, text="Welcome!", fg="black", font="Verdana 30 bold") 
label.pack() 
start = Tkinter.Button(root, text='Start',  
width=15, command=lambda:Start(label)) 
stop = Tkinter.Button(root, text='Stop',  
width=15, state='disabled', command=Stop) 
reset = Tkinter.Button(root, text='Reset', 
 width=15, state='disabled', command=lambda:Reset(label)) 
start.pack() 
stop.pack() 
reset.pack() 
root.mainloop() 
