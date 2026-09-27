import tkinter
from tkinter import *
from tkinter import messagebox
r=Tk()
r.title('Exam')
r.geometry("700x700")
c=Canvas(r)
global numq
def select_Q():
    import random
    L=[]
    for i in range(5):
        while(True):
            x=random.randint(1,15)
            if x not in L:
                L.append(x)
                break
    return L       
def start_Q():
    global numq
    numq=select_Q()
    import pandas as pd
    d=read_excel('questions.xlsx')
    s1=list(d["titr"])
    s2=list(d["g1"])
    s3=list(d["g2"])
    s4=list(d["g3"])
    s5=list(d["g4"])
    l2=Label(r,text=s1[numq[0]-1],font=("tahoma",12),bg="white")
    l2.place(relx=0.05,rely=0.18,relwidth=0.9,relheight=0.12)
    l22=Label(r,text=s2[numq[0]-1],font=("tahoma",10),bg="gray")
    l22.place(relx=0.05,rely=0.19,relwidth=0.25,relheight=0.12)
    l23=Label(r,text=s3[numq[0]-1],font=("tahoma",10),bg="gray")
    l23.place(relx=0.30,rely=0.19,relwidth=0.25,relheight=0.12)
    l24=Label(r,text=s4[numq[0]-1],font=("tahoma",10),bg="gray")
    l24.place(relx=0.55,rely=0.19,relwidth=0.25,relheight=0.12)
    l25=Label(r,text=s5[numq[0]-1],font=("tahoma",10),bg="gray")
    l25.place(relx=0.80,rely=0.19,relwidth=0.25,relheight=0.12)


    
    l3=Label(r,text=s1[numq[1]-1],font=("tahoma",12),bg="white")
    l3.place(relx=0.05,rely=0.31,relwidth=0.9,relheight=0.12)
    l33=Label(r,text=s2[numq[1]-1],font=("tahoma",10),bg="gray")
    l33.place(relx=0.05,rely=0.32,relwidth=0.25,relheight=0.12)
    l34=Label(r,text=s3[numq[1]-1],font=("tahoma",10),bg="gray")
    l34.place(relx=0.30,rely=0.32,relwidth=0.25,relheight=0.12)
    l35=Label(r,text=s4[numq[1]-1],font=("tahoma",10),bg="gray")
    l35.place(relx=0.55,rely=0.32,relwidth=0.25,relheight=0.12)
    l36=Label(r,text=s5[numq[1]-1],font=("tahoma",10),bg="gray")
    l36.place(relx=0.80,rely=0.32,relwidth=0.25,relheight=0.12)



 
    l4=Label(r,text=s1[numq[2]-1],font=("tahoma",12),bg="white")
    l4.place(relx=0.05,rely=0.44,relwidth=0.9,relheight=0.12)
    l44=Label(r,text=s2[numq[2]-1],font=("tahoma",10),bg="gray")
    l44.place(relx=0.05,rely=0.45,relwidth=0.25,relheight=0.12)
    l45=Label(r,text=s3[numq[2]-1],font=("tahoma",10),bg="gray")
    l45.place(relx=0.30,rely=0.45,relwidth=0.25,relheight=0.12)
    l46=Label(r,text=s4[numq[2]-1],font=("tahoma",10),bg="gray")
    l46.place(relx=0.55,rely=0.45,relwidth=0.25,relheight=0.12)
    l47=Label(r,text=s5[numq[2]-1],font=("tahoma",10),bg="gray")
    l47.place(relx=0.80,rely=0.45,relwidth=0.25,relheight=0.12)


    
    l5=Label(r,text=s1[numq[3]-1],font=("tahoma",12),bg="white")
    l5.place(relx=0.05,rely=0.57,relwidth=0.9,relheight=0.12)
    l55=Label(r,text=s2[numq[3]-1],font=("tahoma",10),bg="gray")
    l55.place(relx=0.05,rely=0.58,relwidth=0.25,relheight=0.12)
    l56=Label(r,text=s3[numq[3]-1],font=("tahoma",10),bg="gray")
    l56.place(relx=0.30,rely=0.58,relwidth=0.25,relheight=0.12)
    l57=Label(r,text=s4[numq[3]-1],font=("tahoma",10),bg="gray")
    l57.place(relx=0.55,rely=0.58,relwidth=0.25,relheight=0.12)
    l58=Label(r,text=s5[numq[3]-1],font=("tahoma",10),bg="gray")
    l58.place(relx=0.80,rely=0.58,relwidth=0.25,relheight=0.12)



    
    l6=Label(r,text=s1[numq[4]-1],font=("tahoma",12),bg="white")
    l6.place(relx=0.05,rely=0.69,relwidth=0.9,relheight=0.12)
    l66=Label(r,text=s2[numq[4]-1],font=("tahoma",10),bg="gray")
    l66.place(relx=0.05,rely=0.70,relwidth=0.25,relheight=0.12)
    l67=Label(r,text=s3[numq[4]-1],font=("tahoma",10),bg="gray")
    l67.place(relx=0.30,rely=0.70,relwidth=0.25,relheight=0.12)
    l68=Label(r,text=s4[numq[4]-1],font=("tahoma",10),bg="gray")
    l68.place(relx=0.55,rely=0.70,relwidth=0.25,relheight=0.12)
    l69=Label(r,text=s5[numq[4]-1],font=("tahoma",10),bg="gray")
    l69.place(relx=0.80,rely=0.70,relwidth=0.25,relheight=0.12)


