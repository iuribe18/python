import boto3
import csv
import io

def read_csv_from_s3(bucket_name, file_key):
    """
    Read a CSV file from an S3 bucket.
    
    Arguments:
    bucket_name (str): The name of the S3 bucket.
    file_key (str): The key (path) of the file in the S3 bucket.
    
    Returns:
    A list of temperatures from the CSV file.
    """
    s3 = boto3.client('s3')
    response = s3.get_object(Bucket=bucket_name, Key=file_key)
    content = response['Body'].read().decode('utf-8')
    temperatures = []

    # Using io.StringIO to simulate a file object from the string content
    with io.StringIO(content) as file:
        lines = csv.reader(file)
        for row in lines:
            # print(row) # print all the file
            if row[1] != "temp":
                # List of Temperatures (string)
                # temperatures.append(row[1])
                # List of Temperatures (int)
                temperatures.append(int(row[1]))
    return temperatures

if __name__ == "__main__":
    bucket_name = 'ivanuribegonzalez'  # Name of the S3 bucket
    file_key = 'data.csv'  # Key (path) of the file in the S3 bucket

    # Read and process the CSV file from S3
    temperatures = read_csv_from_s3(bucket_name, file_key)
    print(temperatures)