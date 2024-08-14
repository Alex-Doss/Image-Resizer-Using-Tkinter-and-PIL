import tkinter as tk
from tkinter import filedialog
from PIL import Image
import os

def resize_and_save(image_path, sizes, save_dir):
    base_image = Image.open(image_path)
    for size in sizes:
        resized_image = base_image.resize(size, Image.Resampling.LANCZOS)  # Исправлено здесь
        save_path = os.path.join(save_dir, f'image_{size[0]}x{size[1]}.png')
        resized_image.save(save_path, 'PNG')

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        entry_path.delete(0, tk.END)
        entry_path.insert(0, file_path)

def select_save_folder():
    folder_path = filedialog.askdirectory()  # Исправлено здесь
    if folder_path:
        entry_folder.delete(0, tk.END)
        entry_folder.insert(0, folder_path)  # Исправлено здесь

def process_images():
    file_path = entry_path.get()
    save_dir = entry_folder.get()
    sizes = [(16, 16), (32, 32), (48, 48), (72, 72), (163, 163)]
    resize_and_save(file_path, sizes, save_dir)

root = tk.Tk()
root.title("Image Resizer")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

entry_path = tk.Entry(frame, width=50)
entry_path.pack(side=tk.TOP, fill=tk.X, expand=True)
button_open = tk.Button(frame, text="Open Image", command=open_file)
button_open.pack(side=tk.TOP)

entry_folder = tk.Entry(frame, width=50)
entry_folder.pack(side=tk.TOP, fill=tk.X, expand=True)
button_folder = tk.Button(frame, text="Select Save Folder", command=select_save_folder)
button_folder.pack(side=tk.TOP)

button_process = tk.Button(frame, text="Process Images", command=process_images)
button_process.pack(side=tk.TOP)

root.mainloop()
