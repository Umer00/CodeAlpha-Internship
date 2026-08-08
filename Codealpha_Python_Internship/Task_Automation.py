import os
import shutil

print("📂 JPG File Mover")
source_folder = input("Enter source folder path: ")
destination_folder = input("Enter destination folder path: ")

# Agar destination nahi hai to bana do
os.makedirs(destination_folder, exist_ok=True)

count = 0
for file in os.listdir(source_folder):
    if file.endswith(".jpg") or file.endswith(".jpeg"):
        shutil.move(os.path.join(source_folder, file), destination_folder)
        count += 1

print(f"✅ {count} .jpg files moved to {destination_folder}")