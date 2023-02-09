#注意，此代码大约300行，这是此程序唯一的注释，由于此程序历经多次迭代，代码较为繁琐
#非专业人员，请慎重修改
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
mmyz=0
mmsr=0
entry4=0
def pd():
    global x1
    global y1
    global entry1
    global ar
    global qs
    global ab
    global z1
    global root


    a = entry1.get()
    
    ab=float(ab)
    if qs >= ab:
        root.destroy()
        window.destroy()
    else:
        if a.isdigit():
            a=int(a)
                
            if a==z1:
                
                tk.Label(root,text='正确',font=('Arial', 18),fg = 'red',width=15, height=2).place(x=300,y=150,anchor='nw')

                qs=qs+1
                ct()
            else:
                tk.Label(root,text='错误，请重试',font=('Arial', 18),fg = 'red',width=15, height=2).place(x=300,y=150,anchor='nw')
       
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
    x1=str(randint(1,1000))
    y1=str(randint(1,1000))
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
    x1=str(randint(500,1000))
    y1=str(randint(1,500))
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
    x1=str(randint(1,10))
    y1=str(randint(1,100))
    x2=int(x1)
    y2=int(y1)
    z1=x2*y2
    z2=x1+'x'+y1+'=?'
    av=tk.Label(root,text=z2,font=('Arial', 15),width=15, height=2).place(x=0,y=0,anchor='nw')
    serch()
def chufa():
    global x1
    global y1
    global lc
    global root
    global entry1
    global ab
    global root
    global z1
    x1=str(randint(1,10))
    y1=str(randint(1,10))
    x2=int(x1)
    y2=int(y1)
    sa=x2*y2
    sa1=str(sa)
    z1=sa/x2
    z2=sa1+'÷'+x1+'=?'
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
    xz=4
def f3():
    global xz
    xz=3   

def j():
    global ac
    ac=0
def k():
    global ac
    ac=1
def yzcx():
    global mmyz
    global mmsr
    global entry4
    global winroot
    mmsr=entry4.get()
    mmsr=str(mmsr)
    
    if mmyz == mmsr:
        root.destroy()
        window.destroy()
        winroot.destroy()
    else:
        messagebox.showwarning('警告','密码错误')
        
        
    
def mmqrcx():
    global mmyz
    mmyz=entry3.get()
    mmyz=str(mmyz)
    long=len(mmyz)
    if mmyz=='':
        messagebox.showwarning('警告','密码不能为空')
    elif long <=5:
        messagebox.showwarning('警告','密码不足六位')
    else:
        change_state()
        
        

def change_state():
    global root
    global ar
    global ac
    global ab
    global mmyz
    mmyz=entry3.get()
    mmyz=str(mmyz)
    
    if ab ==0:
        ab=entry2.get()
    else:
        ab = str(ab)
    root = tk.Tk()
    root.geometry('500x300')
    root.title('算数训练器5.0')
    root.attributes("-toolwindow", 2)
    root.attributes('-topmost', 'true')
    root.resizable(False, False)
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
    elif xz == 3:
        chufa()
    else:
        asd=randint(0,3)
        if asd == 0:
            jf()
        elif asd == 1:
            jianfa()
        elif asd == 2:
            cf()
        else:
            chufa()
        
    
def callback():
    global entry4
    global winroot
    winroot = tk.Tk()
    winroot.title('算数训练器5.0')
    winroot.geometry('200x100')
    winroot.resizable ( 0, 0)
    winroot.attributes("-toolwindow", 2)
    winroot.attributes('-topmost', 'true')
    tk.Label(winroot,text='请输入管理员密码：',font=('Arial', 10),width=15, height=2).place(x=0,y=0,anchor='nw')
    entry4= tk.Entry(winroot,show='*',width=15)
    entry4.place(x=10,y=30,anchor='nw')
    button = tk.Button(winroot,text='确认',height = 1, width = 4,command=yzcx).place(x=10,y=60,anchor='nw')
