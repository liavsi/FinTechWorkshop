import MBO_Parser as mbp
import os
import gzip
import pandas as pd
import boto3


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


def get_folder():
    folder_path = input("Enter the folder path: ")

    # Get a list of all files in the folder
    file_list = os.listdir(folder_path)

    for file_name in file_list:
        if file_name.endswith(".rmbo"):
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
    return extracted_file_path


if __name__ == '__main__':
    get_folder()
    #directory_path = download_files_and_create_DataTables()
    #combine_DataTables(directory_path)
