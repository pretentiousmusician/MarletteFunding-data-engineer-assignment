"""
This is the entrypoint to the program. 'python main.py' will be executed and the
expected csv file should exist in ../data/destination/ after the execution is complete.
"""
import os
import pathlib
import src.etl_utils as etl
from src.some_storage_library import SomeStorageLibrary

project_root = pathlib.Path(__file__).parent.parent.resolve()
column_file = os.path.join(project_root, 'data', 'source', 'SOURCECOLUMNS.txt')
data_file = os.path.join(project_root, 'data', 'source', 'SOURCEDATA.txt')
output_file = 'output.csv'


def main():
    etl.create_csv_from_raw_data(column_file, data_file, output_file)
    storage = SomeStorageLibrary()
    storage.load_csv(output_file)


if __name__ == '__main__':
    """Entrypoint"""
    print('Beginning the ETL process...')
    main()
