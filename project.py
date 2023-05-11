import os
import shutil
import glob
import csv
import random
import re
from openpyxl import Workbook
from tqdm import tqdm
import signal

# Define custom exception for directory already exists
class DirectoryExistsError(Exception):
    pass
try:
    # Create directory if it doesn't exist
    directory = 'C:\\Users\\jeetj\mycapstone_project'
    if os.path.isdir(directory):
        # Check if directory already exists and raise exception if it does
        raise DirectoryExistsError(f"Directory '{directory}' already exists.")
    # If the directory doesn't exist, create it
    else:
        os.mkdir(directory)
        print(f"Directory '{directory}' created successfully.")
except DirectoryExistsError as e:
    # Print error message if directory already exists
    print("Error:", e)



def search_files(directory_path, text_pattern):
    try:
        # Define the file extensions to search for
        file_extensions = (".txt", ".doc", ".csv", ".xlsx", ".docx",)        
        # Create an empty list to store the matching file paths
        files_found = []       
        # Compile the regular expression pattern
        pattern = re.compile(text_pattern, re.IGNORECASE)
        # Use os.walk() to recursively search for files in the directory
        for subdir, dirs, files in os.walk(directory_path):
            for file in files:
                # Check if the file extension matches any of the desired extensions
                file_ext = os.path.splitext(file)[-1].lower()
                if file_ext in file_extensions:
                    # If a match is found, add the file path to the list
                    file_path = os.path.join(subdir, file)
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        for line in f:
                            if pattern.search(line):
                                files_found.append(file_path)
                                break
        # If one or more files are found, return their paths and count
        if files_found:
            result = "Files found:\n"
            for file in files_found:
                result += f"File name: {os.path.basename(file)}\nFile path: {file}\n"
            result += f"Total number of search files: {len(files_found)}"
            print(result)
            return result
        else:
            print("No files found.")
            return "No files found."  
    except FileNotFoundError as e:
        error_msg = f"Error: {e.strerror}: '{directory_path}'"
        print(error_msg)
        raise Exception(error_msg)
    except Exception as e:
        error_msg = f"Error: {e}"
        print(error_msg)
        raise Exception(error_msg)
    

def create_inventory_data_text(file_name, directory_path):
    # Creates a list of tuples called inventory_data that contains the name, units in stock, and days' supply for each drug
    inventory_data = [("Acetaminophen", 1000, 30),
                  ("Ibuprofen", 750, 15),
                  ("Aspirin", 500, 25),
                  ("Lisinopril", 100, 10),
                  ("Metformin", 250, 20),
                  ("Atorvastatin", 300, 15),
                  ("Cephalexin", 200, 5),
                  ("Clopidogrel", 150, 30),
                  ("Furosemide", 400, 20),
                  ("Lorazepam", 50, 10)]
    # sort the inventory_data based on units in stock
    #inventory_data.sort(key=lambda x: (x[1], x[2]))
    with open(os.path.join(directory_path, file_name), 'w') as f:
        # writes the header row to the file.
        f.write('Drug Name, Units in Stock, Days\' Supply\n')
        for drug in inventory_data:
        # Writes line each drug's name, units in stock, and days' supply to the file.
            f.write(f'{drug[0]}, {drug[1]}, {drug[2]}\n')
    print('TEXT file created: ', file_name)

def update_inventory_data_text(file_name, directory_path):
    # Open the file in read mode to read the existing data
    with open(os.path.join(directory_path, file_name), 'r') as f:
        lines = f.readlines()
    # Find the indices of the lines containing the data for "Aspirin" and "Ibuprofen"
    aspirin_index = -1
    ibuprofen_index = -1
    for i, line in enumerate(lines):
        if "Aspirin" in line:
            aspirin_index = i
        elif "Ibuprofen" in line:
            ibuprofen_index = i
    # If either drug is not found in the file, exit the function
    if aspirin_index == -1 or ibuprofen_index == -1:
        print("Error: Drug not found in file.")
        return
    # Update the unit in stock for "Aspirin" and "Ibuprofen"
    lines[aspirin_index] = "Aspirin, 600, 25\n"
    lines[ibuprofen_index] = "Ibuprofen, 1000, 20\n"
    # Open the file in write mode to write the updated data
    with open(os.path.join(directory_path, file_name), 'w') as f:
        f.writelines(lines)

    print('Inventory data updated:', file_name)

