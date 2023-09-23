import pgzrun
import random
import numpy
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import sys
gt=0
gir=1
rn=1
aispeed=0
able_to_start=0
winner=''
window = Tk()
window.title("First Window")
window.geometry("300x200")
def rc(Type):
    global gt,able_to_start
    gt=Type
    able_to_start=1
r1c=lambda x=1:rc(x)
r2c=lambda x=5:rc(x)
r3c=lambda x=10:rc(x)
def ai(speed):
    global aispeed
    if speed==0:
        aispeed=0
    elif speed==1:
        aispeed=2
    elif speed==2:
        aispeed=4
def start():
    global able_to_start,window
    if able_to_start==0:
        showerror(title="错误",message="请选择赛制及人数！")
    else:
       window.destroy()
no_ai=lambda x=0:ai(x)
slow_ai=lambda x=1:ai(x)
fast_ai=lambda x=2:ai(x)
ft=IntVar()
ft1 = Radiobutton(window, text="一局定胜负", value=1,command=r1c,variable=ft)
ft2 = Radiobutton(window, text="五分赛制", value=2,command=r2c,variable=ft)
ft3 = Radiobutton(window, text="十分赛制", value=3,command=r3c,variable=ft)
aiintvar=IntVar()
ai1 = Radiobutton(window, text="双人游戏", value=1,command=no_ai,variable=aiintvar)
ai2 = Radiobutton(window, text="低速人机", value=2,command=slow_ai,variable=aiintvar)
ai3 = Radiobutton(window, text="高速人机", value=3,command=fast_ai,variable=aiintvar)
aiintvar.set(1)
start_game= Button(window, text="开始游戏",command=start)
label=Label(window,text='请选择赛制与人数')
label.grid(column=1,row=0)
ft1.grid(column=0, row=1)
ft2.grid(column=1, row=1)
ft3.grid(column=2, row=1)
ai1.grid(column=0, row=2)
ai2.grid(column=1, row=2)
ai3.grid(column=2, row=2)
start_game.grid(column=1, row=5)
window.mainloop()
WIDTH=400
HEIGHT=600
pad1=Actor('pad')
pad1.x=200
pad1.y=550
pad2=Actor('pad')
pad2.x=200
pad2.y=50
ball=Actor('ball')
ball.x=200
ball.y=300
speed=2
ymove=random.choice([2,-2])
a=random.randint(0,1)
p1s=0
p2s=0
stt=0
if a==0:
    xmove=random.randint(-speed,-1)
else:
    xmove=random.randint(1,speed)

def draw():
    global gir,winner,aispeed
    screen.fill((0,0,0))
    if gir and rn:
        pad1.draw()
        pad2.draw()
        ball.draw()
        fnt="chinese"
        if aispeed==0:
            screen.draw.text('玩家二分数: '+str(p2s),(20,30),fontname="chinese")
        else:
            screen.draw.text('人机分数: '+str(p2s),(20,30),fontname="chinese")
        screen.draw.text('玩家一分数: '+str(p1s),(250,570),fontname="chinese")
    elif gir==0 and rn==1:
        screen.draw.text(str(winner)+'\n按空格重来\n按Q退出',(125,200),fontname="chinese")
    elif gir==1 and rn==0:
        screen.draw.text('按空格重来\n按G继续\n按Q退出',(125,200),fontname="chinese")
def update():
    global xmove,ymove,stt,speed,p1s,p2s,gt,gir,winner,rn,aispeed
    if gir and rn:
        ball.y+=ymove
        ball.x+=xmove
        if ball.right>=400:
            ball.right=400
            xmove=-xmove
        elif ball.left<=0:
            ball.left=0
            xmove=-xmove
        if keyboard.a and pad1.left>0:
            pad1.x-=5
        if keyboard.d and pad1.right<400:
            pad1.x+=5
        if aispeed==0:
            if keyboard.j and pad2.left>0:
                pad2.x-=5
            if keyboard.l and pad2.right<400:
                pad2.x+=5
        else:
            if pad2.x<ball.x and pad2.right<400:
                pad2.x+=aispeed
            if pad2.x>ball.x and pad2.left>0:
                pad2.x-=aispeed
        if ball.top<=0 or ball.bottom>=600:
            speed=2
            ymove=random.choice([speed,-speed])
            xmove=random.choice(list(range(1,speed+1))+list(range(-speed)))
        if ball.top<=0:
            ball.x=pad2.x
            ball.y=pad2.y+15
            p1s+=1
        if ball.bottom>=600:
            ball.x=pad1.x
            ball.y=pad1.y-15
            p2s+=1
        if (ball.colliderect(pad1) or ball.colliderect(pad2)) and stt==0:
            xmove=random.choice(list(numpy.arange(1.0,speed+1,0.1))+list(numpy.arange(-speed,0.0,0.1)))
            if ymove-ymove<ymove:
                ymove=-speed
            else:
                ymove=speed
            stt=1
            speed+=0.5
        if not (ball.colliderect(pad1) or ball.colliderect(pad2)):
            stt=0
        if p1s>=gt:
            gir=0
            winner='玩家一赢了'
        elif p2s>=gt:
            gir=0
            winner='玩家二赢了' if aispeed==0 else "人机赢了"
        if keyboard.escape:
            rn=0
def on_key_down(key):
    global xmove,ymove,stt,speed,p1s,p2s,gt,gir,winner,rn
    if rn==0 or gir==0:
        if key==keys.SPACE:
            gir=1
            speed=2
            p1s=0
            p2s=0
            winner=''
            ball.x=200
            ball.y=300
            pad1.x=200
            pad1.y=550
            pad2.x=200
            pad2.y=50
            ymove=random.choice([2,-2])
            a=random.randint(0,1)
            stt=0
            if a==0:
                xmove=random.randint(-speed,-1)
            else:
                xmove=random.randint(1,speed)
        if key==keys.Q:
            sys.exit()
    if key==keys.G and rn==0:
        rn=1
            



















pgzrun.go()
