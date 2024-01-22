
import os

"""
File list extraction to a text file.
Program: file_extract.py
Author: "Ji Yong Hwang"
Description 
An simple extraction of file names of a particular dicrectory onto a designated text file. 

Date: January 22nd, 2024
"""

def list_files_in_directory(directory):
    """
    Lists all files (excluding directories and hidden files) in the specified directory.
    Each file is represented as a string "<filename><extension>".

    :param directory: Path of the directory to list files from.
    :return: List of strings, each containing the filename and its extension.
    """
    files_list = []
    for filename in os.listdir(directory):
        # Construct the full file path
        file_path = os.path.join(directory, filename)
        
        # Check if it's a file and not a directory or hidden file
        if os.path.isfile(file_path) and not filename.startswith('.'):
            files_list.append(filename)
    
    return files_list

def export_to_file(files_list, output_file):
    """
    Exports the list of files to a UTF-8 encoded text file.

    :param files_list: List of file names to write to the file.
    :param output_file: Path of the output file.
    """
    with open(output_file, 'w', encoding='utf-8') as file:
        for filename in files_list:
            file.write(f"{filename}\n")

# Example usage
directory_path = "C://Users/USER/내 드라이브(ragnarokdarkuniverse@gmail.com)/라그옵시디안/라그라로크다크/resources"  # Replace with your directory path
output_file_path = "C://Work/RGL_Local//file.txt"  # Replace with your output file path

files = list_files_in_directory(directory_path)
export_to_file(files, output_file_path)
print(f"Files have been exported to {output_file_path}")



