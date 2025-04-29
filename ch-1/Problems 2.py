import os

# Set the directory you want to list (use '.' for current directory)
directory_path = r'C:\Users\Admin\OneDrive\Desktop\salesforce practical'

try:
    # List all files and directories in the given path
    contents = os.listdir(directory_path)
    
    print(f"Contents of '{directory_path}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print("The specified directory does not exist.")
except PermissionError:
    print("You do not have permission to access this directory.")
