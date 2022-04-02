import tkinter as tk
window = tk.Tk()
greeting = tk.Label(text="Hello, Alex")
greeting.pack()

label = tk.Label(
    text="Name",
    foreground="black",  # Set the text color to white
    background="white",  # Set the background color to black
    width=10,
    height=10
)
label.pack()
entry = tk.Entry()
entry.pack()
button = tk.Button(
    text="Click Here!",
    width=10,
    height=5,
    bg="White",
    fg="Black",
)
button.pack()

window.mainloop()



