global Ai
global question
global chatbox
global label
global input_field
global starting
import difflib
starting = 0
chats = []
label = 0
input_field = 0
admin = False
str_test = {}
import tkinter as tk
from tkinter import END
from tkinter import Tk
from tkinter import filedialog
from tkinter import messagebox
import time
try:
    from PIL import ImageTk
    from PIL import Image
except:
    print("no PIL")
def wait():
    print("worked")
start_up = tk.Tk()
start_up.title("loading.....")
start_up.iconbitmap("D:\python\icon_future linked.ico")
img = ImageTk.PhotoImage(Image.open(r"D:\python\future linked start up .png"))
start_frame = tk.Frame(start_up,bg="black")
y = img.height()
x = img.width()
y = str(y+2)
x = str(x+2)
xy1 = str(x+"x"+y)
xy = str(xy1+"+400+200")
start_up.geometry(xy)
panel = tk.Label(start_frame, image=img)
start_up.overrideredirect(True)
panel.grid(row=0,column=0)
start_frame.pack()

def main():
    try:
        start_up.destroy()
    except:
        print("not start up")
    import json
    with open("verson.json","r") as v:
        global data

        print("found")
        data = json.load(v)
        verson = data["verson"]
        chats.append("                                                Future Linked",)
        chats.append("                                  "+data["new"])
        chats.append("                                            "+data["update"])

    print("no verson")
    try:

        import urllib.request, json
        with urllib.request.urlopen("https://raw.githubusercontent.com/isaacmaker/Future-Linked-Ai/main/verson.json") as url9:
            verson_check = json.load(url9)
            verson_local = data.get("verson")
            verson_online = verson_check.get("verson")
            print(verson_online)
            if verson_local != verson_online:
                messagebox.showinfo("update","an update is available please upgrade your future linked Ai")
    except:
        print("not online or no update")
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
    window.iconbitmap("D:\python\icon_future linked.ico")
    #playsound.playsound("sound.mp3")
    # Set the window size
    window.geometry("398x670+500+90")

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
            with open("D:\python\Ai.json","r") as path_file:
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
            Ai.update({question: answer})
            print(Ai)
            with open("\python\Ai.json",'w') as f:
                json.dump(Ai,f)
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
        global question
        global chatbox
        global answer_label
        global answer
        try:
            qustion_button.destory()
            answer_label.destory()
        except:
            print("no button to clear")

        question = input_field.get()
        question.lower()
        chats.append("you:  "+question)
        if question in Ai:
            global chatbox
            closest_key = difflib.get_close_matches(question, Ai.keys())[0]
            chats.append("Ai: "+Ai.get(closest_key))
            print(chats)
            try:
                chatbox.destroy()
                chatbox = tk.Listbox(window,width=58,height=35,background="grey",border=4,)
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
            try:
                print("found something close")
                closest_key = difflib.get_close_matches(question, Ai.keys())[0]
                #if  difflib.SequenceMatcher(question, closest_key) >= 95:
                chats.append("Ai:  "+Ai.get(closest_key))
                try:
                    chatbox.destroy()
                    chatbox = tk.Listbox(window,width=58,height=35,background="grey",border=4,)
                    chatbox.grid(row=0,column=0)
                except:
                    print("cant find anything in the list")
                try:
                    for item in chats:
                        chatbox.insert(tk.END, item)
                        print("added")
                except:
                    print("nothing in list")
                add_q = messagebox.askyesno("Future Linked Ai", "this is the closest answer would you like to add an answer for this?")
                print(add_q)
                if add_q == True:
                     if admin == False:
                        import base64
                        def pass_check(filler):
                            global admin
                            print("pass cchecking")
                            password = b'F(oH!Er'
                            str(filler)
                            check = password_entry.get().encode()
                            check = base64.a85encode(check)
                            if password == check:
                                admin = True
                                window.title("Future Linked (admin)")
                                try:
                                    answer = Ai.get(closest_key)
                                except:
                                    answer = ""
                                import futureLinkedadim
                                root.destroy()
                                password = futureLinkedadim.update_online(question,answer,admin)
                        root = tk.Tk()
                        frame_pass_check = tk.Frame(root,bg="black")
                        password_d = tk.Label(frame_pass_check,text="password")
                        password_d.pack()
                        password_entry = tk.Entry(frame_pass_check,bg="grey",fg="black")
                        password_entry.bind("<Return>",pass_check)
                        password_entry.pack()
                        pass_enter = tk.Button(frame_pass_check,text="enter",command=lambda: pass_check("hello")).pack()
                        frame_pass_check.pack()
                        root.mainloop()
                     else:
                        try:
                            answer = Ai.get(closest_key)
                        except:
                            answer = ""
                        import futureLinkedadim
                        password = futureLinkedadim.update_online(question,answer,admin)

                #else:
                # chats.append("Ai: i have not answer for that sorry")
                    #try:
                    #   import futureLinkedadim
                    #  futureLinkedadim.update_online(question)
                # except:
                    #    clear()
                try:
                    chatbox.destroy()
                    chatbox = tk.Listbox(window,width=58,height=35,background="grey",border=4,)
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
            except:
                try:
                    chatbox.destroy()
                    chatbox = tk.Listbox(window,width=58,height=35,background="grey",border=4,)
                    chatbox.grid(row=0,column=0)
                except:
                    print("cant find anything in the list")
                try:
                    for item in chats:
                        chatbox.insert(tk.END, item)
                        print("added")
                except:
                    print("nothing in list")
                add_qustion = messagebox.askquestion("no answer","would you like to add an answer",icon='warning')
                if add_qustion == "yes":
                    if admin == False:
                        import base64
                        def pass_check(filler):
                            global admin
                            print("pass cchecking")
                            password = b'F(oH!Er'
                            str(filler)
                            check = password_entry.get().encode()
                            check = base64.a85encode(check)
                            if password == check:
                                admin = True

                                try:
                                    answer = Ai.get(closest_key)
                                except:
                                    answer = ""
                                import futureLinkedadim
                                root.destroy()
                                password = futureLinkedadim.update_online(question,answer,admin)
                        root = tk.Tk()
                        frame_pass_check = tk.Frame(root,bg="black")
                        password_d = tk.Label(frame_pass_check,text="password")
                        password_d.pack()
                        password_entry = tk.Entry(frame_pass_check,bg="grey",fg="black")
                        password_entry.bind("<Return>",pass_check)
                        password_entry.pack()
                        pass_enter = tk.Button(frame_pass_check,text="enter",command=lambda: pass_check("hello")).pack()
                        frame_pass_check.pack()
                        root.mainloop()
                    else:
                        try:
                            answer = Ai.get(closest_key)
                        except:
                            answer = ""
                        import futureLinkedadim
                        password = futureLinkedadim.update_online(question,answer,admin)
                else:
                    clear()
            try:
                chatbox.destroy()
                chatbox = tk.Listbox(window,width=58,height=35,background="grey",border=4,)
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

    def clear_chatbox():
        global chats
        global chatbox
        global enter
        global input_field
        chats = []
        chatbox.destroy()
        chatbox = tk.Listbox(window,width=58,height=35,background="grey",border=4,)
        chatbox.grid(row=0,column=0)
        for item in chats:
            chatbox.insert(tk.END, item)
            print("added")
        verson = data["verson"]
        chats.append("                                                Future Linked",)
        chats.append("                                  "+data["new"])
        chats.append("                                            "+data["update"])
        chats.append("                           "+"Amount of questions i can answer "+str(len(Ai)))
        input_field.destroy()
        input_field = tk.Entry(window,width=35,highlightcolor="blue",relief="sunken",border=2,bg="grey")
        input_field.grid(row=2,column=0)
        input_field.bind("<Return>",ask)
        for item in chats:
            chatbox.insert(tk.END, item)

            
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
            input_field = tk.Entry(window,width=35,highlightcolor="blue",relief="sunken",border=2,bg="grey")
            input_field.grid(row=2,column=0)
            enter = tk.Button(window,text="Enter",command=lambda: ask("hello"),bg="grey",width=10)
            change = tk.Button(window,text="Enter",command=lambda: ask("hello"),bg="grey",width=10)
            input_field.bind("<Return>",ask)
            input_field.select_to
            enter.grid(row=3,column=0)
            change.grid(row=4,column=1)
            if starting == 0:
                chats.append("                           "+"Amount of questions i can answer "+str(len(Ai)))
                chatbox = tk.Listbox(window,width=58,height=35,background="grey",border=4,)
                chatbox.grid(row=0,column=0)
                for item in chats:
                    chatbox.insert(tk.END, item)
                print("added")
            starting = 1
    setup(" ")        
    window.mainloop()
start_up.after(3000,main)

start_up.mainloop()
    # Run the window