def show_result():
    global numq
    import pandas as pd
    d=read_excel('questions.xlsx')
    s1=list(d["ans"])
    a=[]
    a.append(int(t1.get()))
    a.append(int(t2.get()))
    a.append(int(t3.get()))
    a.append(int(t4.get()))
    a.append(int(t5.get()))
    c=0
    for i in range(5):
        if(a[i]==s1[numq[i]-1]):
            c+=4
    messagebox.showinfo("show result","your score is = "+str(c))        

             
l1=Label(r,text="Program for Examing.",font=("tahoma",16))
l1.place(relx=0.05,rely=0.05,relwidth=0.9,relheight=0.1)
B1=Button(r,text="Start",command=start_Q)
B1.place(relx=0.4,rely=0.12,relwidth=0.2,relheight=0.05)

l2=Label(r,text=" ",font=("tahoma",12),bg="white")
l2.place(relx=0.05,rely=0.18,relwidth=0.9,relheight=0.12)
t1=Entry(r)
t1.place(relx=0.9,rely=0.18,relwidth=0.1,relheight=0.12)
l3=Label(r,text=" ",font=("tahoma",12),bg="white")
l3.place(relx=0.05,rely=0.31,relwidth=0.9,relheight=0.12)
t2=Entry(r)
t2.place(relx=0.9,rely=0.31,relwidth=0.1,relheight=0.12)
l4=Label(r,text=" ",font=("tahoma",12),bg="white")
l4.place(relx=0.05,rely=0.44,relwidth=0.9,relheight=0.12)
t3=Entry(r)
t3.place(relx=0.9,rely=0.44,relwidth=0.1,relheight=0.12)
l5=Label(r,text="",font=("tahoma",12),bg="white")
l5.place(relx=0.05,rely=0.57,relwidth=0.9,relheight=0.12)
t4=Entry(r)
t4.place(relx=0.9,rely=0.57,relwidth=0.1,relheight=0.12)
l6=Label(r,text="",font=("tahoma",12),bg="white")
l6.place(relx=0.05,rely=0.7,relwidth=0.9,relheight=0.12)
t5=Entry(r)
t5.place(relx=0.9,rely=0.7,relwidth=0.1,relheight=0.12)
B2=Button(r,text="End Exam",command=show_result)
B2.place(relx=0.2,rely=0.88,relwidth=0.2,relheight=0.05)
B3=Button(r,text="Exit",command=r.destroy)
B3.place(relx=0.6,rely=0.88,relwidth=0.2,relheight=0.05)
r.mainloop()
