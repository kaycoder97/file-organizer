import os
import shutil
file_to_organize = r"C:\Users\kenny\Downloads"
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".avi", ".mov"],
    "Audio": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"],
    "code": [".py", ".js", ".html", ".css"],
    
}
for file in os.listdir(file_to_organize):
    file_path = os.path.join(file_to_organize, file)
    
    if not os.path.isfile(file_path):
        continue  # skip folders

    print(f"Checking: {file}")

    file_path = os.path.join(file_to_organize, file)

    if os.path.isfile(file_path):
        _, ext = os.path.splitext(file)  # get file extension
        ext = ext.lower()

        moved = False

        for folder_name, extensions in file_types.items():
            if ext in extensions:
                new_folder_path = os.path.join(file_to_organize,folder_name)

                if not os.path.exists(new_folder_path):
                    os.makedirs(new_folder_path)

                shutil.move(file_path, os.path.join(new_folder_path, file))
                moved = True
                break

        # If no match found, move to 'Others'
        if not moved:
            other_folder = os.path.join(file_to_organize, "Others")
            if not os.path.exists(other_folder):
                os.makedirs(other_folder)
            shutil.move(file_path, os.path.join(other_folder, file))
            print("✅ Done organizing!")