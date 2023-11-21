import os
import win32com.client

# Connect to Outlook
outlook = win32com.client.Dispatch("Outlook.Application")
namespace = outlook.GetNamespace("MAPI")

# Recursive function to print folder structure
def print_folders(folder, indent="", file=None):
    print(indent + folder.Name, file=file)
    for subfolder in folder.Folders:
        print_folders(subfolder, indent + "  ", file=file)

# Get the path to the Desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Open a text file on the Desktop for writing
with open(os.path.join(desktop_path, "outlook_folders.txt"), "w") as file:
    # Print the folder structure starting from the root
    for folder in namespace.Folders:
        print_folders(folder, file=file)
