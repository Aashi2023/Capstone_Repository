# Capstone_Repository

User Stories: My capstone "File Organizer" project.

User Story 1: 

As a user, I want to be able to create a text file with data on the name, units in stock, and days supply for various drugs so that I can easily access this information later.

User Story 2: 

As a user, I want to be able to update the data for specific drugs in the text file created earlier so that I can keep the information accurate and up-to-date.

User Story 3: 

As a user, I want to be able to create a CSV file with information on the product name, product code, batch number, manufacturing date, expiry date, quantity, and location for various drugs so that I can easily manage and track this information.

User Story 4: 

As a user, I want to be able to create a CSV file with information on the date of the sale, the product name, product code, quantity sold, unit price, total price, customer name, and customer email so that I can keep track of sales data.

User Story 5: 

As a user, I want to be able to search for files in a directory and its subdirectories that contain a specific text pattern so that I can quickly find the files I need.

User Story 6: 

As a user, I want to be able to organize files in a directory by moving them to subdirectories based on their extensions so that I can easily locate and access my files. The function should display a progress bar and allow me to cancel the process if necessary. The function should only move files with extensions .txt, .csv, .xlsx, .doc, and .pdf to their respective subdirectories.

Technical Challenges:

The below technical challenges encountered during the development of the File Organizer project:

Custom exception handling: 

Creating a custom exception class and handling it correctly can be challenging, especially if the developer is not familiar with Python's exception handling mechanism.

Working with different file formats: 

The project requires creating and working with different file formats, including text files, CSV files, and Excel files. Each of these file formats has its own syntax and conventions, and the developer needs to be familiar with them.

File searching: 

The search_files function needs to search for files in a directory and its subdirectories that match a specific text pattern. This can be challenging, especially if the directory contains a large number of files.

Progress bar implementation: 

The file_organizer function displays a progress bar to show the user the progress of the file organizing process. Implementing a progress bar can be challenging, especially if the developer is not familiar with the concept.

User input handling: The file_organizer function allows the user to cancel the process by pressing 'Cntrl C'. Handling user input correctly can be challenging, especially if the developer needs to handle multiple types of user input.


Overcoming Technical Challenges:

Custom exception handling: 

A custom exception class was created to handle the specific case of a directory already existing. This exception was then raised with an appropriate error message when the directory already exists.

Working with different file formats: 

The project utilized existing Python libraries such as 'csv' and 'openpyxl' to create and manipulate CSV and Excel files respectively. In addition, Python's built-in file handling mechanisms were used to create and manipulate text files.

File searching: 

The os module in Python was used to recursively search for files in a directory and its subdirectories that match the specified text pattern.

Progress bar implementation: 

The 'tqdm'module was used to implement the progress bar, which allowed for easy and customizable implementation of the progress bar functionality.

User input handling: 

Python's built-in 'input()' function was used to handle user input, and an if statement was used to check for the user input "E" and cancel the file organizing process if necessary.
