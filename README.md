# 🗂️ File Organizer Script

This Python script helps you clean up messy folders by automatically sorting files into categorized subfolders — like `Images`, `Documents`, `Audio`, `Videos`, and more.

---

## 🚀 Features

✅ Automatically detects file types by extension  
✅ Creates subfolders like `Images`, `Documents`, etc.  
✅ Moves unknown file types to an `Others` folder  
✅ Easy to customize and reuse  
✅ Super simple to run — no third-party libraries needed

---

## 📂 Example Folder Structure (Before & After)

**Before:**
messyfolder/
├── photo1.jpg
├── notes.txt
├── song.mp3
├── video.mp4
├── unknown.xyz

** After**
messyfolder/
├── Images/
│   └── photo1.jpg
├── Documents/
│   └── notes.txt
├── Audio/
│   └── song.mp3
├── Videos/
│   └── video.mp4
├── Others/
│   └── unknown.xyz


---

## ⚙️ How to Use

1. **Edit the path** to your messy folder:
   ```python
   file_to_organize = r"C:\Users\yourname\path\to\folder"

Run the script from terminal:
python file_organizer.py

Watch as your files are neatly sorted into subfolders!

 Built With
Python 3

os module

shutil module

Future Ideas (Optional Upgrades)
Add a GUI using Tkinter

Add logging (record what files were moved)

Let user choose folder via input

Schedule it to run automatically

 Author
Kenny (@kaycoder97)
Crafted with 💻 and some 🎧

 License
This project is open source and available under the MIT License.



