import requests
import json
from tkinter import *
from tkinter import messagebox

#Using the Webistie's API and
def send_message(number,mes):
    url1="https://www.fast2sms.com/dev/bulk"
    diction={"authorization":"ENTER YOUR AUTHORIZATION KEY",
             "sender_id" : "FSTSMS",
             "message":mes,
             "language":"english",
             "route":"p",
             "numbers":number
    }
    responseMes=requests.get(url1,params=diction)
    diction=responseMes.json()
    if responseMes:
        from playsound import playsound
        playsound("success.mp3")
        messagebox.showinfo("SUCCESS", "THE MESSAGE WAS SENT SUCCESSFULLY")
    else:
        from playsound import playsound
        playsound("unsucc.mp3")
        messagebox.showerror("FAILED", "THE MESSAGE WAS NOT SENT")
def click():
    n=numberEntry.get()
    t=mesEntry.get(1.0,END)
    send_message(n,t)

#Designing the GUI of the Application
root= Tk()
root.resizable(width=False, height=False)
root.configure(bg="yellow")
image=PhotoImage(file="spidey.png")
root.iconphoto(True,image)
root.title(" PYTHON MESSAGE SENDER")
root.geometry("500x570")
label = Label(root, text="Enter Phone Number:",font=("Helvetica", 16,"italic"),fg="navy blue",bg="yellow",anchor="w")
label.pack(fill=X)

numberEntry=Entry(root,bg="light yellow",fg="black",font=40)
numberEntry.pack(fill=X,pady=20)
label2 = Label(root, text="Enter the Message:",font=("Helvetica", 16,"italic"),fg="navy blue",bg="yellow",anchor='w')
label2.pack(fill=X)
mesEntry=Text(root,bg="light yellow",fg="brown")
mesEntry.pack()
send=Button(root,text="SEND",height=90,width=10,bg="orange",font="bold",command=click)
send.pack()

root.mainloop()




