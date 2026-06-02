# import the os package
import os

# function list file in folder

def list_folder_file(folder_path):
    try:
        files = os.listdir(folder_path)
        return files, None 
    except FileNotFoundError:
        return None, "Folder not found"
    except PermissionError:
        return None, "Permission dinied"

# main function
def main():
    folders = input("Please enter the list of folders separated by space: ").split()
    for folder in folders:
        files, error_message = list_folder_file(folder)
        if files:
            print(f"File in folder, {folder}")
            for file in files:
                print(file)
        else:
            print(f"error in {folder}: {error_message}")
if __name__ == "__main__":
    main()



        