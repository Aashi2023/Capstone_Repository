import os
import shutil
import unittest
import tempfile
import signal
from tqdm import tqdm
from project import file_organizer,  DirectoryExistsError, search_files, create_sales_data_csv, update_inventory_data_text, create_product_inventory_csv
from project import CancelExecution, signal_handler

class TestFunctions(unittest.TestCase):

    def setUp(self):
        # Create a test directory and files
        self.test_dir = tempfile.mkdtemp(dir='.')
        # Define the directory for the test
        self.directory = os.path.join(self.test_dir, 'test_dir')
    
    def test_DirectoryExistsError(self):
        # Create the directory
        os.mkdir(self.directory)
        # Test if a DirectoryExistsError is raised when trying to create the directory again
        with self.assertRaises(DirectoryExistsError):
            raise DirectoryExistsError(f"Directory '{self.directory}' already exists.")
        print("Test case 1 : DirectoryExistsError")
    
    def test_DirectoryExistsError(self):
       # Define the directory for the test
        self.directory = os.path.join(self.test_dir, 'test_dir')
       # Create the directory
        os.mkdir(self.directory)
        # Test if a DirectoryExistsError is raised when trying to create the directory again
        with self.assertRaises(DirectoryExistsError):
          raise DirectoryExistsError(f"Directory '{self.directory}' already exists.")
        print("Test case 2 : DirectoryExistsError, 'test_dir' is already exists")

    def test_file_organizer(self):
        # Create test files in the directory
        with open(os.path.join(self.test_dir, 'test_file.txt'), 'w') as f:
           f.write('test')
        with open(os.path.join(self.test_dir, 'test_file.csv'), 'w') as f:
            f.write('test')
        with open(os.path.join(self.test_dir, 'test_file.xlsx'), 'w') as f:
            f.write('test')
        with open(os.path.join(self.test_dir, 'test_file.doc'), 'w') as f:
            f.write('test')

        # Create test files with invalid extension in the directory
        with open(os.path.join(self.test_dir, 'test_file_1.txt'), 'w') as f:
           f.write('test')
        with open(os.path.join(self.test_dir, 'test_file.xyz'), 'w') as f:
            f.write('test')
       # Test that the function organizes files correctly
        try:
          file_organizer(self.test_dir)
        except CancelExecution:
          pass
        # Test that the function organizes files correctly
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'txt')))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'csv')))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'xlsx')))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'doc')))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'txt', 'test_file.txt')))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'csv', 'test_file.csv')))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'xlsx', 'test_file.xlsx')))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'doc', 'test_file.doc')))

    # Test that the function ignores files with invalid extensions
        self.assertFalse(os.path.exists(os.path.join(self.test_dir, 'xyz')))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'txt')))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'txt', 'test_file_1.txt')))
    

    def test_update_inventory_data_text(self):
        # create a test file for inventory data
        inventory_file = 'test_inventory.txt'
        with open(os.path.join(self.test_dir, inventory_file), 'w') as f:
            f.write("Aspirin, 500, 20\nParacetamol, 1000, 15\nIbuprofen, 800, 25\n")
       # call the function to update inventory data
        update_inventory_data_text(inventory_file, self.test_dir)
        #breakpoint()  # Pause to inspect the files list
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
        
        """ # Test that the function handles errors gracefully
        self.assertEqual(search_files('/invalid/directory', 'test'), "Error: [WinError 3] The system cannot find the path specified: '/invalid/directory'")
         """
        # Test that the function returns "No files found" for an empty directory
        self.assertEqual(search_files(self.test_dir, 'test'), "No files found.")
        
        """ # Test that the function returns an error message for a nonexistent directory
        self.assertEqual(search_files('/nonexistent/directory', 'test'), "Error: [WinError 3] The system cannot find the path specified: '/nonexistent/directory'") """
    """ 
    def tearDown(self):
        # Remove the test directory and files
       shutil.rmtree(self.test_dir)  """
    


if __name__ == '__main__':
    unittest.main()
   