import csv

"""
Covnvert raw source data into a 2D list of rows.
Default delimiter is '|'
"""
def extract_source_data(filepath: str, delim='|') -> list:
    with open(filepath, 'r') as f:
        # Read each line into a list, dropping each newline char.
        lines = [line.rstrip() for line in f.readlines()]
        # Separate each line on the delimiter and map to a list.
        # Creates 2D list of rows.
        rows = list(map(lambda l: l.split(delim), lines))
        return rows


"""
Extract raw data from source files into 2D lists of rows.
Create CSV from data and sorted columns.
"""
def create_csv_from_raw_data(column_file: str, data_file: str, output_file: str) -> None:
    columns = extract_source_data(column_file)
    data = extract_source_data(data_file)
    # Transform raw source data into a formatted CSV file
    convert_raw_data_to_csv(columns, data, output_file)


"""
Create CSV file with header using raw data and column info from source files.
"""
def convert_raw_data_to_csv(unsorted_columns: list, data: list, output_file: str) -> None:
    header = map_columns_to_header(unsorted_columns)
    with open(output_file, 'w', newline='') as csvfile:
        # Instantiate csv writer and set header
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()
        # Write each row of data, matched with the proper column, to the csv
        for row in data:
            writer.writerow(dict(zip(header, row)))


"""
Convert a list of [order, column_name] pairs into a sorted list of column names that
can be used as a header
"""
def map_columns_to_header(unsorted_columns: list) -> list:
    # Sort the column names according to the int in first column.
    sorted_columns = sorted(unsorted_columns, key=lambda x: int(x[0]))
    # Map sorted column names to new list, dropping the integer column.
    return list(map(lambda x: x[1], sorted_columns))