def create_product_inventory_csv(file_name, directory_path):
    # Create a new .csv file with the given name
    with open(os.path.join(directory_path, file_name), 'w', newline='') as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow(['Product Name', 'Product Code', 'Batch Number', 'Manufacturing Date', 'Expiry Date', 'Quantity', 'Location'])      
        # Write the data rows
        writer.writerow(['Aspirin', 'AS100', 'BN123', '2022-05-01', '2023-04-30', 5000, 'Warehouse A'])
        writer.writerow(['Ibuprofen', 'IB200', 'BN456', '2022-06-15', '2023-06-14', 3000, 'Warehouse B'])
        writer.writerow(['Amoxicillin', 'AM500', 'BN789', '2022-07-01', '2023-06-30', 4000, 'Warehouse C'])
        writer.writerow(['Paracetamol', 'PA500', 'BN321', '2022-08-01', '2023-07-31', 2000, 'Warehouse A'])
    print('CSV created: ', file_name)

def create_sales_data_csv(file_name, directory_path):
    # Create a new .csv file with the given name
    with open(os.path.join(directory_path, file_name), 'w', newline='') as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow(['Date', 'Product Name', 'Product Code', 'Quantity', 'Unit Price', 'Total Price', 'Customer Name', 'Customer Email'])      
        # Write the data rows
        writer.writerow(['2022-05-01', 'Aspirin', 'AS100', 100, 0.50, 50.00, 'ABC Pharmacy', 'info@abcpharmacy.com'])
        writer.writerow(['2022-05-01', 'Ibuprofen', 'IB200', 50, 0.75, 37.50, 'XYZ Pharmacy', 'info@xyzpharmacy.com'])
        writer.writerow(['2022-05-02', 'Amoxicillin', 'AM500', 150, 1.25, 187.50, 'LMN Healthcare', 'orders@lmnhealthcare.com'])
        writer.writerow(['2022-05-03', 'Paracetamol', 'PA500', 200, 1.00, 200.00, 'DEF Pharmacy', 'info@defpharmacy.com'])
    print('CSV created: ', file_name)

def create_excel(file_name, directory_path):
    # Create a new Excel workbook with the given name
    workbook = Workbook()
    worksheet = workbook.active   
    # Write the header row
    header = ['Employee ID', 'Name', 'Position', 'Department', 'Hire Date', 'Salary']
    worksheet.append(header)   
    # Write the data rows
    rows = [['001', 'John Smith', 'Sales Manager', 'Sales', '2020-01-01', '$80,000'],
        ['002', 'Jane Doe', 'Researcher', 'Research', '2020-02-15', '$60,000'],
        ['003', 'Mike Johnson', 'Chemist', 'Production', '2019-10-01', '$70,000'],
        ['004', 'Sarah Lee', 'HR Manager', 'HR', '2021-03-15', '$90,000']]
    for row in rows:
        worksheet.append(row)   
    # Save the workbook
    #workbook.save(os.path.join(directory_path, file_name + '.xlsx'))
    workbook.save(os.path.join(directory_path, file_name))
    print('Excel file created: ', file_name)

""" def file_organizer(directory):
   # Get the list of all files in the directory
    #breakpoint()  # Pause to inspect the files list
    files = os.listdir(directory)
    print("Files in directory:", files)  # Print the files list for inspection
    # Loop through each file in the directory
    for file in files:
        # Get the full file path
        file_path = os.path.join(directory, file)
        print("File path:", file_path)  # Print the file path for inspection
        #breakpoint()  # Pause to inspect the file path
        # Check if the file is a .doc, .txt, .csv, or .xlsx file
        if file.endswith(('.doc', '.txt', '.csv', '.xlsx',)):
            # Create a subdirectory based on the file extension
            subdirectory = os.path.join(directory, file.split('.')[-1])
            os.makedirs(subdirectory, exist_ok=True)
            # Move the file to the subdirectory
            new_file_path = os.path.join(subdirectory, file)
            shutil.move(file_path, new_file_path)
            #breakpoint()  # Pause to inspect the file moving operation
    print("File organization completed.") """