def back():
    window.destroy()
def smcx():
    a = tk.Tk()
    a.geometry('500x200')
    a.title('算数训练器5.0')
    a.resizable ( 0, 0)
    a.attributes("-toolwindow", 2)
    tk.Label(a,text='注意：',font=('华文行楷', 15),width=15, height=2).place(x=0,y=0,anchor='nw')
    tk.Label(a,text='1.管理员密码必须为6位以上的数字，大小写字母，不可输入特殊符号',font=('华文行楷', 10),width=70, height=1).place(x=0,y=40,anchor='nw')
    tk.Label(a,text='2.管理员密码为您退出该程序的唯一途径，请务必认真填写且牢记密码',font=('华文行楷', 10),width=70, height=1).place(x=3,y=60,anchor='nw')
    tk.Label(a,text='3.目前版本无法改变题型，现有题型为1000以内加减法与100以内乘除法',font=('华文行楷', 10),width=70, height=1).place(x=7,y=80,anchor='nw')
    tk.Label(a,text='更多程序见https://github.com/15593153999/MR，祝您使用愉快',font=('华文行楷', 10),width=70, height=1).place(x=3,y=100,anchor='nw')
window = tk.Tk()
var=tk.StringVar()
r=tk.StringVar()
lc=tk.StringVar()
v1 = tk.StringVar()
window.geometry('500x300')
window.title('算数训练器5.0')
window.resizable ( 0, 0)
window.attributes("-toolwindow", 2)

ar=tk.StringVar()
az=tk.Label(window,text='请选择题目数量：',font=('Arial', 10),width=15, height=2).place(x=0,y=60,anchor='nw')
ax=tk.Label(window,text='选择题型：',font=('Arial', 10),width=15, height=2).place(x=150,y=60,anchor='nw')
av=tk.Label(window,text='算数训练器5.0',font=('华文行楷', 15,"italic"),width=15, height=2).place(x=0,y=0,anchor='nw')


x=tk.Radiobutton(window,text='10道' ,variable=var, value='10',command=e).place(x=50,y=100,anchor='nw')
y=tk.Radiobutton(window,text='20道' ,variable=var, value='20',command=f).place(x=50,y=130,anchor='nw')
z=tk.Radiobutton(window,text='30道' ,variable=var, value='30',command=g).place(x=50,y=160,anchor='nw')
x1=tk.Radiobutton(window,text='自定义:' ,variable=var, value='自定义',command=e1).place(x=50,y=190,anchor='nw')
entry2= tk.Entry(window,width=5)
entry2.place(x=120,y=190,anchor='nw')
ax=tk.Label(window,text='设置管理员密码：',font=('Arial', 10),width=15, height=2).place(x=300,y=60,anchor='nw')

entry3= tk.Entry(window,show='*',width=15)
entry3.place(x=350,y=90,anchor='nw')

xcv=tk.Radiobutton(window,text='加法' ,variable=r, value='加法',command=a3).place(x=200,y=100,anchor='nw')
ycv=tk.Radiobutton(window,text='减法' ,variable=r, value='减法',command=b3).place(x=200,y=130,anchor='nw')
zcv=tk.Radiobutton(window,text='乘法' ,variable=r, value='乘法',command=c3).place(x=200,y=160,anchor='nw')
hcv=tk.Radiobutton(window,text='除法' ,variable=r, value='除法',command=f3).place(x=200,y=190,anchor='nw')
gcv=tk.Radiobutton(window,text='综合' ,variable=r, value='综合',command=d3).place(x=200,y=220,anchor='nw')


button = tk.Button(window,text='确认开始',height = 2, width = 10,command=mmqrcx).place(x=300,y=200,anchor='nw')
button1 = tk.Button(window,text='退出',height = 2, width = 10,command=back).place(x=400,y=200,anchor='nw')
button2 = tk.Button(window,text='有疑问？',height = 2, width = 10,command=smcx).place(x=350,y=150,anchor='nw')

window.mainloop()

    
