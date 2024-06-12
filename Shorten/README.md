# URL Shortener Project

## Description
This project takes a list of URLs, removes duplicates and shortens the URLs using the is.gd API. The results are printed to the console.

## Requirements
- Docker
- Python 3.9 (If you want to run the script without Docker)

## Setting
### Using Docker
1. Make sure you have Docker installed on your system.
2. Build the Docker image:
    ```sh
    docker build -t url-shortener .
3. Run the Docker container:
    ```sh
    docker run --rm url-shortener

### Without Docker
1. Run the Python script:
    ```sh
    python main.py