""" def file_organizer(directory):
    # Get the list of all files in the directory
    files = os.listdir(directory)
    print("Scanning for files in directory:", directory)
    # Loop through each file in the directory
    files_scanned = 0
    files_organized = 0
    for i, file in enumerate(files):
        # Get the full file path
        file_path = os.path.join(directory, file)
        # Check if the file is a .doc, .txt, .csv, or .xlsx file
        if file.endswith(('.doc', '.txt', '.csv', '.xlsx',)):
            # Create a subdirectory based on the file extension
            subdirectory = os.path.join(directory, file.split('.')[-1])
            os.makedirs(subdirectory, exist_ok=True)
            # Move the file to the subdirectory
            new_file_path = os.path.join(subdirectory, file)
            shutil.move(file_path, new_file_path)
            files_organized += 1
        files_scanned += 1
        # Update progress every 10 files
        if i % 5 == 0:
            print(f"Processed {i+1} files out of {len(files)}")
    print("Scanning and organizing files completed.")
    print(f"Total files scanned: {files_scanned}")
    print(f"Total files organized: {files_organized}")
#This code will print out a progress message every 10 files processed and then print the final results of the scanning 
#and organizing process, including the total number of files scanned and the total number of files organized. """


class CancelExecution(Exception):
    pass
def signal_handler(signal, frame):
    raise CancelExecution("Scanning/organizing files canceled by user.")

def file_organizer(directory):
    # Get the list of all files in the directory
    files = os.listdir(directory)
    print("Scanning for files in directory:", directory)
    # Loop through each file in the directory
    files_scanned = 0
    files_organized = 0
    with tqdm(total=len(files), unit="file") as progress_bar:
        signal.signal(signal.SIGINT, signal_handler)
        for file in files:
            # Get the full file path
            file_path = os.path.join(directory, file)
            # Check if the file is a .doc, .txt, .csv, or .xlsx file
            if file.endswith(('.txt', '.csv', '.xlsx', '.doc',)):
                # Create a subdirectory based on the file extension
                subdirectory = os.path.join(directory, file.split('.')[-1])
                os.makedirs(subdirectory, exist_ok=True)
                # Move the file to the subdirectory
                new_file_path = os.path.join(subdirectory, file)
                shutil.move(file_path, new_file_path)
                files_organized += 1
            files_scanned += 1
            progress_bar.update(1)
            # Check for user input to cancel process
            if input("Press 'q' to cancel file organizing process: ") == 'q':
                if input("Do you want to continue with the process? (y/n): ") == 'n':
                    print("File organizing process cancelled.")
                    return
    print("Scanning and organizing files completed.")
    print(f"Total files scanned: {files_scanned}")
    print(f"Total files organized: {files_organized}")

def main():
    # call function to organize the root directory by placing 3 types of files into respective sub-directories
    directory = "C:\\Users\\jeetj\\mycapstone_project"   
    #call function to create a .text file
    create_inventory_data_text('inventory_data_Jan5.txt', directory)   
    #call function to update a .text file
    update_inventory_data_text('inventory_data_Feb3.txt', directory) 
    #call function to create a .csv file
    create_product_inventory_csv('productinventory3.csv', directory)  
    create_sales_data_csv('SalesData.csv', directory)
    #call function to create a .xlsx file
    create_excel('EmployeeData1.xlsx', directory)
    text_pattern = input("Enter a text pattern to search for: ")
    search_files(directory, text_pattern)
    file_organizer(directory)
    DirectoryExistsError(directory)
    CancelExecution(directory)
   
   

if __name__ == '__main__':
    main()
