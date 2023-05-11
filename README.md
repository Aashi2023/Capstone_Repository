# Capstone_Repository

User Stories:

As a user, I want to be able to organize my files based on their extensions so that I can easily find them later.
As a user, I want to be able to search for files containing a specific text pattern so that I can quickly locate the files I need.
As a user, I want to be able to specify the directory to scan so that I can organize/search for files in a specific location.
As a user, I want to be able to see the progress of the scanning and organizing process so that I know how much time is left.
As a user, I want to be able to cancel the scanning/organizing process so that I can stop the program if necessary.
As a user, I want to be able to update inventory data by parsing CSV files and adding/updating records.
Overall, providing users with the option to cancel the scanning/organizing process can help make the program more user-friendly and prevent potential problems.

Technical Challenges:

Parsing the command-line arguments to get the directory to scan, the search pattern, and other options. 
Checking if a folder for a specific extension already exists and creating it if it doesn't. 
Moving files to their corresponding folders and handling errors if the destination folder cannot be created. Implementing the search function using regex and handling errors if the search pattern is invalid. 
Updating the inventory data file with accurate drug quantities. Designing and implementing tests for all the functions in the program to ensure correctness and robustness.


Approach:

Create a main function that parses the command-line arguments and calls the appropriate functions based on the options. 
Create four other functions: organize_files, search_files, Update_Inventory_Data, each of which handles a specific task. 
Use the os and shutil modules to manage files and directories, and the re module for regex. Implement tests for all the functions using pytest. Create a README.md file that documents the user stories, technical challenges, and how you tackled those challenges.

