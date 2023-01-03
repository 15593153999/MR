from random import*
import time
import tkinter as tk
import tkinter.messagebox as messagebox

ab=0
ac=0
x1=0
y1=0
z1=0
a1=0
ar=0
root=0
root=0
qs=1
xz=0
def pd():
    global x1
    global y1
    global entry1
    global ar
    global qs
    global ab
    global z1

    a = entry1.get()
    
    ab=float(ab)
    if qs >= ab:
        root.destroy()
    else:
        if a.isdigit():
            a=int(a)
                
            if a==z1:
                if qs >= ab:
                    messagebox.showwarning('','正确')
                    time.sleep(3)
                    root.destroy()
                else:
                    messagebox.showwarning('','正确')
                    qs=qs+1
                    ct()
            else:
                messagebox.showwarning('','错误，请重试')
       
        else:
            messagebox.showwarning('警告','请正确输入数字')
  
def jf():
    global x1
    global y1
    global lc
    global root
    global entry1
    global ab
    global root
    global z1
    x1=str(randint(1,100))
    y1=str(randint(1,100))
    x2=int(x1)
    y2=int(y1)
    z1=x2+y2
    z2=x1+'+'+y1+'=?'
    av=tk.Label(root,text=z2,font=('Arial', 18),width=15, height=2).place(x=0,y=0,anchor='nw')
    serch()
def jianfa():
    global x1
    global y1
    global lc
    global root
    global entry1
    global ab
    global root
    global z1
    x1=str(randint(50,100))
    y1=str(randint(1,50))
    x2=int(x1)
    y2=int(y1)
    z1=x2-y2
    z2=x1+'-'+y1+'=?'
    av=tk.Label(root,text=z2,font=('Arial', 15),width=15, height=2).place(x=0,y=0,anchor='nw')
    serch()
def cf():
    global x1
    global y1
    global lc
    global root
    global entry1
    global ab
    global root
    global z1
    x1=str(randint(1,15))
    y1=str(randint(1,15))
    x2=int(x1)
    y2=int(y1)
    z1=x2*y2
    z2=x1+'x'+y1+'=?'
    av=tk.Label(root,text=z2,font=('Arial', 15),width=15, height=2).place(x=0,y=0,anchor='nw')
    serch()
def serch():
    global x1
    global y1
    global lc
    global root
    global entry1
    global ab
    az=tk.Label(root,text='请输入答案：',font=('Arial', 10),width=15, height=2).place(x=0,y=100,anchor='nw')
    entry1 = tk.Entry(root,textvariable=v1,width=20)
    entry1.place(x=100,y=110,anchor='nw')
    button1 = tk.Button(root,text='确认',height = 2, width = 10,command=pd).place(x=150,y=200,anchor='nw')
    
     


def clearAll():
    window.delete(tk.ALL)

def e():
    global ab
    ab=3
def e1():
    global ab
    ab=0
def f():
    global ab
    ab=20
def g():
    global ab
    ab=30
    
def a3():
    global xz
    xz=0   
def b3():
    global xz
    xz=1   
def c3():
    global xz
    xz=2
def d3():
    global xz
    xz=3

def j():
    global ac
    ac=0
def k():
    global ac
    ac=1

    
def change_state():
    global root
    global ar
    global ac
    global ab
    if ab ==0:
        ab=entry2.get()
    else:
        ab = str(ab)
    root = tk.Tk()
    root.geometry('500x300')
    root.title('算数训练器4.0')
    root.attributes("-toolwindow", 2)
    root.attributes('-topmost', 'true')
    root.protocol("WM_DELETE_WINDOW", callback)
    ct()
def ct():
    global xz
    global root
    global ar
    global ac
    global ab
    if xz == 0:
        jf()
    elif xz == 1:
        jianfa()
    elif xz == 2:
        cf()
    else:
        asd=randint(0,2)
        if asd == 0:
            jf()
        elif asd == 1:
            jianfa()
        else:
            cf()
        
    
def callback():
    messagebox.showwarning('警告','回答问题')
def back():
    window.destroy()
window = tk.Tk()
var=tk.StringVar()
r=tk.StringVar()
lc=tk.StringVar()
v1 = tk.StringVar()
window.geometry('500x300')
window.title('算数训练器4.0')
window.resizable ( 0, 0)
window.attributes("-toolwindow", 2)


ar=tk.StringVar()
az=tk.Label(window,text='请选择题目数量：',font=('Arial', 10),width=15, height=2).place(x=0,y=60,anchor='nw')
ax=tk.Label(window,text='选择题型：：',font=('Arial', 10),width=15, height=2).place(x=150,y=60,anchor='nw')
av=tk.Label(window,text='算数训练器4.0',font=('华文行楷', 15,"italic"),width=15, height=2).place(x=0,y=0,anchor='nw')
#entry= tk.Entry(window,width=5)
#entry.place(x=260,y=130,anchor='nw')

x=tk.Radiobutton(window,text='10道' ,variable=var, value='10',command=e).place(x=50,y=100,anchor='nw')
y=tk.Radiobutton(window,text='20道' ,variable=var, value='20',command=f).place(x=50,y=130,anchor='nw')
z=tk.Radiobutton(window,text='30道' ,variable=var, value='30',command=g).place(x=50,y=160,anchor='nw')
x1=tk.Radiobutton(window,text='自定义:' ,variable=var, value='自定义',command=e1).place(x=50,y=190,anchor='nw')
entry2= tk.Entry(window,width=5)
entry2.place(x=120,y=190,anchor='nw')

xcv=tk.Radiobutton(window,text='加法' ,variable=r, value='加法',command=a3).place(x=200,y=100,anchor='nw')
ycv=tk.Radiobutton(window,text='减法' ,variable=r, value='减法',command=b3).place(x=200,y=130,anchor='nw')
zcv=tk.Radiobutton(window,text='乘法' ,variable=r, value='乘法',command=c3).place(x=200,y=160,anchor='nw')
gcv=tk.Radiobutton(window,text='综合' ,variable=r, value='综合',command=d3).place(x=200,y=190,anchor='nw')

'''o=tk.Radiobutton(window,text='不限时' ,variable=r, value='10',command=j).place(x=200,y=100,anchor='nw')
p=tk.Radiobutton(window,text='限时:' ,variable=r, value='20',command=k).place(x=200,y=130,anchor='nw')
q=tk.Label(window,text='s',font=('Arial', 10),width=1, height=1).place(x=300,y=132,anchor='nw')'''

button = tk.Button(window,text='确认开始',height = 2, width = 10,command=change_state).place(x=120,y=250,anchor='nw')
button1 = tk.Button(window,text='退出',height = 2, width = 10,command=back).place(x=270,y=250,anchor='nw')

window.mainloop()

    
