import vt
import os
import json
from dotenv import load_dotenv


def fetch_report_from_virustotal(client, file_hash):
    # Fetch the report of a file from VirusTotal using its hash
    return client.get_object(f"/files/{file_hash}")


def extract_hashes():
    # Returns the hash of the quarantined file
    return "0cc3bf14ca3acf47396f0cbe6392ffe9d8e6af2fddb48b6f8353dc26118b9a2a"


# def print_attributes(obj, indent=0):
#     prefix = ' ' * indent
#     if isinstance(obj, dict):
#         for key, value in obj.items():
#             print(f"{prefix}{key}:")
#             print_attributes(value, indent + 4)
#     elif isinstance(obj, list):
#         for index, item in enumerate(obj):
#             print(f"{prefix}Item {index}:")
#             print_attributes(item, indent + 4)
#     else:
#         print(f"{prefix}{obj}")

def print_last_analysis_stats(response_dict):
    """Print the last analysis stats from the VirusTotal response."""
    try:
        last_analysis_stats = response_dict['attributes']['last_analysis_stats']
        print("Last Analysis Stats:")
        for key, value in last_analysis_stats.items():
            print(f"{key}: {value}")
    except KeyError as e:
        print(f"Error: Missing key in response - {e}")


def retrieve_api_key():
    # Load the API key from a file
    load_dotenv()
    api_key = os.getenv("VIRUS_TOTAL_API_KEY")
    return api_key


def main():
    api_key = retrieve_api_key()
    
    with vt.Client(api_key) as client:
        hashes = extract_hashes()
        
        try:
            response = fetch_report_from_virustotal(client, hashes).to_dict()
            
            print_last_analysis_stats(response)
        except vt.APIError as e:
            print(f"Error with hash: {e}")
