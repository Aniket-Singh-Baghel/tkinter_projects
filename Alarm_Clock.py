from tkinter import *
from PIL import ImageTk,Image
from datetime import datetime
from playsound import playsound
import time

window=Tk()
window.config(bg="#778beb")

alarm=None
stop=False
def show_t(l):
    
    def nowtime():
        
        now=datetime.now().strftime("%B %d,%Y  %H:%M %S")
        sa=datetime.now().strftime("%H:%M")
        if sa==alarm and stop==False:
            
            print("Beep")
            
            playsound("F:\salamisound.mp3")
            time.sleep(0.5)
        l.config(text=now)
        l.after(1000,nowtime)
    nowtime()

    
def set_a():
    global stop
    a=set_alarm_e.get()
    global alarm
    if ":" in a:
        alarm=a
    
    stop=False

def stop_a():
    global stop
    al = Label(f,bg="white",text=("Alarm at: ",alarm))
    al.grid(row=6,column=0,columnspan=2)
    # al.config(width=30,height=3)
    stop=True

f=Frame(window,height=500,width=500,bg="#778beb")
f.grid(row=0,column=0,padx=80)

alarm=Label(f,text="Alarm Clock",font=('Times New Roman',24,'bold'),bg="#778beb")
alarm.grid(row=0,column=0,columnspan=2)

img = Image.open('F:\SS\clock-image-transparent-background-19.png').resize((250,250))
photo = ImageTk.PhotoImage(img)
alarm_clock = Label(f,image=photo,bg="#778beb")
alarm_clock.grid(row=1,column=0,columnspan=2,pady=10)

time_s=Label(f,fg="#303952",font=("Century",18),bg="#778beb")
time_s.grid(row=2,column=0,columnspan=2)
show_t(time_s)

set_alam=Label(f,text="Set Alarm ",font=("Century",18),fg="#303952",bg="#778beb")
set_alam.grid(row=3,column=0,pady=15,padx=5)

set_alarm_e=Entry(f,font=18)
set_alarm_e.grid(row=3,column=1,pady=15)

start_b=Button(f,text="Start Alarm",fg="white",bg="#778beb",font=10,command=set_a)
start_b.grid(row=4,column=0,pady=15,sticky="EW")

stop_b=Button(f,text="Stop Alarm",fg="white",bg="#778beb",font=10,command=stop_a)
stop_b.grid(row=4,column=1,pady=15,padx=10,sticky="EW")

exit_b=Button(f,text="Exit",fg="white",bg="#778beb",font=10,command= lambda : window.destroy())
exit_b.grid(row=5,column=0,pady=15,padx=10,columnspan=2,sticky="EW")

window.title("Alarm Clock")
window.geometry("500x600")
window.resizable(False,False)
window.mainloop()