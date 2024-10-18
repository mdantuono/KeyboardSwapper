import tkinter as tk
import keyboard

normalText = "Keys are normal"
activeText = "Keys are swapped to arrows"

state = False

def buttonClicked():
    global state

    print("Button clicked!")
    if state is False:
        swapKeys()
        state = True
        label.config(text=activeText)


    elif state is True:
        unswap()
        state = False
        label.config(text=normalText)

    label.pack(padx=20, pady=20)

def swapKeys():
    keyboard.remap_key('j', 'left')
    keyboard.remap_key('l', 'right')
    keyboard.remap_key('i', 'up')
    keyboard.remap_key('k', 'down')
    keyboard.remap_key('u', 'pageup')
    keyboard.remap_key('o', 'pagedown')

def unswap():
    keyboard.unhook_all()

root = tk.Tk()

# Creating a button with specified options
button = tk.Button(root, 
                   text="Swap", 
                   command=buttonClicked,
                   activebackground="blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)

label = tk.Label(text="Click to swap keys")

button.pack(padx=20, pady=20)
label.pack(padx=20, pady=20)


root.mainloop()