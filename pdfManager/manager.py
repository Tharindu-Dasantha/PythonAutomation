import PyPDF2
import sys
import os

merger = PyPDF2.PdfFileMerger()

for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        merger.append(file)
    
    nameOfTheFile = input("Enter the name of the file: ")
    merger.write(nameOfTheFile + ".pdf")