global Ai
global qustion
global chatbox
global label
global input_field
global starting
starting = 0
chats = []
label = 0
input_field = 0
import tkinter as tk
from tkinter import END
from tkinter import Tk
from tkinter import filedialog
from tkinter import messagebox
import json
with open("verson.json","r") as v:
    data = json.load(v)
    verson = data["verson"]
    chats.append(data["new"])
    chats.append(data["update"])

try:
    import vlc
    p = vlc.MediaPlayer("\python\sound.mp3")
    p.play()
except:
    print("no vlc")
# Create a new window
window = tk.Tk()
# Set the window title
#sets window icon
#with open("D:\python\future Linked Ai\icon_future linked.ico","r+") as icon:
window.iconbitmap("python\icon_future linked.ico")
#playsound.playsound("sound.mp3")
# Set the window size
window.geometry("398x670")
window.maxsize(398,670)
#this part does the answering
import time
import json
import random
Ai = {}
try:
    print("online")
    import urllib.request, json
    with urllib.request.urlopen("https://raw.githubusercontent.com/isaacmaker/Future-Linked-Ai/main/Ai.json") as url:
        Ai = json.load(url)
        with open("python\Ai.json","w") as path_file:
            json.dump(Ai,path_file)
            print("Ai saved")
except:
    try:
        verson = "[not online] " + verson
        with open("python\Ai.json","r") as path_file:
            Ai = json.load(path_file)
    except:
        print("no file")
        window.quit()
window.title("Future Linked "+verson)
Greatings = ["is there any thing else i can help you with?","If you Liked that answer ask me something else","hi my name is Future Linked Ai how can i help you"]
# Open an image file
#with Image.open('background.png') as im:
    # Create a PhotoImage object
 #   photo = ImageTk.PhotoImage(im)

    # Create a label widget
  #  backg = tk.Label(window, image=photo)

    # Set the label widget as the window's main widget
   # backg.grid(column=0,row=0,rowspan=1,columnspan=1)

background = tk.Label(window,bg="black",fg="grey",width=53,height=43,border=20,borderwidth=12,relief="sunken")
background.grid(row=0,column=0,rowspan=15)
def clear():
    global input_field
    global enter
    global answer_label
    global label
    try:
        label.destroy()

        enter.destroy()
        input_field.destroy()
 #   except:
        #print("not there")
        #global qustion_button
        #qustion_button = tk.Button(window,text="question",command=setup,bg="grey",width=15)
        #ustion_button.bind("<>",setup)
        #qustion_button.grid(column=0,row=3)
        setup("answered q")
    except:
        print("fail clear")
def updaten_answer_defs():
        answer = input_field.get()
        Ai.update({qustion: answer})
        print(Ai)
        with open("\python\Ai.json",'w') as f:
            json.dump(Ai,f)
        time.sleep(1)
        clear()

def ask(enter1):
    print(enter1)
    try:
        enter_sound = vlc.MediaPlayer("\python\enter sound.mp3")
        enter_sound.play()
    except:
       print("no vlc")
    global qustion_button
    global label
    global qustion
    global chatbox
    global answer_label
    try:
        qustion_button.destory()
        answer_label.destory()
    except:
        print("no button to clear")

    qustion = input_field.get()
    chats.append("you:  "+qustion)
    #dot_lenth = 0
    #dot_list = [".","..","..."]
    #qustion= input("how how can i help you: ")
    #for a in range(3):
    #if dot_lenth == 4:
     #   print("True")
      #  dot_lenth == 0
    #dot_lenth =+ 1
    #print(dot_lenth)
     #   dot = dot_list[a]
    #print(f"{dot}", end="\r")
    #time.sleep(0.2)
    if qustion in Ai:
        global chatbox
        print(Ai.get(qustion))
        answer_label = tk.Label(window,text=Ai.get(qustion),fg="white",bg="black")
        answer_label.grid(row=2,column=0,)
        chats.append("Ai:  "+Ai.get(qustion))
        print(chats)
        try:
            chatbox.destroy()
            chatbox = tk.Listbox(window,width=60,height=35,background="grey",border=4,)
            chatbox.grid(row=0,column=0)
        except:
            print("cant find anything in the list")
        try:
            for item in chats:
                chatbox.insert(tk.END, item)
                print("added")
        except:
            print("nothing in list")
        clear()
    else:
        #global enter
        #global label
        #qustion = input_field.get()
        #input_field.delete(0, END)
        #label.destroy()
        #enter.destroy()
        #label = tk.Label(window,text="what is the answer?",bg="black",fg="white")
        #label.grid(row=1,column=0)
        #enter = tk.Button(window,text="Enter",command=lambda: ask("hello"))
        #enter.bind("<Return>",ask)
        #enter.grid(row=4,column=0)
        print("hello")
        messagebox.showwarning("no Answer", "i have no answer for that sorry")
        setup("hello")

def clear_chatbox():
    global chats
    global chatbox
    chats = []
    chatbox.destroy()
    chatbox = tk.Listbox(window,width=60,height=35,background="grey",border=4,)
    chatbox.grid(row=0,column=0)
    for item in chats:
        chatbox.insert(tk.END, item)
        print("added")

        
def setup(hello):
        print(hello)
        global starting
        global chatbox
 #       try:
  #          for item in chats:
   #             chatbox.delete()
    #            chatbox.insert(tk.END, item)
     ##  except:
       #     print("nothing in list")
        global label
        global enter
        global input_field
        # Add a label to the window
        try:
            qustion_button.destroy()
            answer_label.destroy()
        except:
            print("no answer to clear")
        if starting == 0:
            label = tk.Label(window, text="Welcome, how can i help you?",bg="black",fg="white",border=8,borderwidth=4,)
            label.grid(row=1,column=0)
        elif starting == 1:
            greet_lenth = len(Greatings)
            greet_str = random.randint(0,greet_lenth-1)
            label = tk.Label(window, text=Greatings[greet_str],bg="black",fg="white",border=8,borderwidth=4,)
            label.grid(row=1,column=0)
        clear_button = tk.Button(window,text="clear",command=clear_chatbox,width=7,bg="grey")
        clear_button.grid(row=4,column=0)            


    # Add an input field to the window
        input_field = tk.Entry(window,width=30,highlightcolor="blue",relief="sunken",border=2,bg="grey")
        input_field.grid(row=2,column=0)
        enter = tk.Button(window,text="Enter",command=lambda: ask("hello"),bg="grey",width=10)
        input_field.bind("<Return>",ask)
        input_field.select_to
        enter.grid(row=3,column=0)
        starting = 1
        window.mainloop()
chatbox = tk.Listbox(window,width=58,height=35,background="grey",border=4,)
chatbox.grid(row=0,column=0)
for item in chats:
    chatbox.insert(tk.END, item)
    print("added")

setup("hello")
    # Run the window