import tkinter as tk
from PIL import Image, ImageTk

def load_image():
    """Load a single image and return it."""
    try:
        img = Image.open('symbol1.jpg')  # Replace with a known good image file
        img = img.resize((100, 100))
        return ImageTk.PhotoImage(img)
    except FileNotFoundError:
        print("Image file not found.")
        return None

# Initialize the main window
root = tk.Tk()
root.title("Image Display Test")

# Load an image
image = load_image()

if image:
    # Label to display image
    label = tk.Label(root, image=image)
    label.image = image  # Keep a reference
    label.pack()

    # Start the GUI event loop
    root.mainloop()
else:
    print("No image loaded. Exiting.")
