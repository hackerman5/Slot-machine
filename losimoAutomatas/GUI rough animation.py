import tkinter as tk
import time
import random
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
    # create three slot machine reels
    reels = []
    for i in range(3):
        #reel_image = tk.PhotoImage(file="C:/Users/Mantas/Desktop/inzinerijos nsm/reel.png")
        reel_image = ImageTk.PhotoImage(Image.open("reel.png"))
        #reel_image = Image.open('slot_bg.jpg')
        #reel_image = reel_image.resize((50, 50))
        #reel_image = ImageTk.PhotoImage(reel_image)

        #reel = canvas.create_image(70 + (i * 80), 80, image=reel_image)
        reel = canvas.create_image(150 + (i * 80), 80, image=reel_image)
        reels.append(reel)
    
    # start the slot machine animation
    animate(reels)

def reset():
    pass

# define a function for animating the slot machine reels
def animate(reels):
    # generate three random symbols for the slot machine reels
    symbols = []
    for i in range(3):
        symbols.append(random.choice(["cherry", "lemon", "orange", "plum"]))

    # animate the reels
    for i in range(10):
        for reel in reels:
            symbol_image = ImageTk.PhotoImage(Image.open(f"{symbols[reels.index(reel)]}.png"))
            canvas.itemconfig(reel, image=symbol_image)
            window.update()
            time.sleep(0.1)
    
    # update the final symbols for the slot machine reels
    for reel in reels:
        symbol_image = tk.PhotoImage(file=f"{symbols[reels.index(reel)]}.png")
        canvas.itemconfig(reel, image=symbol_image)



# add buttons to window
spin_button = tk.Button(window, text="Spin", command=spin)
spin_button.pack(side=tk.LEFT, padx=10, pady=10)

reset_button = tk.Button(window, text="Reset", command=reset)
reset_button.pack(side=tk.LEFT, padx=10, pady=10)

# start the window
window.mainloop()