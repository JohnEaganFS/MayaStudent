import tkinter
from tkinter import filedialog as fd
import os

def checkFile(name):
    split_tup = os.path.splitext(filename)
    if (split_tup[1] != ".ma"):
        print("That file no good")
        return
    writeFile(name)

def writeFile(filename):
    lines = ""
    with open(filename, "r") as fl:
        lines = fl.readlines()
    with open(filename, "w") as fl:
        for line in lines:
            if line.strip("\n") != "fileinfo \"license\" \"student\";":
                fl.write(line)

if __name__ == "__main__":
    filename = fd.askopenfilename()
    checkFile(filename)