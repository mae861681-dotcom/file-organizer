import os
import shutil

def organize_junk():
    path = os.getcwd()
    files = os.listdir(path)

    for file in files:
        if file == 'organizer.py':
            continue
            
        filename, extension = os.path.splitext(file)
        extension = extension[1:].lower()

        if extension in ['jpg', 'jpeg', 'png']:
            folder = 'Images'
        elif extension in ['pdf', 'docx', 'txt']:
            folder = 'Documents'
        elif extension in ['mp4', 'mkv']:
            folder = 'Videos'
        else:
            continue

        if not os.path.exists(folder):
            os.makedirs(folder)

        shutil.move(file, f"{folder}/{file}")
        print(f"Moved {file} to {folder}")

if __name__ == "__main__":
    organize_junk()