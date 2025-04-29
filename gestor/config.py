import sys
import os

# Get the directory of the current script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define the database path
DATABASE_PATH = os.path.join(BASE_DIR, 'clientes.csv')

# Use a separate file for tests
if 'pytest' in sys.argv[0]:
    DATABASE_PATH = os.path.join(BASE_DIR, 'tests', 'clientes_test.csv')
