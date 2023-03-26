import tkinter as tk
from PIL import ImageTk, Image

# new window
window = tk.Tk()

# title of window
window.title("Slot Machine")

# open background image
image = Image.open('slot_bg.jpg')
image = image.resize((500, 500))
image = ImageTk.PhotoImage(image)

# create a canvas(background)
canvas = tk.Canvas(window, width=500, height=500)
canvas.pack()

# add image to background
canvas.create_image(250, 250, image=image)

# buttons
def spin():
    pass

def reset():
    pass

# add buttons to window
spin_button = tk.Button(window, text="Spin", command=spin)
spin_button.pack(side=tk.LEFT, padx=10, pady=10)

reset_button = tk.Button(window, text="Reset", command=reset)
reset_button.pack(side=tk.LEFT, padx=10, pady=10)

# start the window
window.mainloop()