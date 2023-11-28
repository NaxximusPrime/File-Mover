import os
import shutil

source_folder = r"C:\Users\eiste\Documents"
destination_folder = r"F:\Dokumente\zzz_moved_pdfs"

print(source_folder)

pdf_files = [file for file in os.listdir(r"C:\Users\eiste\Documents") if file.endswith(".pdf")]
print(pdf_files)

for file in pdf_files:
	source_path = os.path.join(source_folder, file)
	destination_path = os.path.join(destination_folder, file)
	shutil.move(source_path, destination_path)
	print(f"{file} has successfully been moved.")
else:
	print("No more files found to move!")