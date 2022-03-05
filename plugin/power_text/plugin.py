import tkinter
from tkinter import *

class Plugin():

    def __init__(self, root):
        self.root = root
        self.root.plugin.add_command(label="Grep",command=self.action)
        self.grep_text = None
        
    def action(self):
        print("action")

        
        newWindow = tkinter.Toplevel(self.root.root)
 
        newWindow.title("New Window")
    
        newWindow.geometry("300x400")
    
        # A Label widget to show in toplevel
        tkinter.Label(newWindow,
            text ="grep").pack()
        self.grep_text = tkinter.Text(newWindow, height = 5, width = 52)
        self.grep_text.pack()
        button_grep = tkinter.Button(newWindow, text ="grep", command = self.grep_line).pack()

    def grep_line(self):
        grep_text = self.grep_text.get("1.0","end-1c")
        content = self.root.txtarea.get("1.0","end-1c")
        self.root.txtarea.delete("1.0",END)
        replace_to = []
        for line in content.split("\n"):
            if line.find(grep_text)>=0:
                replace_to.append(line)
        
        
        self.root.txtarea.insert(END,"\n".join(replace_to))
