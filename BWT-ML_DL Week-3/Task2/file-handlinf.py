def read_file(file_path):
    
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            print("File Contents:")
            print(contents)
            
            # Counting words in the file
            word_count = len(contents.split())
            print(f"\nNumber of words in the file: {word_count}")
            
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except IOError:
        print(f"Error: Could not read the file '{file_path}'.")

# Writing File
def write_to_file(file_path, content):
    
    try:
        with open(file_path, 'w') as file:
            file.write(content)
            print(f"Content successfully written to '{file_path}'.")
    except IOError:
        print(f"Error: Could not write to the file '{file_path}'.")


if __name__ == "__main__":
    read_file('data.txt')
    
    user_content = input("\nEnter content to write to 'output.txt': ")
    write_to_file('output.txt', user_content)
