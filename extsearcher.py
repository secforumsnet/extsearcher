import requests
from bs4 import BeautifulSoup
from colorama import init, Fore
import os

# Initialize colorama for colored text
init(autoreset=True)

# Function to crawl the website and search for files with the given extensions
def crawl_and_search(url, extensions):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all links on the page
            links = soup.find_all('a', href=True)

            # Filter links that end with any of the specified extensions
            matching_links = [link['href'] for link in links if link['href'].endswith(tuple(extensions))]

            # Print the matching links in green
            if matching_links:
                print(Fore.GREEN + f"Files with extensions {', '.join(extensions)} found on {url}:" + Fore.RESET)
                for file_link in matching_links:
                    print(Fore.GREEN + file_link + Fore.RESET)
                print("\n")

            # Find all subdirectories and crawl them recursively
            subdirectories = [link['href'] for link in links if link['href'].endswith('/')]
            for subdir in subdirectories:
                subdir_url = url + subdir
                crawl_and_search(subdir_url, extensions)

    except requests.exceptions.RequestException as e:
        pass  # Suppress request-related errors
    except Exception as e:
        pass  # Suppress other unexpected errors

# Accept user input for the website URL and the file extensions to search for
website_url = input("Enter the website URL: ")
extensions_input = input("Enter the file extensions to search for (comma-separated, e.g., '.pdf, .txt'): ")
extensions = [ext.strip() for ext in extensions_input.split(',')]

# Call the crawl_and_search function with user-provided values
crawl_and_search(website_url, extensions)
