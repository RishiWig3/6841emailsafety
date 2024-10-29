import vt
import os
import hashlib
from dotenv import load_dotenv


def fetch_report_from_virustotal(client, file_hash):
    # Fetch the report of a file from VirusTotal using its hash
    return client.get_object(f"/files/{file_hash}")


def getFileNameFromQuarantine():
    for filename in os.listdir("src/quarantine"):
        file = os.path.join("src/quarantine", filename)
        if os.path.isfile(file):
            return file;
    return "Error"


def extract_hashes():
    # Returns the hash of the quarantined file
    file = getFileNameFromQuarantine()
    with open(file, "rb") as quarantinedFile:
        bytes = quarantinedFile.read()
        return hashlib.sha256(bytes).hexdigest();


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
