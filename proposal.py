import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def on_yes_click():
    image_path = "prose.1.png"
    msg = "I love you too!"
    show_image_and_msg(image_path, msg)

def on_no_click_first():
    image_path = "prose.2.jpg"
    msg = "Are you sure??"
    show_image_and_msg(image_path, msg, on_no_click_second, on_yes_click)

def on_no_click_second():
    image_path = "thinking 2.png"
    msg = "Phir se soch le."
    show_image_and_msg(image_path, msg, on_no_click_third, on_yes_click)

def on_no_click_third():
    image_path = "last.2.jpg"
    msg = "Plzzz plzzz accept karle."
    show_image_and_msg(image_path, msg, on_no_click_fourth, on_yes_click)

def on_no_click_fourth():
    
    image_path = "anime-boy-anime.gif"  # Replace with your desired final image
    msg = "------good byyy!-----"
    show_image_and_msg(image_path, msg, on_no_click_fourth, on_yes_click)

def show_image_and_msg(image_path, msg, no_function=None, yes_function=None):
    
    for widget in root.winfo_children():
        widget.destroy()

    try:
        img = Image.open(image_path)
        img = img.resize((700, 655))
        img_tk = ImageTk.PhotoImage(img)

        img_label = tk.Label(root, image=img_tk)
        img_label.image = img_tk
        img_label.pack(pady=10)

        msg_label = tk.Label(root, text=msg, font=("Arial", 16))
        msg_label.pack(pady=10)

        # If "Yes" and "No" buttons are present, show them.
        if no_function is not None and yes_function is not None:
            yes_button = tk.Button(root, text="Yes", command=yes_function, font=("Arial", 14))
            yes_button.pack(side="left", padx=20, pady=10)

            no_button = tk.Button(root, text="No", command=no_function, font=("Arial", 14))
            no_button.pack(side="right", padx=20, pady=10)

    except FileNotFoundError:
        messagebox.showerror("File Not Found", f"The image file at {image_path} could not be found.")
        root.quit()


root = tk.Tk()
root.title("Image Choice Application")
root.geometry("800x700")


initial_image_path = "last3.jpg"
initial_msg = "I love you."

show_image_and_msg(initial_image_path, initial_msg, on_no_click_first, on_yes_click)


root.mainloop()
