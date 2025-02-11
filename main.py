# Python Tkinter GUI Tutorial from Codemy.com yt channel
# modified to be evil
from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser
from win32 import win32api
import tkinter.font as tkFont
import random

root = Tk()
root.title('Evil Text Editor')
#root.iconbitmap('D:/text editor/second one/woman-head.ico')
root.geometry("1200x680")

# set variable for open file name
global open_status_name
open_status_name = False

global selected
selected = False

global language
language = "American English"

global night
night = False

#new file func
def new_file():
    text.delete("1.0", END)
    root.title("New File")
    status_bar.config(text="New File    ")

    global open_status_name
    open_status_name = False

#open file func
def open_file():
    text.delete("1.0", END)
    
    text_file = filedialog.askopenfilename(title="Open File", 
                                           filetypes = 
                                               (("Text Files", "*.txt"),
                                                ("All Files", "*.*")))

    if text_file:
        #make filename global
        global open_status_name
        open_status_name = text_file
        
    name = text_file
    status_bar.config(text=f"{name}    ")
    root.title(f"{name}")

    #open the file
    text_file = open(text_file, 'r')
    text_from_file = text_file.read()
    text.insert(END, text_from_file)

def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension=".*",
                                             title="Save As",
                                             filetypes = (("Text File", "*.txt"),
                                                         ("All Files", "*.*")))
    if text_file:
        name = text_file
        status_bar.config(text = f"Saved!    ")
        root.title(f"{name}")

        #save as file
        text_file = open(text_file, 'w')
        text_file.write(text.get("1.0", END))
        #close file
        text_file.close()

def save_file():
    global open_status_name
    if open_status_name:
        #save the file
        text_file = open(open_status_name, 'w')
        text_file.write(text.get("1.0", END))
        #close file
        text_file.close()

        status_bar.config(text=f"Saved {open_status_name}!    ")
    else:
        save_as_file()

def cut_text(e):
    global selected
    #key bindings
    if e:
        selected = root.clipbaord_get()
    else:
        if text.selection_get():
            #grab selected text
            selected = text.selection_get()
            #delete selected text
            text.delete("sel.first", "sel.last")
            #clear clipboard, then append
            root.clipboard_clear()
            root.clipboard_append(selected)

def copy_text(e):
    global selected
    #key bindings
    if e:
        #grab selected text
        selected = root.clipboard_get()
    #no key bindings
    if text.selection_get():
        #grab selected text
        selected = text.selection_get()
        #clear clipboard, then append
        root.clipboard_clear()
        root.clipboard_append(selected)

def paste_text(e):
    global selected
    #key bindings
    if e:
        selected = root.clipboard_get()
    #no key bindings
    else:
        if selected:
            cursor_position = text.index(INSERT)
            text.insert(cursor_position, selected)

def bold_it():
    #create font
    bold_font = font.Font(text, text.cget("font"))
    bold_font.configure(weight="bold")
    #config a tag
    text.tag_configure("bold", font = bold_font)

    #define current tags
    current_tags = text.tag_names("sel.first")

    #if bold or not
    if "bold" in current_tags:
        text.tag_remove("bold", "sel.first", "sel.last")
    else:
        text.tag_add("bold", "sel.first", "sel.last")

def italics_it():
    #create font
    italics_font = font.Font(text, text.cget("font"))
    italics_font.configure(slant="italic")
    #config a tag
    text.tag_configure("italics", font = italics_font)

    #define current tags
    current_tags = text.tag_names("sel.first")

    #if italics or not
    if "italics" in current_tags:
        text.tag_remove("italics", "sel.first", "sel.last")
    else:
        text.tag_add("italics", "sel.first", "sel.last")

#change colour
def text_color():
    #pick a colour
    picked_color = colorchooser.askcolor()[1]

    if picked_color:
        status_bar.config(text=picked_color)
        #create font
        color_font = font.Font(text, text.cget("font"))
        #config a tag
        text.tag_configure("colored", font = color_font, foreground=picked_color)

        #define current tags
        current_tags = text.tag_names("sel.first")

        #if italics or not
        if "colored" in current_tags:
            text.tag_remove("colored", "sel.first", "sel.last")
        else:
            text.tag_add("colored", "sel.first", "sel.last")

def crit_chance(event):
    global night
    
    if random.random() < 0.05:
        text_widget = event.widget
        current_text = text_widget.get("1.0", END)

        if current_text:
            last_char_index = len(current_text) - 2
            if last_char_index >= 0:
                last_char = current_text[last_char_index]
                text_widget.insert(END, last_char, "critical")
                text_widget.see(END)
                text_widget.tag_configure("critical", font=("TkDefaultFont", 64))

    if random.random() < 0.1:
        string_in_text = text.get('1.0', 'end-1c')
        string_length = len(string_in_text)
        if string_length == 0:
            random_index = 0
        else:
            random_index = random.randint(0, string_length)

        if night == False:
            text.insert(f"1.0 + {random_index} chars", "🐜")
        else:
            text.insert(f"1.0 + {random_index} chars", "🦇")

    if random.random() < 0.2:
        if night == False:
            night_on()
            replace_ants()
            night = True
        else:
            light_on()
            replace_bats()
            night = False

