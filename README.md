# Project Description

**Project Description: Image Resizer Using Tkinter and PIL**

**Overview:**
This project implements a simple graphical user interface (GUI) application using Python's Tkinter library and the Python Imaging Library (PIL) to resize images. The application allows users to select an image file, specify a folder to save the resized images, and process the image to create multiple resized versions.

**Features:**
1. **Image Selection:**
   - Users can choose an image file from their file system using a file dialog.
   
2. **Save Directory Selection:**
   - Users can specify a folder where the resized images will be saved using a directory selection dialog.
   
3. **Image Resizing:**
   - The application supports resizing the selected image to several predefined sizes: 16x16, 32x32, 48x48, 72x72, and 163x163 pixels.
   - The resized images are saved in the specified directory with appropriate filenames.

**Components:**
1. **GUI Components:**
   - **Entry Widgets:** For displaying the paths of the selected image and save directory.
   - **Buttons:** For opening the file dialog (`Open Image`), selecting the save folder (`Select Save Folder`), and initiating the image processing (`Process Images`).

2. **Core Functions:**
   - `resize_and_save(image_path, sizes, save_dir)`: Handles the resizing of the image to multiple sizes and saves the resized images.
   - `open_file()`: Opens a file dialog for selecting the image file and updates the file path entry.
   - `select_save_folder()`: Opens a directory selection dialog for specifying the save directory and updates the folder path entry.
   - `process_images()`: Gathers user inputs (file path and save directory) and triggers the resizing process using predefined sizes.

**Technical Details:**
- **Tkinter:** Used for creating the GUI components.
- **PIL (Python Imaging Library):** Used for image handling (opening, resizing, and saving images).
- **File Dialogs:**
  - `filedialog.askopenfilename()`: For opening the file selection dialog.
  - `filedialog.askdirectory()`: For opening the directory selection dialog.
- **Image Resampling:** The resizing process uses `Image.Resampling.LANCZOS` for high-quality image resampling.

**Usage:**
1. Run the program.
2. Click the `Open Image` button to select an image file.
3. Click the `Select Save Folder` button to choose a directory where the resized images will be stored.
4. Click the `Process Images` button to generate and save the resized images in the selected folder.

**Dependencies:**
- Python 3.x
- Tkinter (typically included with Python)
- PIL (Pillow library)

**Installation:**
To install the required Pillow library, run:
```bash
pip install pillow
```

**Notes:**
- Ensure that the selected image file is a format supported by PIL.
- The filenames of the resized images will indicate their dimensions (e.g., `image_16x16.png`, `image_32x32.png`, etc.).
