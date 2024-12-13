import tkinter as tk
from tkinter import filedialog

# hidden root window
root = tk.Tk()
root.withdraw()

# get dir to sort
directory = filedialog.askdirectory(title="Select Directory To Sort")
print(directory)