#change all text color
def all_text_color():
    picked_color = colorchooser.askcolor()[1]
    if picked_color:
        text.config(fg=picked_color)

#change bg color
def background_color():
    picked_color = colorchooser.askcolor()[1]
    if picked_color:
        text.config(bg=picked_color)

def print_file():
    #printer_name = win32print.GetDefaultPrinter()
    #status_bar.config(text = f"{printer_name}")
    file_to_print = filedialog.askopenfilename(title="Open File",
                                               filetypes=(("Text Files", "*.txt"),
                                                          ("All Files", "*.*")))
    if file_to_print:
        win32api.ShellExecute(0, "print", file_to_print, None, ".", 0)

def select_all(e):
    #add sel to select all text
    text.tag_add('sel', '1.0', 'end')

def clear_all():
    text.delete(1.0, END)

#turn on night mode
def night_on():
    #colours
    main_color = "#3C3C3C"
    second_color = "#011627"
    text_color = "#015FB8"

    #configure the color
    root.config(bg=main_color)
    status_bar.config(bg=main_color, fg=text_color)
    text.config(bg=second_color, fg=text_color)
    toolbar_frame.config(bg=main_color)
    #buttons
    bold_button.config(bg=second_color, fg=text_color)
    italics_button.config(bg=second_color, fg=text_color)
    redo_button.config(bg=second_color, fg=text_color)
    undo_button.config(bg=second_color, fg=text_color)
    color_text_button.config(bg=second_color, fg=text_color)
    ant_button.config(bg=second_color, fg=text_color)
    #file menu
    file_menu.config(bg=second_color, fg=text_color)
    edit_menu.config(bg=second_color, fg=text_color)
    color_menu.config(bg=second_color, fg=text_color)
    options_menu.config(bg=second_color, fg=text_color)

#light mode
def light_on():
    #colours
    main_color = "SystemButtonFace"
    second_color = "SystemButtonFace"
    text_color = "black"

    #configure the color
    root.config(bg=main_color)
    status_bar.config(bg=main_color, fg=text_color)
    text.config(bg="white", fg=text_color)
    toolbar_frame.config(bg=main_color)
    #buttons
    bold_button.config(bg=second_color, fg=text_color)
    italics_button.config(bg=second_color, fg=text_color)
    redo_button.config(bg=second_color, fg=text_color)
    undo_button.config(bg=second_color, fg=text_color)
    color_text_button.config(bg=second_color, fg=text_color)
    ant_button.config(bg=second_color, fg=text_color)
    #file menu
    file_menu.config(bg=second_color, fg=text_color)
    edit_menu.config(bg=second_color, fg=text_color)
    color_menu.config(bg=second_color, fg=text_color)
    options_menu.config(bg=second_color, fg=text_color)

#unpleasant mode
def unpleasant_on():
    #colours
    main_color = "#32CD32"
    second_color = "#BF40BF"
    text_color = "#FF1300"

    #configure the color
    root.config(bg=main_color)
    status_bar.config(bg=main_color, fg=text_color)
    text.config(bg=main_color, fg=text_color)
    toolbar_frame.config(bg=main_color)
    #buttons
    bold_button.config(bg=second_color, fg=text_color)
    italics_button.config(bg=second_color, fg=text_color)
    redo_button.config(bg=second_color, fg=text_color)
    undo_button.config(bg=second_color, fg=text_color)
    color_text_button.config(bg=second_color, fg=text_color)
    ant_button.config(bg=second_color, fg=text_color)
    #file menu
    file_menu.config(bg=second_color, fg=text_color)
    edit_menu.config(bg=second_color, fg=text_color)
    color_menu.config(bg=second_color, fg=text_color)
    options_menu.config(bg=second_color, fg=text_color)

