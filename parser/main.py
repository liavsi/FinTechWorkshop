import MBO_Parser as mbp
import os
import gzip
import pandas as pd
import boto3
import sqlite3
import csv
from datetime import datetime


def combine_DataTables(path):
    # Get a list of all CSV files in the folder
    csv_files = [f for f in os.listdir(path)]

    # Initialize an empty DataFrame to store the combined data
    combined_data = pd.DataFrame()

    # Loop through each CSV file
    for f in csv_files:
        # Read the CSV file into a DataFrame
        file_path = os.path.join(path, f)
        data = pd.read_csv(file_path)

        # Append the data to the combined_data DataFrame
        combined_data = pd.concat([combined_data, data], ignore_index=True)

    output_dir_path = 'C:\\temp\\output'
    output_file_path = output_dir_path + '\\' + 'DataTable.csv'

    # Write the combined data to a new CSV file
    combined_data.to_csv(output_file_path, index=False)


def download_files_and_create_DataTables():
    # import AWS credentials
    AWS_Credentials = pd.read_csv('AWS_Credentials.csv')

    # Creating Session to the AWS S3 storage
    session = boto3.Session(
        aws_access_key_id=AWS_Credentials['aws_access_key_id'][0],
        aws_secret_access_key=AWS_Credentials['aws_secret_access_key'][0],
        region_name='eu-west-3'
    )
    s3 = session.client('s3')
    bucket_name = 'tase-rmbo-files'
    folder_name = 'rmbo files/rezef/'
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=folder_name)  # Creating list of files from the folder
    local_directory_path = r'C:\temp'
    output_directory_path = local_directory_path + '\\' + 'Data Tables'

    # Check if the folder exists
    if not os.path.exists(output_directory_path):
        # Create the folder
        os.makedirs(output_directory_path)

    # Iterating over the list of object in the storage
    for obj in response['Contents']:
        # Skip if the object is a folder
        if obj['Key'].endswith('/'):
            continue

        # Construct the local file path
        local_file_path = local_directory_path + '\\' + obj['Key'].split('/')[-1]

        # Download the file
        s3.download_file(bucket_name, obj['Key'], local_file_path)

        extracted_file_path = decompress_GZ_file(local_file_path)

        create_DataTable(extracted_file_path, output_directory_path)

        return output_directory_path


def create_DataTable(extracted_file_path, output_directory_path):
    # parse the necessary data from the MBO file into DataTable
    with open(extracted_file_path, 'rb') as MBO_File:
        file_name = os.path.splitext(os.path.basename(extracted_file_path))[0]
        csv_file_path = os.path.join(output_directory_path, "DataTable_" + file_name.split("_")[3] + ".csv")
        currentFile = mbp.MBO_Parser(MBO_File)
        pd.DataFrame(currentFile.parseFile()).to_csv(csv_file_path, index=False)
    # Remove the MBO file after extraction
    os.remove(extracted_file_path)


def get_folder(folder_path):
    # Get a list of all files in the folder
    file_list = os.listdir(folder_path)

    for file_name in file_list:
        if file_name.endswith(".rmbo.gz"):
            decompress_GZ_file(folder_path + '\\' + file_name)


def decompress_GZ_file(local_file_path):
    # Specify the path to save the extracted file
    extracted_file_path = os.path.splitext(local_file_path)[0]

    # Open the input GZIP file in binary read mode
    with gzip.open(local_file_path, 'rb') as gz_file:
        # Read the compressed contents
        decompressed_data = gz_file.read()

    # Write the decompressed data to the output file
    with open(extracted_file_path, 'wb') as file:
        file.write(decompressed_data)

    # Remove the GZ file after extraction
    os.remove(local_file_path)
    create_DataTable(extracted_file_path, "C:\workshop\extracted")
    return extracted_file_path


def convert_timestamp(csv_file):
    df = pd.read_csv(csv_file)
    timestamps = df['Timestamp'].values
    df['Date'] = pd.to_datetime(timestamps, unit='ns')
    df.drop('Timestamp', axis=1, inplace=True)
    df.to_csv(csv_file, index=False)

