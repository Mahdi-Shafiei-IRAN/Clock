import time
import tkinter as tk

root = tk.Tk()
root.title("Clock")
root.geometry("400x300")
root.resizable(0,0)
root.iconbitmap(r"code\icon\clock.ico")

frm = tk.Frame(root,bg="black")
frm.pack(expand=1,fill="both")

label1 = tk.Label(frm, text=time.strftime("%H:%M:%S"), font=("Times", 48),bg="black",fg="red")
label1.place(relx=0.5, rely=0.3, anchor="center")

label2 = tk.Label(frm, text=time.strftime("%Z %Y/%m/%d"), font=("Times", 18),bg="black",fg="green")
label2.place(relx=0.5, rely=0.7, anchor="center")

def showTime():
    text=time.strftime("%I:%M:%S %p")
    label1.config(text=text)
    label1.after(1000,showTime)
showTime()

root.mainloop()