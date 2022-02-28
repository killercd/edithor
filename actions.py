from tkinter import messagebox
from tkinter import filedialog
from tkinter import *

class Actions():
    def __init__(self, root):
        self.root = root
    def settitle(self):
        if self.root.filename:
            self.root.title.set(self.root.filename)
        else:
            self.root.title.set("Untitled")

    def newfile(self,*args):
        self.root.txtarea.delete("1.0",END)
        self.root.filename = None
        self.settitle()
        self.root.status.set("New File Created")

    def openfile(self,*args):
        try:
            self.root.filename = filedialog.askopenfilename(title = "Select file",filetypes = (("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py")))
            if self.root.filename:
                infile = open(self.root.filename,"r")
                self.root.txtarea.delete("1.0",END)
                for line in infile:
                    self.root.txtarea.insert(END,line)
                infile.close()
                self.settitle()
                self.root.status.set("Opened Successfully")
        except Exception as e:
            messagebox.showerror("Exception",e)

    def savefile(self,*args):
        try:
            if self.root.filename:
                data = self.root.txtarea.get("1.0",END)
                outfile = open(self.root.filename,"w")
                outfile.write(data)
                outfile.close()
                self.settitle()
                self.root.status.set("Saved Successfully")
            else:
                self.saveasfile()
        except Exception as e:
            messagebox.showerror("Exception",e)

    def saveasfile(self,*args):
        try:
            untitledfile = filedialog.asksaveasfilename(title = "Save file As",defaultextension=".txt",initialfile = "Untitled.txt",filetypes = (("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py")))
            data = self.root.txtarea.get("1.0",END)
            outfile = open(untitledfile,"w")
            outfile.write(data)
            outfile.close()
            self.root.filename = untitledfile
            self.settitle()
            self.root.status.set("Saved Successfully")
        except Exception as e:
            messagebox.showerror("Exception",e)

    def exit(self,*args):
        op = messagebox.askyesno("WARNING","Your Unsaved Data May be Lost!!")
        if op>0:
            self.root.root.destroy()
        else:
            return

    def cut(self,*args):
        self.root.txtarea.event_generate("<<Cut>>")

    def copy(self,*args):
        self.root.txtarea.event_generate("<<Copy>>")

    def paste(self,*args):
        self.root.txtarea.event_generate("<<Paste>>")

    def undo(self,*args):
        try:
            if self.root.filename:
                self.root.txtarea.delete("1.0",END)
                infile = open(self.root.filename,"r")
                for line in infile:
                    self.root.txtarea.insert(END,line)
                infile.close()
                self.settitle()
                self.root.status.set("Undone Successfully")
            else:
                self.root.txtarea.delete("1.0",END)
                self.root.filename = None
                self.settitle()
                self.root.status.set("Undone Successfully")
        except Exception as e:
            messagebox.showerror("Exception",e)

    def infoabout(self):
        messagebox.showinfo("About Text Editor","A Simple Text Editor\nCreated using Python.")

    def shortcuts(self):
        self.root.txtarea.bind("<Control-n>",self.newfile)
        self.root.txtarea.bind("<Control-o>",self.openfile)
        self.root.txtarea.bind("<Control-s>",self.savefile)
        #self.root.txtarea.bind("<Control-a>",self.root.saveasfile)
        self.root.txtarea.bind("<Control-e>",self.exit)
        self.root.txtarea.bind("<Control-x>",self.cut)
        self.root.txtarea.bind("<Control-c>",self.copy)
        self.root.txtarea.bind("<Control-v>",self.paste)
        self.root.txtarea.bind("<Control-u>",self.undo)