def convert_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            file_path = os.path.join(folder_path, filename)
            convert_timestamp(file_path)


def create_sql_script(folder_path, sql_file):
    with open(sql_file, 'w', encoding='utf-8') as f:
        f.write('CREATE TABLE IF NOT EXISTS transactions (\n')
        f.write('    ID TEXT PRIMARY KEY,\n')  # Define ID as the primary key
        f.write('    Transaction_ID TEXT,\n')
        f.write('    Name TEXT,\n')
        f.write('    Price REAL,\n')
        f.write('    Side TEXT,\n')
        f.write('    Volume REAL,\n')
        f.write('    Order_Executed TEXT,\n')
        f.write('    Target TEXT,\n')
        f.write('    Date TEXT\n')
        f.write(');\n\n')
        id = 0

        for filename in os.listdir(folder_path):
            if filename.endswith('.csv'):
                file_path = os.path.join(folder_path, filename)
                df = pd.read_csv(file_path)
                records = df.to_records(index=False)
                values = ', '.join([f"('{id}', '{rec[0]}', '{rec[1]}', {rec[2]}, '{rec[3]}', {rec[4]}, '{rec[5]}', '{rec[6]}', '{rec[7]}')" for rec in records])
                f.write(f'INSERT INTO transactions VALUES\n{values};\n\n')
                id += 1

def create_sql_from_csvs(folder_path):
    # Create the SQL file
    sql_filename = os.path.join(folder_path, "data.sql")
    with open(sql_filename, "w", encoding="utf-8") as sql_file:
        # Write the SQL statement to create the table
        table_name = "transactions"
        sql_file.write(f"CREATE TABLE {table_name} (\n")
        sql_file.write('    ID INT PRIMARY KEY,\n')  # Define ID as the primary key
        sql_file.write("    Transaction_ID INT NOT NULL,\n")
        sql_file.write("    Name VARCHAR(255) NOT NULL,\n")
        sql_file.write("    Price DECIMAL(10,2) NOT NULL,\n")
        sql_file.write("    Side VARCHAR(10) NOT NULL,\n")
        sql_file.write("    Volume INT NOT NULL,\n")
        sql_file.write("    Order_Executed BOOLEAN NOT NULL,\n")
        sql_file.write("    Target DECIMAL(10,2) NOT NULL,\n")
        sql_file.write("    Date DATE NOT NULL,\n")
        sql_file.write(");\n\n")
        id = 0

        # Write the INSERT statements for each CSV file
        for csv_filename in os.listdir(folder_path):
            if csv_filename.endswith(".csv"):
                csv_filepath = os.path.join(folder_path, csv_filename)
                with open(csv_filepath, "r", encoding="utf-8") as csv_file:
                    csv_reader = csv.reader(csv_file)
                    next(csv_reader)  # Skip the header row
                    for row in csv_reader:
                        transaction_id, name, price, side, volume, order_executed, target, date = row
                        sql_file.write(f"INSERT INTO {table_name} VALUES ({id}, {transaction_id}, '{name}', {price}, '{side}', {volume}, {order_executed}, {target}, '{date}');\n")
                        id += 1

    print(f"SQL file created: {sql_filename}")

def check_sql():
    # Connect to an in-memory SQLite database
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    # Read the SQL statements from the file
    with open('data.sql', 'r') as f:
        sql_statements = f.read()

    # Execute the SQL statements
    cursor.executescript(sql_statements)

    # Query the database for transactions with name '1185321'
    query = "SELECT Name, Date FROM transactions WHERE Name = '1185321';"
    cursor.execute(query)

    # Get the results
    results = cursor.fetchall()

    # Print the results
    for row in results:
        print(f"Name: {row[0]}, Date: {row[1]}")

    # Close the connection
    conn.close()



if __name__ == '__main__':
    folder_path = 'C:\temp'
    get_folder(folder_path)
    convert_folder(folder_path)
    #create_sql_script(folder_path, 'transactions.sql')
    #create_sql_from_csvs(folder_path)
    #check_sql()
    directory_path = download_files_and_create_DataTables()
    combine_DataTables(directory_path)