def random_on():
    #okay let me explain myself
    #first random.randint(0, 0xFFFFFF) generates a random hex number
    #then, it removes the "0x" python puts there automatically (and the colour has to be a string)
    main_color = str(random.randint(0, 0xFFFFFF)).upper()[2:]
    second_color = str(random.randint(0, 0xFFFFFF)).upper()[2:]
    text_color = str(random.randint(0, 0xFFFFFF)).upper()[2:]

    #the string must be 6 characters long, and sometimes a low number is generated (e.g. 0xFF)
    #so we just add 0s to the front, because 0000FF == FF
    while len(main_color) < 6:
        main_color = "0" + main_color
    while len(second_color) < 6:
        second_color = "0" + second_color
    while len(text_color) < 6:
        text_color = "0" + text_color
    
    #then, once we have our 6 digit hex number we can add a hashtag so that tkinter can understand it
    main_color = "#" + main_color
    second_color = "#" + second_color
    text_color = "#" + text_color

    #configure the color
    root.config(bg=main_color)
    status_bar.config(bg=main_color, fg=text_color)
    text.config(bg=main_color, fg=text_color)
    toolbar_frame.config(bg=main_color)
    #buttons
    bold_button.config(bg=second_color, fg=text_color)
    italics_button.config(bg=second_color, fg=text_color)
    redo_button.config(bg=second_color, fg=text_color)
    undo_button.config(bg=second_color, fg=text_color)
    color_text_button.config(bg=second_color, fg=text_color)
    ant_button.config(bg=second_color, fg=text_color)
    #file menu
    file_menu.config(bg=second_color, fg=text_color)
    edit_menu.config(bg=second_color, fg=text_color)
    color_menu.config(bg=second_color, fg=text_color)
    options_menu.config(bg=second_color, fg=text_color)

def american_english():
    #menu drop downs
    main_menu.entryconfigure(1, label="File")
    main_menu.entryconfigure(2, label="Edit")
    main_menu.entryconfigure(3, label="Color")
    main_menu.entryconfigure(4, label="Options")
    main_menu.entryconfigure(5, label="Language")
    #buttons
    bold_button.config(text = "Bold")
    italics_button.config(text = "Italics")
    redo_button.config(text = "Undo")
    undo_button.config(text = "Redo")
    color_text_button.config(text = "Text Color")
    ant_button.config(text = "Ant")
    #window title
    root.title('Evil Text Editor')

def english_english():
    #menu drop downs
    main_menu.entryconfigure(1, label="File")
    main_menu.entryconfigure(2, label="Edit")
    main_menu.entryconfigure(3, label="Colour")
    main_menu.entryconfigure(4, label="Options")
    main_menu.entryconfigure(5, label="Language")
    #buttons
    bold_button.config(text = "Bold")
    italics_button.config(text = "Italics")
    redo_button.config(text = "Undo")
    undo_button.config(text = "Redo")
    color_text_button.config(text = "Text Colour")
    ant_button.config(text = "Ant")
    #window title
    root.title('Evil Text Editor')

def cat_language():
    #menu drop downs
    main_menu.entryconfigure(1, label="Meow")
    main_menu.entryconfigure(2, label="Meow")
    main_menu.entryconfigure(3, label="Meow")
    main_menu.entryconfigure(4, label="Meow")
    main_menu.entryconfigure(5, label="Meow")
    #buttons
    bold_button.config(text = "Meow")
    italics_button.config(text = "Meow")
    redo_button.config(text = "Meow")
    undo_button.config(text = "Meow")
    color_text_button.config(text = "Meow")
    ant_button.config(text = "Meow")
    #window title
    root.title('Meow')
    #status bar
    status_bar.config(text="Meow    ")

def alien_language():
    #https://lingojam.com/AlienLanguage
    #menu drop downs
    main_menu.entryconfigure(1, label="⎎⟟⌰⟒")
    main_menu.entryconfigure(2, label="⟒⎅⟟⏁")
    main_menu.entryconfigure(3, label="☊⍜⌰⍜⎍⍀")
    main_menu.entryconfigure(4, label="⍜⌿⏁⟟⍜⋏⌇")
    main_menu.entryconfigure(5, label="⌰⏃⋏☌⎍⏃☌⟒")
    #buttons
    bold_button.config(text = "⏚⍜⌰⎅")
    italics_button.config(text = "⟟⏁⏃⌰⟟☊⌇")
    redo_button.config(text = "⎍⋏⎅⍜")
    undo_button.config(text = "⍀⟒⎅⍜")
    color_text_button.config(text = "⏁⟒⌖⏁ ☊⍜⌰⍜⎍⍀")
    ant_button.config(text = "⏃⋏⏁")
    #window title
    root.title('⟒⎐⟟⌰ ⏁⟒⌖⏁ ⟒⎅⟟⏁⍜⍀')

def ant():
    string_in_text = text.get('1.0', 'end-1c')
    string_length = len(string_in_text)
    if string_length == 0:
        random_index = 0
    else:
        random_index = random.randint(0, string_length)

    text.insert(f"1.0 + {random_index} chars", "🐜")

def replace_ants():
    string_in_text = text.get('1.0', 'end-1c')
    
    string_in_text = string_in_text.replace("🐜", "🦇")

    text.delete("1.0", END)
    text.insert("1.0", string_in_text)

