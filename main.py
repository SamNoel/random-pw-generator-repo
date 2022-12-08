import tkinter as tk
import random
import string

#----------------FUNCTIONS----------------
def generate_password():
    #get length selection. This will always have a value since we default to 8
    length_selection = int(selected.get())

    #get all customization selections
    customization_selections = []
    for chkbx_selection in checkbox_selections:
        chk_val = chkbx_selection.get()
        if chk_val != 0:
            customization_selections.append(chk_val)
    
    #initialize
    generated_password = ""
    current_val = ""
    valid_nums = [0,1,2,3,4,5,6,7,8,9]
    valid_symbols = ["~","!","@","#","$","%","^","&","*","(",")"]

    #iterate over length selection to build out the password
    for x in range(length_selection):
        if len(customization_selections) != 0:
            random_customization = random.choice(customization_selections)

            if (random_customization == 1):
                #Uppercase letter
                current_val = random.choice(string.ascii_uppercase)
            elif (random_customization == 2):
                #Lowercase letter
                current_val = random.choice(string.ascii_lowercase)
            elif (random_customization == 3):
                #Number
                current_val = random.choice(valid_nums)
            else:
                #Symbol
                current_val = random.choice(valid_symbols)
        else:
            current_val = "-"
        
        #concat character to overall string
        generated_password += str(current_val)
    
    #clear the entry box first then insert the new pw
    entry_pw_output.delete(0, tk.END)
    entry_pw_output.insert(0, generated_password)

#might build these out at some point but not really necessary
def copy_password():
    pass

def refresh_password():
    pass

def clear_password():
    pass

#----------------GRID SETUP----------------

#create the window
window = tk.Tk()
window.title("Random Password Generator")

#configure the grid
window.rowconfigure(0, minsize=50, weight=1) #Main title
window.rowconfigure(1, minsize=300, weight=1) #PW customization section
window.rowconfigure(2, minsize=50, weight=1) #margin
window.rowconfigure(3, minsize=50, weight=1) #Generate PW button
window.rowconfigure(4, minsize=70, weight=1) #PW output section
window.rowconfigure(5, minsize=50, weight=1) #PW output buttons
window.columnconfigure(0, minsize=250, weight=1)
window.columnconfigure(1, minsize=250, weight=1)

#for radio buttons
lengths = (("Eight", "8"),
            ("Nine", "9"),
            ("Ten", "10"),
            ("Eleven", "11"),
            ("Twelve", "12"),)
selected = tk.StringVar(None, lengths[4][1]) #set the default value

#for checkbox selection
customizations = (("Uppercase", 1),
            ("Lowercase", 2),
            ("Numbers", 3),
            ("Symbols", 4))
        
#set all 4 to checked
checkbox_selections = [tk.IntVar(None, customizations[0][1]), 
                        tk.IntVar(None, customizations[1][1]), 
                        tk.IntVar(None, customizations[2][1]), 
                        tk.IntVar(None, customizations[3][1])]

#set the widgets
lbl_title = tk.Label(master=window, text="Customize your password:", pady=20)
frm_pw_length = tk.Frame(master=window, bg="#F4F4F4", padx=20, pady=20)
frm_pw_customize = tk.Frame(master=window, bg="#F4F4F4", padx=20, pady=20)
lbl_pw_length = tk.Label(master=frm_pw_length, text="Password Length:", bg="#F4F4F4", fg="#040404", pady=10)
lbl_pw_customize = tk.Label(master=frm_pw_customize, text="Customize:", bg="#F4F4F4", fg="#040404", pady=10)
btn_generate = tk.Button(master=window, text="Generate Password!", highlightbackground="#81B186", pady=10, command=generate_password)
frm_pw_output = tk.Frame(master=window)
entry_pw_output = tk.Entry(master=frm_pw_output)

#pack the widgets that are part of frames
lbl_pw_length.pack(anchor=tk.W)
lbl_pw_customize.pack(anchor=tk.W)
entry_pw_output.pack()

#set radio buttons based on lengths list
for length in lengths:
    rad = tk.Radiobutton(frm_pw_length, text=length[1], value=length[1], variable=selected, bg="#F4F4F4", fg="#040404")
    rad.pack(padx=5, pady=5, anchor=tk.W)

#set checkbox selections based on customizations list
i = 0
for custom in customizations:
    chkbx = tk.Checkbutton(frm_pw_customize, text=custom[0], variable=checkbox_selections[i], onvalue=custom[1], offvalue=0, bg="#F4F4F4", fg="#040404")
    chkbx.pack(padx=5, pady=5, anchor=tk.W)
    i += 1

#assign the widgets to the grid
lbl_title.grid(row=0, column=0, columnspan=2, stick="ew", padx=5, pady=5)
frm_pw_length.grid(row=1, column=0, sticky="nsew", padx=5)
frm_pw_customize.grid(row=1, column=1, sticky="nsew", padx=5)
btn_generate.grid(row=3, column=0, columnspan=2, sticky="ew", padx=5)
frm_pw_output.grid(row=4, column=0, columnspan=2, sticky="ew", padx=5)

#test

#run the event loop
window.mainloop()