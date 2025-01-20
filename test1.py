import os

folders = input("please provide list of folder names with spaces: ").split()
for folder in folders:
    if os.path.exists(folder):
        files = os.listdir(folder)
        print(f"Files in {folder}: {files}")
    else:
        print(f"Folder '{folder}' does not exist.")