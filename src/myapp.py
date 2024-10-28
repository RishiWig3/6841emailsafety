import emailRetrieval
import threatAnalysis


# url = "https://www.virustotal.com/api/v3/files/id/behaviour_summary"

# headers = {"accept": "application/json"}

# response = requests.get(url, headers=headers)

# print(response.text)



def main():
    # email listener
    # email listener identifies when file is downloaded
    # email attachment is downloaded and saved in a particular folder
    # threat analysis finds a file
    # threat analysis generates a hash
    # threat analysis requests for a report
    # threat analyis detects file danger of a certain amount, provide report + warning
    threatAnalysis.main()
    


if __name__ == "__main__":
    main()