def replace_bats():
    string_in_text = text.get('1.0', 'end-1c')
    
    string_in_text = string_in_text.replace("🦇", "🐜")

    text.delete("1.0", END)
    text.insert("1.0", string_in_text)

#toolbar frame
toolbar_frame = Frame(root)
toolbar_frame.pack(fill=X)

# main frame
frame = Frame(root)
frame.pack(pady=random.randint(0, 8))

#vertical scroll
text_scroll = Scrollbar(frame)
text_scroll.pack(side=RIGHT, fill=Y)

#horizontal scroll
horizontal_text_scroll = Scrollbar(frame, orient="horizontal")
horizontal_text_scroll.pack(side=BOTTOM, fill=X)

#text box
text = Text(frame, 
            width = 97,
            height=25,
            font=("Helvetica", 16),
            selectbackground="blue",
            selectforeground="black",
            undo=True,
            yscrollcommand=text_scroll.set,
            #options are "none" "word" and "char"
            wrap="none",
            xscrollcommand=horizontal_text_scroll.set)

text.pack()

#scroll config
text_scroll.config(command=text.yview)
horizontal_text_scroll.config(command=text.xview)

#menu
main_menu = Menu(root)
root.config(menu=main_menu)

#file
file_menu = Menu(main_menu, tearoff=False)
main_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command = new_file)
file_menu.add_command(label="Open", command = open_file)
file_menu.add_command(label="Save", command = save_file)
file_menu.add_command(label="Save As...", command = save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Print...", command = print_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

#edit
edit_menu = Menu(main_menu, tearoff=False)
main_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=lambda: cut_text(False), accelerator="Ctrl+X")
edit_menu.add_command(label="Copy", command=lambda: copy_text(False), accelerator="Ctrl+C")
edit_menu.add_command(label="Paste        ", command=lambda: paste_text(False), accelerator="Ctrl+V")
edit_menu.add_separator()
edit_menu.add_command(label="Undo", command=text.edit_undo, accelerator="Ctrl+Z")
edit_menu.add_command(label="Redo", command=text.edit_redo, accelerator="Ctrl+Y")
edit_menu.add_separator()
edit_menu.add_command(label="Select All", command=lambda: select_all(True), accelerator="Ctrl+A")
edit_menu.add_command(label="Clear All", command=clear_all)

#color Menu
color_menu = Menu(main_menu, tearoff=False)
main_menu.add_cascade(label="Color", menu=color_menu)
color_menu.add_command(label="Change Selected Text", command=text_color)
color_menu.add_command(label="Change All Text", command=all_text_color)
color_menu.add_command(label="Background", command=background_color)

#options menu
options_menu = Menu(main_menu, tearoff=False)
main_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Night Mode", command=night_on)
options_menu.add_command(label="Light Mode", command=light_on)
options_menu.add_command(label="Unpleasant Mode", command=unpleasant_on)
options_menu.add_command(label="Random!!!", command=random_on)

#language menu
language_menu = Menu(main_menu, tearoff=False)
main_menu.add_cascade(label="Language", menu=language_menu)
language_menu.add_command(label="American English", command=american_english)
language_menu.add_command(label="English English", command=english_english)
language_menu.add_command(label="Cat", command=cat_language)
language_menu.add_command(label="Alien", command=alien_language)

#status bar at the bottom
status_bar = Label(root, text = 'Hi!    ', anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=random.randint(10, 15))

#edit bindings
root.bind('<Control-Key-x>', cut_text)
root.bind('<Control-Key-c>', copy_text)
root.bind('<Control-Key-v>', paste_text)
root.bind('<Control-Key-a>', select_all)

#buttons
#bold
bold_button = Button(toolbar_frame, text = "Bold", command = bold_it)
bold_button.grid(row = 0, column = 0, sticky=W, padx=random.randint(0,20))
#italics
italics_button = Button(toolbar_frame, text = "Italics", command = italics_it)
italics_button.grid(row = 0, column = 1, padx=random.randint(0,20))
#undo/redo
undo_button = Button(toolbar_frame, text = "Undo", command = text.edit_undo)
undo_button.grid(row = 0, column = 2, padx=random.randint(0,20))
redo_button = Button(toolbar_frame, text = "Redo", command = text.edit_redo)
redo_button.grid(row = 0, column = 3, padx=random.randint(0,20))
#text colour
color_text_button = Button(toolbar_frame, text="Text Color", command=text_color)
color_text_button.grid(row=0, column=4, padx=random.randint(0,20))
#ants
ant_button = Button(toolbar_frame, text="Ant", command=ant)
ant_button.grid(row=0, column=5, padx=random.randint(0,20))

#TODO: make crits only happen on alphanumeric characters
root.bind("<Key>", crit_chance)

root.mainloop()