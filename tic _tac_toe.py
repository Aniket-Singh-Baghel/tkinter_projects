from tkinter import *
from tkinter import messagebox
import PIL.Image
from PIL import ImageTk,Image

window=Tk()
main_frame=Frame(window)
main_frame.pack(fill=BOTH,expand=TRUE)

bnt1=StringVar()
bnt2=StringVar()
bnt3=StringVar()
bnt4=StringVar()
bnt5=StringVar()
bnt6=StringVar()
bnt7=StringVar()
bnt8=StringVar()
bnt9=StringVar()

click=True
count=0

def img1(num,r,c):
    
    global click,count
    if click==True:
        img = PIL.Image.open("F:\SS\labro.jpg").resize((130,112))
        photo = PIL.ImageTk.PhotoImage(img)
        dog_i = Label(main_frame,image=photo)
        dog_i.image=photo
        dog_i.grid(row=r,column=c)
        if num==1:
            bnt1.set('X')
        elif num==2:
            bnt2.set('X')
        elif num==3:
            bnt3.set('X')
        elif num==4:
            bnt4.set('X')
        elif num==5:
            bnt5.set('X')
        elif num==6:
            bnt6.set('X')
        elif num==7:
            bnt7.set('X')
        elif num==8:
            bnt8.set('X')
        elif num==9:
            bnt9.set('X')
        count+=1
        click=False
        score()
    else:
        img1 = PIL.Image.open("F:\SS\clock-clipart-25.jpg").resize((110,107))
        photo1 = PIL.ImageTk.PhotoImage(img1)
        xok = Label(main_frame,image=photo1)
        xok.image=photo1
        xok.grid(row=r,column=c)
        if num==1:
            bnt1.set('O')
        elif num==2:
            bnt2.set('O')
        elif num==3:
            bnt3.set('O')
        elif num==4:
            bnt4.set('O')
        elif num==5:
            bnt5.set('O')
        elif num==6:
            bnt6.set('O')
        elif num==7:
            bnt7.set('O')
        elif num==8:
            bnt8.set('O')
        elif num==9:
            bnt9.set('O')
        count+=1
        click=True
        score()

def score():
    global count,click
    if(bnt1.get()=='X' and bnt2.get()=='X' and bnt3.get()=='X' or
        bnt4.get()=='X' and bnt5.get()=='X' and bnt6.get()=='X' or
        bnt7.get()=='X' and bnt8.get()=='X' and bnt9.get()=='X' or
        bnt1.get()=='X' and bnt4.get()=='X' and bnt7.get()=='X' or
        bnt2.get()=='X' and bnt5.get()=='X' and bnt8.get()=='X' or
        bnt3.get()=='X' and bnt6.get()=='X' and bnt9.get()=='X' or
        bnt1.get()=='X' and bnt5.get()=='X' and bnt9.get()=='X' or
        bnt3.get()=='X' and bnt5.get()=='X' and bnt7.get()=='X'):
        messagebox.showinfo(title=None,message=("Tic Tac Toe X"))
        print(pl1)
        click=True
        count=0
        clear()
        but()
    elif(bnt1.get()=='O' and bnt2.get()=='O' and bnt3.get()=='O' or
        bnt4.get()=='O' and bnt5.get()=='O' and bnt6.get()=='O' or
        bnt7.get()=='O' and bnt8.get()=='O' and bnt9.get()=='O' or
        bnt1.get()=='O' and bnt4.get()=='O' and bnt7.get()=='O' or
        bnt2.get()=='O' and bnt5.get()=='O' and bnt8.get()=='O' or
        bnt3.get()=='O' and bnt6.get()=='O' and bnt9.get()=='O' or
        bnt1.get()=='O' and bnt5.get()=='O' and bnt9.get()=='O' or
        bnt3.get()=='O' and bnt5.get()=='O' and bnt7.get()=='O'):
        messagebox.showinfo(title=None,message=("Tic Tac Toe "))
        print(pl2)
        count=0
        clear()
        but()
    elif(count==9):
        messagebox.showinfo(title=None,message="Tie",)
        click=True
        count=0
        clear()
        but()

def clear():
    bnt1.set('')
    bnt2.set('')
    bnt3.set('')
    bnt4.set('')
    bnt5.set('')
    bnt6.set('')
    bnt7.set('')
    bnt8.set('')
    bnt9.set('')
pl1=''
pl2=''

def pg1():

    global main_frame,pl1,pl2
    main_frame.destroy()
    main_frame=Frame(window)
    main_frame.pack(fill=BOTH,expand=TRUE)

    p=Label(main_frame,text="Player 1 : ",font=25)
    p.place(x=50,y=50)
    p1_e=Entry(main_frame,font=25)
    p1_e.place(x=100,y=50)

    p2=Label(main_frame,text="Player 2 : ",font=25)
    p2.place(x=50,y=100)
    p2_e=Entry(main_frame,font=25)
    p2_e.place(x=100,y=100)
    
    p_b=Button(main_frame,text="Next>>>>",command=but)
    p_b.place(x=120,y=200)
    p_b.config(width=20,height=2)
    
    pl1=pl1+p1_e.get()
    pl2=pl2+p1_e.get()

l1=Label(main_frame,text="Tic  Tac",font=("Algerian",27))
l1.place(x=120,y=30)
l2=Label(main_frame,text="Toe",font=("Algerian",27))
l2.place(x=150,y=70)

l3=Label(main_frame,text="Let's Go>>>>>>",font=("Times New Roman",17))
l3.place(x=140,y=280)

main_frame.after(2000,pg1)


def but():
    global main_frame
    main_frame.destroy()
    main_frame=Frame(window)
    main_frame.pack(fill=BOTH,expand=TRUE)

    b1=Button(main_frame,text="1",textvariable=bnt1,command=lambda:img1(1,0,0))
    b1.grid(row=0,column=0)
    b1.config(width=18,height=7)

    b2=Button(main_frame,text="2",textvariable=bnt2,command=lambda:img1(2,0,1))
    b2.grid(row=0,column=1)
    b2.config(width=18,height=7)

    b3=Button(main_frame,text="3",textvariable=bnt3,command=lambda:img1(3,0,2))
    b3.grid(row=0,column=2)
    b3.config(width=18,height=7)

    b4=Button(main_frame,text="4",textvariable=bnt4,command=lambda:img1(4,1,0))
    b4.grid(row=1,column=0)
    b4.config(width=18,height=7)

    b7=Button(main_frame,text="5",textvariable=bnt5,command=lambda:img1(5,1,1))
    b7.grid(row=1,column=1)
    b7.config(width=18,height=7)

    b6=Button(main_frame,text="6",textvariable=bnt6,command=lambda:img1(6,1,2))
    b6.grid(row=1,column=2)
    b6.config(width=18,height=7)

    b7=Button(main_frame,text="7",textvariable=bnt7,command=lambda:img1(7,2,0))
    b7.grid(row=2,column=0)
    b7.config(width=18,height=7)

    b8=Button(main_frame,text="8",textvariable=bnt8,command=lambda:img1(8,2,1))
    b8.grid(row=2,column=1)
    b8.config(width=18,height=7)

    b9=Button(main_frame,text="9",textvariable=bnt9,command=lambda:img1(9,2,2))
    b9.grid(row=2,column=2)
    b9.config(width=18,height=7)
    
    e=Button(main_frame,text="Back",command=pg1)
    e.place(x=150,y=355)
    e.config(width=10,height=2)

window.geometry("409x400")
window.mainloop()