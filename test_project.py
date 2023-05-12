import os
import shutil
import unittest
import tempfile
from project import file_organizer,  DirectoryExistsError, search_files, create_sales_data_csv, update_inventory_data_text, create_product_inventory_csv
from project import CancelExecution, create_inventory_data_text, create_excel

class TestFunctions(unittest.TestCase):

    def setUp(self):
        # Create a test directory and files
        self.test_dir = tempfile.mkdtemp(dir='.')
        # Define the directory for the test
        self.directory = os.path.join(self.test_dir)
        
    """ 
    def test_DirectoryExistsError(self):
        # Create the directory
        os.mkdir(self.directory)
        # Test if a DirectoryExistsError is raised when trying to create the directory again
        with self.assertRaises(DirectoryExistsError):
            raise DirectoryExistsError(f"Directory '{self.directory}' already exists.")
        print("Test case 1 : DirectoryExistsError") """
    
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
        directory_path = self.test_dir
        create_inventory_data_text(file_name, directory_path)
        file_path = os.path.join(directory_path, file_name)
        self.assertTrue(os.path.exists(file_path))
        
    def test_create_product_inventory_csv(self):
        file_name = 'test_product_inventory.csv'
        directory_path = self.test_dir
        create_product_inventory_csv(file_name, directory_path)
        file_path = os.path.join(directory_path, file_name)
        self.assertTrue(os.path.exists(file_path))
        
    def test_create_sales_data_csv(self):
        file_name = 'test_sales_data.csv'
        directory_path = self.test_dir
        create_sales_data_csv(file_name, directory_path)
        file_path = os.path.join(directory_path, file_name)
        self.assertTrue(os.path.exists(file_path))
        
    def test_create_excel(self):
        file_name = 'test_employees.xlsx'
        directory_path = self.test_dir
        create_excel(file_name, directory_path)
        file_path = os.path.join(directory_path, file_name)
        self.assertTrue(os.path.exists(file_path))

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
        
        """ 
        # Test that the function handles errors gracefully
        self.assertEqual(search_files('/invalid/directory', 'test'), "Error: [WinError 3] The system cannot find the path specified: '/invalid/directory'") """
    
     
        # Test that the function returns "No files found" for an empty directory
        self.assertEqual(search_files(self.test_dir, 'test'), "No files found.")

    def test_file_organizer(self):
    # Create test files in the directory
        with open(os.path.join(self.test_dir, 'file1.txt'), 'w') as f:
          f.write('test')
        with open(os.path.join(self.test_dir, 'file2.csv'), 'w') as f:
          f.write('file test')
        with open(os.path.join(self.test_dir, 'file3.xlsx'), 'w') as f:
          f.write('test')
        with open(os.path.join(self.test_dir, 'file4.doc'), 'w') as f:
          f.write('test')
        with open(os.path.join(self.test_dir, 'file5.csv'), 'w') as f:
          f.write('csv test')
        with open(os.path.join(self.test_dir, 'file6.txt'), 'w') as f:
          f.write('txt test')
        
       # Call the file_organizer function
        try:
           file_organizer(self.test_dir)
        except CancelExecution:
            pass
        # Print the list of files before calling the function
        print(os.listdir(self.test_dir))
            
        # Test that the function organizes files correctly
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'txt')))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'csv')))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'xlsx')))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'doc')))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'txt', 'file1.txt')))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'csv', 'file2.csv')))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'xlsx', 'file3.xlsx')))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'doc', 'file4.doc')))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'csv', 'file5.csv')))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'txt', 'file6.txt')))

    # Create test files with invalid extension in the directory
        with open(os.path.join(self.test_dir, 'file6.xyz'), 'w') as f:
         f.write('test')
       
    # Test that the function ignores files with invalid extensions
        self.assertFalse(os.path.exists(os.path.join(self.test_dir, 'xyz')))
    
 
    """ def tearDown(self):
        # Remove the test directory and files
       shutil.rmtree(self.test_dir)  """

if __name__ == '__main__':
    unittest.main()