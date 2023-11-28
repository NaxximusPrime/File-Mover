import os
import shutil

source_folder = r"C:\Users\user\Documents"
destination_folder = r"F:\Dokumente\zzz_moved_pdfs"

# Output of all PDF-files in source folder
pdf_files = [file for file in os.listdir(r"C:\Users\user\Documents") if file.endswith(".pdf")]
print(pdf_files)

# iterate over every file in source folder and moves it to destination folder.
for file in pdf_files:
	source_path = os.path.join(source_folder, file)
	destination_path = os.path.join(destination_folder, file)
	shutil.move(source_path, destination_path)
# After iteration gives output for every moved file.
	print(f"{file} has successfully been moved.")
# If no (more) file to move, gives output.
else:
	print("No more files found to move!")
