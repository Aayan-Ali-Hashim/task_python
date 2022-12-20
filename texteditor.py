import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext as st

# create the main window

root = tk.Tk()
root.title("Text Editor")
# create a Text widget and set it as the root window's default widget

text = tk.Text(root,font='classic-roman',undo=True,background='#abdbe3')
text.pack(fill="both",expand=True)
# Creating scroll bar
scroll = tk.Scrollbar(root)
scroll.pack(side="right",fill="y")

# Creating undo function

def undo_text():
 text.edit_undo()

def redo_text():
 text.edit_redo()

# Creating copy function

def copy_text():
 text.event_generate("<<Copy>>")

# Creating cut text function

def cut_text():
  text.event_generate("<<Cut>>")


def paste_text():
    text.event_generate("<<Paste>>")
#Creating new file function

def new_file():
    text.delete("1.0","end")
    root.title('New file')

#creating open file function
def open_file():
   path = filedialog.askopenfilename()
   with open(path, "r") as f:
    contents = f.read()

    # Clear the current contents of the Text widget and insert the
    # contents of the opened file
    text.delete("1.0", tk.END)
    text.insert("1.0", contents)
    
def save_file():
    filepath = filedialog.asksaveasfilename(defaultextension=".txt",filetypes=[("Text File", "*.txt*")])
    if filepath:
        # Save the file at the specified location
        with open(filepath, "w") as f:
          f.write(text.get("1.0", "end"))
# adding menu
 
menu_bar = tk.Menu(root) 
file_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_cascade(label="edit",menu=edit_menu)
file_menu.add_command(label='New',command=new_file)
file_menu.add_command(label='Open',command=open_file)
file_menu.add_command(label='Save',command=save_file)
file_menu.add_command(label='Exit',command=root.quit)
edit_menu.add_command(label='Cut',command=cut_text)
edit_menu.add_command(label='Copy',command=copy_text)
edit_menu.add_command(label='Undo',command=undo_text)
edit_menu.add_command(label='Redo',command=redo_text)
edit_menu.add_command(label='Paste',command=paste_text)
root.config(menu = menu_bar)

# Animating text 

def animate_text():
    global message
    message = message[1:] + message[0]
    label.config(text=message)
    root.after(100, animate_text)
message = " AAYAN ALI  "
label = tk.Label(root, text=message,font="Bold",background='seagreen')
label.pack()
animate_text()

root.mainloop()


