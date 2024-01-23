import csv
import os

"""
    This code read image data management .csv file and refer to the image's original filenames on the .csv
    and replace it with renamed image filename on all converted .txt file. Therefore providing the correct link for DocuWiki upload txt file.
    
"""
def read_and_process_csv(csv_file_path, folder_path):
    not_found_count = 0
    processed_rows = []

    with open(csv_file_path, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # Skip the header row
        header.append('D')  # Add column D for new filenames
        processed_rows.append(header)

        for row in csv_reader:
            original_filename, category, number = row[1], row[2], row[0]
            file_path = os.path.join(folder_path, original_filename)

            if os.path.isfile(file_path):
                # Rename file based on the rules
                extension = os.path.splitext(original_filename)[1].lower()
                category_code = {'Map': 'map', 'Character': 'cha', 'Monster': 'mon', 'ETC': 'etc'}.get(category, 'unknown')
                new_filename = f"RO_{category_code}_{number}{extension}".lower()
                new_file_path = os.path.join(folder_path, new_filename)

                # Rename the file
                os.rename(file_path, new_file_path)

                # Update row with new filename
                row.append(new_filename)
            else:
                not_found_count += 1
                row.append('')  # No new filename

            processed_rows.append(row)

##            if not_found_count > 3:
##                print("More than 3 files not found. Terminating process.")
##                break

    return processed_rows

def write_csv(csv_file_path, processed_rows):
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(processed_rows)

# Paths
csv_file = 'C:/Work/RGL_Local/imagefile/옵시디언_resource_File_list.csv'  # Replace with your CSV file path
folder_path = 'C:/Work/RGL_Local/imagefile'  # Replace with your folder path

# Process CSV and rename files
processed_data = read_and_process_csv(csv_file, folder_path)

# Write the processed data back to the CSV
write_csv(csv_file, processed_data)
