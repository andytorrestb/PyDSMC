import unittest
import os
import sys
import importlib

def load_tests(loader, standard_tests, pattern):
    """
    Load test files from the 'tests' directory matching the pattern 'test_*.py'.
    """
    # Get the current directory
    this_dir = os.path.dirname(__file__)
    
    # Load all test cases that match 'test_*.py' in the 'tests' directory
    package_tests = loader.discover(start_dir=os.path.join(this_dir, 'tests'), pattern='test_*.py')
    
    # Add the discovered tests to the standard test suite
    standard_tests.addTests(package_tests)
    
    return standard_tests

if __name__ == '__main__':
    # To handle the NumPy initialization issue, try reloading the module
    if 'numpy' in sys.modules:
        importlib.reload(sys.modules['numpy'])  # Reload NumPy to avoid double initialization

    # Create a test loader and run the tests using TextTestRunner
    loader = unittest.TestLoader()
    
    # Automatically discover and load tests from the 'tests' directory
    # Ensure the correct directory is specified
    suite = loader.discover(start_dir=os.path.join(os.path.dirname(__file__), 'tests'), pattern='test_*.py')
    
    # Use TextTestRunner to execute the suite
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
