import csv
def process_csv(file_path):
    """
    Processes a file containing weather_data.
    Arguments: file_path (str): The path to the file containing the list of URLs.
    Returns: A list of combined URLs.
    """
    with open(file_path) as file:
        lines = csv.reader(file)
        tempertures = []
        for row in lines:
            #print(row) #print all the file
            if row[1] != "temp":
                # List of Tempertures (string)
                # tempertures.append(row[1])
                # List of Tempertures (int)
                tempertures.append(int(row[1]))
        print(tempertures)

if __name__ == "__main__":
    file_path = 'data.csv'  # Path of the file containing the csv file
    process_csv(file_path)