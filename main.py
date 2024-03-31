import PyPDF2
import os

files = os.listdir("Files")
searchInput = input("What do you want to search? \n")
print("\n")

for file in files:
  with open(f'Files/{file}', 'rb') as file_path:
    reader = PyPDF2.PdfReader(file_path)

    for page in reader.pages:
      if searchInput in page.extract_text():
        print(f"Found in: {file}\n")
        break
