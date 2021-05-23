from tkinter import *
import threading
from PIL import Image, ImageTk
import time
from random import *
import itertools
from tkinter import messagebox



root=Tk()
score=IntVar()
t=300
def countdown():
    global t, root
    root.title(str(t))
    if t==0:
        messagebox.showinfo("ура","вы продержались 5 минут,так держать!")
        root.destroy()
    t-=1
    root.after(1000, countdown)
countdown()

base = ("base.png")
sleep = ("sleep.png")
dead= ("dead.png")
eat= ("eat.png")
mitb= ("mitb.png")
play1= ("play1.png")
play2= ("play2.png")



canvas = Canvas(root, width = 1280, height =1280)
canvas.place(x=0,y=0)

def load_image1(name):
    img = Image.open(name)
    img.thumbnail((210, 210), Image.ANTIALIAS)
    return ImageTk.PhotoImage(img)


def load_image(name):
    img = Image.open(name)
    img.thumbnail((1280, 1280), Image.ANTIALIAS)
    return ImageTk.PhotoImage(img)

def set_image(image):
    canvas.delete("all")
    canvas.create_image(400, 270,image=base)

base = load_image("base.png")
sleep = load_image("sleep.png")
dead= load_image("dead.png")
eat= load_image("eat.png")
mitb = load_image("mitb.png")
play1 =load_image("play1.png")
play2 =load_image("play2.png")

b1game= load_image1("poigrat.PNG")
b2mit=load_image1("pomit.PNG")
b3corm=load_image1("pokorm.PNG")
b4spat=load_image1("spatt.PNG")



set_image(base)


#добавление к параметру "сытость"


score=IntVar()

def gol():

    sc=score.get()
    sc+=randint(0,4)
    score.set(sc)

    c=v4.get()#энергия
    c =c+ randint(0,8)
    v4.set(c)

    a=v1.get()#сытость
    a+=randint(0,10)
    v1.set(a)


    b=v3.get()#чистота
    b-=randint(0,8)
    v3.set(b)




    canvas.delete("all")
    canvas.create_image(400, 270,image=eat)
    def sm():
        if a>100:
            canvas.delete("all")
            canvas.create_image(400, 270,image=dead)

            messagebox.showwarning("так держать", "питомец лопнул")
            exit()
        if a<=0:
            canvas.delete("all")
            canvas.create_image(400, 270,image=dead)
            messagebox.showwarning("так...", "питомец умер с голоду")
            exit()
    sm()





#добавление к параметру "сытость"
#
#
#добавление к параметру "энергия"
def spat():

    sc=score.get()
    sc+=randint(0,3)
    score.set(sc)

    a1=v4.get()#энергия
    a1 += randint(0,10)
    v4.set(a1)

    b1=v2.get()#счастье
    b1-=randint(0,6)
    v2.set(b1)

    c1=v1.get()#голод
    c1-=randint(0,9)
    v1.set(c1)

    d1=v3.get()#чистота
    d1-=randint(0,8)
    v3.set(d1)



    canvas.delete("all")
    canvas.create_image(400, 270,image=sleep)
    def sm2():
        if a1>100:
            canvas.delete("all")
            canvas.create_image(400, 270,image=dead)
            messagebox.showwarning("так держать", "питомцу приснился рай")
            exit()
        if a1<0:
            canvas.delete("all")
            canvas.create_image(400, 270,image=dead)
            messagebox.showwarning("ессс","питомец умер от недосыпа")
            exit()
    sm2()


#добавление к параметру "энергия"
#
#
#добавление к параметру "чистота"
def mit():

    sc=score.get()
    sc+=randint(0,1)
    score.set(sc)

    a2=v3.get()#чистота
    a2 += randint(0,10)
    v3.set(a2)

    b2=v4.get()#энергия
    b2+=randint(0,8)
    v4.set(b2)

    c2=v2.get()#счастье
    c2+=randint(0,8)
    v2.set(c2)
    if a2>100:
        canvas.delete("all")
        canvas.create_image(400, 270,image=dead)
        messagebox.showwarning("молодец","вы замыли питомца до смерти")
        exit()
    if a2<0:
        canvas.delete("all")
        canvas.create_image(400, 270,image=dead)
        messagebox.showwarning("умничка","питомца разъела грязь")
        exit()
    def sm3():
        if a2>100:
            canvas.delete("all")
            canvas.create_image(400, 270,image=dead)
            messagebox.showwarning("молодец","вы замыли питомца до смерти")
            exit()
        if a2<0:
            canvas.delete("all")
            canvas.create_image(400, 270,image=dead)
            messagebox.showwarning("умничка","питомца разъела грязь")
            exit()

    canvas.delete("all")
    canvas.create_image(400, 270,image=mitb)

    #######
#добавление к параметру "чистота"
#
#
#добавление к параметру "счастье"
def igr():
    sc=score.get()
    sc+=randint(0,1)
    score.set(sc)

    a3=v2.get()#счастье
    a3 += randint(0,10)
    v2.set(a3)

    b3=v3.get()#чистота
    b3-=randint(0,8)
    v3.set(b3)

    c3=v4.get()#энергия
    c3-=randint(0,8)
    v4.set(c3)
    d3=v1.get()#голод
    d3-=randint(0,8)
    v1.set(d3)

    def sm4():
        if a3>100:
            canvas.delete("all")
            canvas.create_image(400, 270,image=dead)
            messagebox.showwarning("юхууу","питомец закопал косточку в землю вместе с собой")
            exit()
        if a3<0:
            canvas.delete("all")
            canvas.create_image(400, 270,image=dead)
            messagebox.showwarning("блиииин...","питомцу стало скучно и он ушел..")
            exit()
    sm4()

    canvas.delete("all")
    canvas.create_image(400, 270,image=play2)







#добавление к параметру "счастье"
#
#
#
root.title("тамагочи")
root.resizable(False, False)
root.geometry("870x560")

v1=IntVar()
v2=IntVar()
v3=IntVar()
v4=IntVar()
a1=IntVar()
a2=IntVar()
a3=IntVar()
a4=IntVar()
v1.set(50)
v2.set(50)
v3.set(50)
v4.set(50)
a1=IntVar()
a2=IntVar()
a3=IntVar()
a4=IntVar()
score=IntVar()



scl=Label(root,text="очков набрано",font=3,bg="#FFB6C1").place(x=700,y=370)
sce=Entry(root,bg="#FFB6C1",textvariable=score).place(x=700,y=400)

l1=Label(root,text="сытость",font=3,bg="#FFB6C1").place(x=50,y=57)
en1=Entry(root,bg="#FFB6C1",textvariable=v1).place(x=70,y=98)


en2=Label(root,text="энергия",font=3,bg="#FFB6C1").place(x=50,y=269)
sc2=Entry(root,bg="#FFB6C1",textvariable=v4).place(x=70,y=313)




l3=Label(root,text="счастье",font=3,bg="#FFB6C1").place(x=700,y=48)
en3=Entry(root,bg="#FFB6C1",textvariable=v2).place(x=720,y=92)


l4=Label(root,text="чистота",font=3,bg="#FFB6C1").place(x=700,y=268)
en4=Entry(root,bg="#FFB6C1",textvariable=v3).place(x=720,y=312)

#кнопки
bt1=Button(root,command=gol,image=b3corm)
bt1.place(x=0, y=450)
bt2=Button(root,image=b4spat,command=spat)
bt2.place(x=215,y=450)
bt3=Button(root,image=b2mit,command=mit)
bt3.place(x=435,y=450)
bt4=Button(root,command=igr,image=b1game)
bt4.place(x=650,y=450)
#кнопки


root.mainloop()
