import boto3
import csv
import os

def download_file_from_s3(bucket_name, file_key, download_path):
    """
    Download a file from an S3 bucket.
    
    Arguments:
    bucket_name (str): The name of the S3 bucket.
    file_key (str): The key (path) of the file in the S3 bucket.
    download_path (str): The local path to download the file to.
    """
    s3 = boto3.client('s3')
    s3.download_file(bucket_name, file_key, download_path)

def process_csv(file_path):
    """
    Processes a file containing weather data.

    Arguments:
    file_path (str): The path to the file containing the list of URLs.

    Returns:
    A list of combined URLs.
    """
    with open(file_path) as file:
        lines = csv.reader(file)
        temperatures = []
        for row in lines:
            # print(row) # print all the file
            if row[1] != "temp":
                # List of Temperatures (string)
                # temperatures.append(row[1])
                # List of Temperatures (int)
                temperatures.append(int(row[1]))
        print(temperatures)

if __name__ == "__main__":
    bucket_name = 'ivanuribegonzalez'  # Name of the S3 bucket
    file_key = 'data.csv'    # Key (path) of the file in the S3 bucket
    download_path = r'C:\Users\Ivancho\Documents\python\projects\weather\data.csv'

    #download_path = 'C:\Users\Ivancho\Documents\python\projects\data.csv'  # Local path to download the file to
    
    # Download the file from S3
    download_file_from_s3(bucket_name, file_key, download_path)
    
    # Process the downloaded file
    process_csv(download_path)