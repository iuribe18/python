import requests

def shorten_url(url):
    """
    Shortens a given URL using the is.gd API.
    Args: url (str): The URL to be shortened.
    Returns: url (str): The shortened URL.
    Raises: requests.RequestException: If there is an issue with the HTTP request.
    """
    api_url = "https://is.gd/create.php"
    parameters = {'format': 'simple', 'url': url}
    response = requests.get(api_url, params=parameters)
    return response.text

def process_urls(file_path):
    """
    Processes a file containing URLs, combines lines into URLs, and returns a list of URLs.
    Arguments: file_path (str): The path to the file containing the list of URLs.
    Returns: A list of combined URLs.
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Combine lines into URLs
    urls = []
    current_url = ""
    for line in lines:
        # Remove all whitespace characters from the start and end of the string
        stripped_line = line.strip()
        if stripped_line != "":
            if current_url:
                current_url += stripped_line
            else:
                current_url = stripped_line
        else:
            if current_url:
                urls.append(current_url)
                current_url = ""
    if current_url:  # Add the last URL if there is one
        urls.append(current_url)
    return urls

def remove_duplicates(urls):
    """
    Removes duplicates from a list of URLs, shortens each unique URL, and prints the results.
    Arguments: file_path (str): The path to the file to remove duplicates from.
    Returns: None
    """
    unique_urls = list(set(urls))
    shortened_urls = [(shorten_url(url), url) for url in unique_urls]

    # Print the shortened URLs
    for short_url, original_url in shortened_urls:
        print(f"{short_url}, {original_url}")

if __name__ == "__main__":
    file_path = 'urls.txt'  # Path of the file containing the list of URLs
    urls = process_urls(file_path)
    remove_duplicates(urls)