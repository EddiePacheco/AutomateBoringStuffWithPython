#!/usr/bin/env python3
# This script reads content from a text file and writes it to a spreadsheet, one line of text per row.
# The lines of the first text file will be in the cells of column A,
# The lines of the second text file will be in the cells of column B, and so on.

import openpyxl, sys, logging, os
logging.basicConfig(filename='text_file_to_spreadsheet.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

if len(sys.argv) < 2:
    print('Usage: python text_file_to_spreadsheet.py file1.txt file2.txt ...')
    logging.error('No text files provided. Exiting program.')
    sys.exit()

# Read the text files
text_files = sys.argv[1:]
text_lines = []
for text_file in text_files:
    try:
        with open(text_file, 'r') as file:
            text_lines.append(file.readlines()) # text_lines is a list of lists
            logging.info(f'Read {text_file} successfully.')
    except Exception as e:
        logging.error(f'Error reading {text_file}: {e}')
        print(f'Error reading {text_file}: {e}')
        sys.exit()

# Create a new spreadsheet
wb = openpyxl.Workbook()
sheet = wb.active
logging.info('Created a new spreadsheet.')

# Write the text lines to the spreadsheet
for i in range(len(text_lines)):
    for j in range(len(text_lines[i])): # text_lines[i] is a list
        sheet.cell(row=j+1, column=i+1).value = text_lines[i][j].strip() # strip() removes the newline character
logging.info('Written text lines to the spreadsheet.')

# Function to generate a new filename
def get_new_filename(base_name, extension):
    i = 1
    while os.path.exists(f"{base_name}_{i}.{extension}"):
        i += 1
    return f"{base_name}_{i}.{extension}"

# Save the spreadsheet with a dynamically incremented filename
filename = get_new_filename('text_files', 'xlsx')
wb.save(filename)
logging.debug(f'Spreadsheet saved as {filename}')
print(f'Spreadsheet saved as {filename}')
