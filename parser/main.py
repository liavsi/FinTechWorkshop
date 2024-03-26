import MBO_Parser as mbp
import os
import gzip
import pandas as pd
import boto3
import logging
import logging.config
import yaml

def setup_logging(default_path='FinTechWorkshop\logs\logging_config.yaml',
                    default_level=logging.INFO):
    """Setup logging configuration"""
    if os.path.exists(default_path):
        with open(default_path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

def combine_DataTables(path):
    logging.info(f'Combining data tables from {path}')
    # Get a list of all CSV files in the folder
    csv_files = [f for f in os.listdir(path)]

    # Initialize an empty DataFrame to store the combined data
    combined_data = pd.DataFrame()

    # Loop through each CSV file
    for f in csv_files:
        # Read the CSV file into a DataFrame
        file_path = os.path.join(path, f)
        data = pd.read_csv(file_path)
        logging.info(f'Loaded data from {file_path}')

        # Append the data to the combined_data DataFrame
        combined_data = pd.concat([combined_data, data], ignore_index=True)

    output_dir_path = 'C:\\temp\\output'
    output_file_path = output_dir_path + '\\' + 'DataTable.csv'

    # Write the combined data to a new CSV file
    combined_data.to_csv(output_file_path, index=False)
    logger.info(f'Combined data written to {output_file_path}')

def download_files_and_create_DataTables():
    logger.info('Downloading files and creating data tables')


    
    local_directory_path = 'FinTechWorkshop\files'
    output_directory_path = local_directory_path + '\\' + 'Data Tables'
    logger.info()
    # Check if the folder exists
    if not os.path.exists(output_directory_path):
        # Create the folder
        os.makedirs(output_directory_path)
        logger.info(f'Created output directory: {output_directory_path}')

    # Iterating over the list of object in the storage
    for obj in response['Contents']:
        # Skip if the object is a folder
        if obj['Key'].endswith('/'):
            continue

        # Construct the local file path
        local_file_path = local_directory_path + '\\' + obj['Key'].split('/')[-1]

        # Download the file
        s3.download_file(bucket_name, obj['Key'], local_file_path)
        logging.info(f'Downloaded file: {local_file_path}')

        extracted_file_path = decompress_GZ_file(local_file_path)

        create_DataTable(extracted_file_path, output_directory_path)

    return output_directory_path

def create_DataTable(extracted_file_path, output_directory_path):
    logging.info(f'Creating data table from {extracted_file_path}')
    # parse the necessary data from the MBO file into DataTable
    with open(extracted_file_path, 'rb') as MBO_File:
        file_name = os.path.splitext(os.path.basename(extracted_file_path))[0]
        csv_file_path = os.path.join(output_directory_path, "DataTable_" + file_name.split("_")[3] + ".csv")
        currentFile = mbp.MBO_Parser(MBO_File)
        pd.DataFrame(currentFile.parseFile()).to_csv(csv_file_path, index=False)
        logging.info(f'Data table written to {csv_file_path}')
    # Remove the MBO file after extraction
    os.remove(extracted_file_path)
    logging.info(f'Removed {extracted_file_path}')

def get_folder():
    folder_path = input("Enter the folder path: ")
    logging.info(f'Processing folder: {folder_path}')

    # Get a list of all files in the folder
    file_list = os.listdir(folder_path)

    for file_name in file_list:
        if file_name.endswith(".rmbo.gz"):
            local_file_path = os.path.join(folder_path, file_name)
            logging.info(f'Decompressing file: {local_file_path}')
            decompress_GZ_file(local_file_path)

def decompress_GZ_file(local_file_path):
    logging.info(f'Decompressing file: {local_file_path}')
    # Specify the path to save the extracted file
    extracted_file_path = os.path.splitext(local_file_path)[0]

    # Open the input GZIP file in binary read mode
    with gzip.open(local_file_path, 'rb') as gz_file:
        # Read the compressed contents
        decompressed_data = gz_file.read()

    # Write the decompressed data to the output file
    with open(extracted_file_path, 'wb') as file:
        file.write(decompressed_data)

    # Remove the GZ file after extraction - NOT NEEDED YET
    # os.remove(local_file_path)
    # logging.info(f'Removed {local_file_path}')
    return extracted_file_path

try:
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info('Logger initialized')
except Exception as e:
    print(f"Error setting up logging: {e}")

if __name__ == '__main__':
    logger.info('Starting the application')
    get_folder()
    directory_path = download_files_and_create_DataTables()
    combine_DataTables(directory_path)