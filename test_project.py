import os
import shutil
import unittest
import tempfile
from project import file_organizer,  DirectoryExistsError, search_files, create_sales_data_csv, update_inventory_data_text, create_product_inventory_csv
from project import create_inventory_data_text, create_excel

class TestFunctions(unittest.TestCase):

    def setUp(self):
        # Create a test directory and files
        self.test_dir = tempfile.mkdtemp(dir='.')
        # Define the directory for the test
        self.directory = os.path.join(self.test_dir)
    
    def test_DirectoryExistsError(self):
       # Define the directory for the test
        self.directory = os.path.join(self.test_dir, 'test_dir')
       # Create the directory
        os.mkdir(self.directory)
        # Test if a DirectoryExistsError is raised when trying to create the directory again
        with self.assertRaises(DirectoryExistsError):
          raise DirectoryExistsError(f"Directory '{self.directory}' already exists.")
        print("Test case 2 : DirectoryExistsError, 'test_dir' is already exists")

    def test_create_inventory_data_text(self):
        file_name = 'test_inventory_data.txt'
        directory = self.test_dir
        create_inventory_data_text(file_name, directory)
        file_path = os.path.join(directory, file_name)
        self.assertTrue(os.path.exists(file_path))
        
    def test_create_product_inventory_csv(self):
        file_name = 'test_product_inventory.csv'
        directory = self.test_dir
        create_product_inventory_csv(file_name, directory)
        file_path = os.path.join(directory, file_name)
        self.assertTrue(os.path.exists(file_path))
        
    def test_create_sales_data_csv(self):
        file_name = 'test_sales_data.csv'
        directory = self.test_dir
        create_sales_data_csv(file_name, directory)
        file_path = os.path.join(directory, file_name)
        self.assertTrue(os.path.exists(file_path))
        
    def test_create_excel(self):
        file_name = 'test_employees.xlsx'
        directory = self.test_dir
        create_excel(file_name, directory)
        file_path = os.path.join(directory, file_name)
        self.assertTrue(os.path.exists(file_path))

    def test_update_inventory_data_text(self):
        # create a test file for inventory data
        inventory_file = 'test_inventory.txt'
        with open(os.path.join(self.test_dir, inventory_file), 'w') as f:
            f.write("Aspirin, 500, 20\nParacetamol, 1000, 15\nIbuprofen, 800, 25\n")
       # call the function to update inventory data
        update_inventory_data_text(inventory_file, self.test_dir)
        # check if the inventory data is updated correctly
        with open(os.path.join(self.test_dir, inventory_file), 'r') as f:
            updated_data = f.readlines()
        expected_data = ["Aspirin, 600, 25\n", "Paracetamol, 1000, 15\n", "Ibuprofen, 1000, 20\n"]
        self.assertEqual(updated_data, expected_data)

    def test_search_files(self):
        # Create test files in the directory
        with open(os.path.join(self.test_dir, 'test_file1.txt'), 'w') as f:
            f.write('hello')
        with open(os.path.join(self.test_dir, 'test_file2.csv'), 'w') as f:
            f.write('hello world')
        with open(os.path.join(self.test_dir, 'test_file3.xlsx'), 'w') as f:
            f.write('python')
        with open(os.path.join(self.test_dir, 'test_file4.doc'), 'w') as f:
            f.write('java')
        with open(os.path.join(self.test_dir, 'test_file5.txt'), 'w') as f:
            f.write('hello')
        with open(os.path.join(self.test_dir, 'test_file6.csv'), 'w') as f:
            f.write('HELLO WORLD')
        with open(os.path.join(self.test_dir, 'test_file7.txt'), 'w') as f:
            f.write('hello\nworld\n')
        
        # Test that the function finds files with matching text
        self.assertEqual(search_files(self.test_dir, 'hello'), "Files found:\nFile name: test_file1.txt\nFile path: " + os.path.join(self.test_dir, 'test_file1.txt') + "\nFile name: test_file2.csv\nFile path: " + os.path.join(self.test_dir, 'test_file2.csv') + "\nFile name: test_file5.txt\nFile path: " + os.path.join(self.test_dir, 'test_file5.txt') + "\nFile name: test_file6.csv\nFile path: " + os.path.join(self.test_dir, 'test_file6.csv') + "\nFile name: test_file7.txt\nFile path: " + os.path.join(self.test_dir, 'test_file7.txt') + "\nTotal number of search files: 5")
        self.assertEqual(search_files(self.test_dir, 'PYTHON'), "Files found:\nFile name: test_file3.xlsx\nFile path: " + os.path.join(self.test_dir, 'test_file3.xlsx') + "\nTotal number of search files: 1")
        
        # Test that the function returns "No files found" if no matching files are found
        self.assertEqual(search_files(self.test_dir, 'no_match'), "No files found.")
            
        # Test that the function returns "No files found" for an empty directory
        self.assertEqual(search_files(self.test_dir, 'test'), "No files found.")
    
    def test_file_organizer(self):
        # Create some test files in the test directory
        test_files = ['file1.txt', 'file2.csv', 'file3.doc', 'file4.xlsx', 'file5.pdf', 'file6.xyz']
        for file in test_files:
            file_path = os.path.join(self.directory, file)
            open(file_path, 'w').close()

        # Call the function to be tested
        file_organizer(self.directory)

        # Check if the files are properly organized in subdirectories based on their extensions
        for file in test_files[:4]:
           extension = file.split('.')[-1]
           subdirectory = os.path.join(self.directory, extension)
           print(f"Checking if subdirectory exists: {subdirectory}")

        # Check if the unorganized files are still in the directory
        for file in test_files[4:]:
           file_path = os.path.join(self.directory, file)
           print(f"Checking if unorganized file exists: {file_path}")

    """ def tearDown(self):
        # Remove the test directory and files
        shutil.rmtree(self.test_dir) """

if __name__ == '__main__':
    unittest.main()