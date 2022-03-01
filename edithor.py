from curses import COLOR_BLACK
from tkinter import *
from turtle import bgcolor
from actions import Actions
from os import walk

from plugin.power_text.plugin import Plugin


class TextEditor:

  def __init__(self,root):
    self.root = root
    self.root.title("Edi Thor")
    self.root.geometry("1200x700+200+150")
    self.filename = None
    self.title = StringVar()
    self.status = StringVar()
    self.actions = Actions(self)
    self.titlebar = Label(self.root,textvariable=self.title,font=("times new roman",15,"bold"),bd=2,relief=GROOVE)
    self.titlebar.pack(side=TOP,fill=BOTH)
    self.actions.settitle()

    self.statusbar = Label(self.root,textvariable=self.status,font=("times new roman",15,"bold"),bd=2,relief=GROOVE)
    self.statusbar.pack(side=BOTTOM,fill=BOTH)
    #self.status.set("Welcome To Text Editor")

    self.menubar = Menu(self.root,font=("times new roman",15,"bold"),activebackground="skyblue")
    self.root.config(menu=self.menubar)

    self.filemenu = Menu(self.menubar,font=("times new roman",12,"bold"),activebackground="skyblue",tearoff=0)
    self.filemenu.add_command(label="New",accelerator="Ctrl+N",command=self.actions.newfile)
    self.filemenu.add_command(label="Open",accelerator="Ctrl+O",command=self.actions.openfile)
    self.filemenu.add_command(label="Save",accelerator="Ctrl+S",command=self.actions.savefile)
    self.filemenu.add_command(label="Save As",accelerator="Ctrl+A",command=self.actions.saveasfile)
    self.filemenu.add_separator()
    self.filemenu.add_command(label="Exit",accelerator="Ctrl+E",command=self.actions.exit)
    self.menubar.add_cascade(label="File", menu=self.filemenu)

    
    
    

    self.editmenu = Menu(self.menubar,font=("times new roman",12,"bold"),activebackground="skyblue",tearoff=0)
    self.editmenu.add_command(label="Cut",accelerator="Ctrl+X",command=self.actions.cut)
    self.editmenu.add_command(label="Copy",accelerator="Ctrl+C",command=self.actions.copy)
    self.editmenu.add_command(label="Paste",accelerator="Ctrl+V",command=self.actions.paste)
    self.editmenu.add_separator()
    self.editmenu.add_command(label="Undo",accelerator="Ctrl+U",command=self.actions.undo)
    self.menubar.add_cascade(label="Edit", menu=self.editmenu)

    self.helpmenu = Menu(self.menubar,font=("times new roman",12,"bold"),activebackground="skyblue",tearoff=0)
    self.helpmenu.add_command(label="About",command=self.actions.infoabout)
    self.menubar.add_cascade(label="Help", menu=self.helpmenu)


    self.plugin = Menu(self.menubar,font=("times new roman",12,"bold"),activebackground="skyblue",tearoff=0)
    
    self.menubar.add_cascade(label="Plugin", menu=self.plugin)

    from plugin.power_text import plugin
    ptext_plugin = Plugin(self)


    scrol_y = Scrollbar(self.root,orient=VERTICAL)
    scrol_x = Scrollbar(self.root,orient=HORIZONTAL)
    self.txtarea = Text(self.root,
                        xscrollcommand=scrol_x.set, 
                        yscrollcommand=scrol_y.set,
                        font=("times new roman",12,"bold"),
                        state="normal",
                        relief=GROOVE,
                        background="black",
                        foreground="white",
                        insertbackground="white",
                        wrap=NONE
                        )


    
    scrol_y.pack(side=RIGHT,fill=Y)
    scrol_y.config(command=self.txtarea.yview)
    self.txtarea.pack(fill=BOTH,expand=1)

    self.actions.shortcuts()

  

root = Tk()
TextEditor(root)
root.mainloop()
