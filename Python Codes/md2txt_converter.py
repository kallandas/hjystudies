import os
import re
from urllib.parse import quote

# Function to find all .md files in a directory
def find_md_files(directory):
    md_files = []
    for filename in os.listdir(directory):
        if filename.endswith('.md') and os.path.isfile(os.path.join(directory, filename)):
            md_files.append(filename)
    return md_files

# Function to convert .md file to .txt file with transformations
def convert_md_to_txt(input_md, output_txt):
    with open(input_md, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    # Apply transformations to the first two lines
    lines[:2] = [re.sub(r'#([^#\s]+)', r'[[\1]]', line) for line in lines[:2]]

    # Join the lines back together and apply other transformations
    content = ''.join(lines)
    content = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'[[\2|\1]]', content) #convert outer link
    content = re.sub(r'###\s+(.+)', r'==== \1 ====', content)   #convert header level by level
    content = re.sub(r'##\s+(.+)', r'===== \1 =====', content)
    content = re.sub(r'#\s+(.+)', r'====== \1 ======', content)
    content = re.sub(r'!\[\[([^\]]+)\]\]', r'{{:\1|}}', content)  #convert image link
    content = re.sub(r'^\*\s+(.+)', r'  * \1', content, flags=re.MULTILINE)  #convert ?

    with open(output_txt, 'w', encoding='utf-8') as outfile:
        outfile.write(content)

# Directory containing .md files
directory_path = "C:\Work\RGL_Local\md files"  # Replace with your directory path

# Ensure the 'text_files' subfolder exists
text_files_directory = os.path.join(directory_path, "text_files")
os.makedirs(text_files_directory, exist_ok=True)

# Find all .md files
md_files = find_md_files(directory_path)

# Convert each .md file to .txt
for md_file in md_files:
    input_md_path = os.path.join(directory_path, md_file)
    base_name = os.path.splitext(md_file)[0]
    url_encoded_name = quote(base_name)
    output_txt_path = os.path.join(text_files_directory, url_encoded_name + '.txt')
    convert_md_to_txt(input_md_path, output_txt_path)
    print(f"Converted '{md_file}' to URL-encoded '{output_txt_path}'")
