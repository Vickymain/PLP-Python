#File Read & Write Challenge
def file_read_write():
    try:
        with open("MainaLessons.txt", "r") as infile:
            content = infile.readlines()
        modified = [f"{i+1}: {line.upper()}" for i, line in enumerate(content)]
        with open("MainaLessonsModified.txt", "w") as outfile:
            outfile.writelines(modified)
        print("File successfully read and modified. Check MainaLessonsModified.txt")

    except FileNotFoundError:
        print("Error: MainaLessons.txt was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

#Error Handling Lab 
def error_handling_lab():
    filename = input("Enter the filename to read: ")

    try:
        with open(filename, "r") as f:
            print("File contents:")
            print(f.read())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: You don’t have permission to read '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


file_read_write()
error_handling_lab()
