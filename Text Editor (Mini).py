# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 19:26:36 2021

@author: HP
"""
from tkinter import * 
from PIL import ImageTk, Image
from tkinter import filedialog
import os

root=Tk()
root.minsize(650,650)
root.maxsize(650,650)

open_img = ImageTk.PhotoImage(Image.open("open.png"))
save_img = ImageTk.PhotoImage(Image.open("save.png"))
exit_img = ImageTk.PhotoImage(Image.open("exit.jpg"))

name = ""
def OpenFile():
    global name
    input_file_name.delete(0,END)
    myText.delete(1.0,END)
    text_file = filedialog.askopenfilename(title="Open Text File",filetypes=(("Text Files","*.txt"),))
    print(text_file)
    name = os.path.basename(text_file)
    formated_name = name.split('.')[0]
    input_file_name.insert(END,formated_name)
    root.title(formated_name)
    text_file = open(name,'r')
    paragraph = text_file.read()
    myText.insert(END,paragraph)
    text_file.close()
    
def save():
    input_name = input_file_name.get()
    file = open(input_name+".txt","w")
    data = myText.get("1.0",END)
    print(data)
    file.write(data)
    input_file_name.delete(0,END) 
    myText.delete(1.0,END)
    messagebox.showinfo("Succes","Saved!")
    
def closeWindow():
    root.destroy()

label_file = Label(root,text="File Name: ")
label_file.place(relx=0.28,rely=0.03,anchor=CENTER)

input_file_name = Entry(root)
input_file_name.place(relx=0.46,rely=0.03,anchor=CENTER)

myText = Text(root,height=35,width=80)
myText.place(relx=0.5,rely=0.55,anchor=CENTER)

open_btn = Button(root,image = open_img,command = OpenFile)
open_btn.place(relx=0.05,rely=0.03,anchor=CENTER)

save_button = Button(root,image=save_img,text="Save",command=save)
save_button.place(relx=0.11,rely=0.03,anchor=CENTER)

exit_btn = Button(root,image=exit_img,text="Exit",command=closeWindow)
exit_btn.place(relx=0.17,rely=0.03,anchor=CENTER)

root.mainloop()