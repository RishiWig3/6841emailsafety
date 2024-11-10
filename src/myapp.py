import emailRetrieval
import threatAnalysis
import emailListener
import os
from dotenv import load_dotenv
import time

all_uids = []

def retrieve_mail_server():
    load_dotenv()
    mail_server = os.getenv("MAIL_SERVER")
    return str(mail_server)

def retrieve_mail_port():
    load_dotenv()
    mail_port = os.getenv("MAIL_PORT")
    return int(mail_port)

def retrieve_mail_username():
    load_dotenv()
    mail_username = os.getenv("MAIL_USERNAME")
    return mail_username

def retrieve_mail_password():
    load_dotenv()
    mail_password = os.getenv("MAIL_PASSWORD")
    return mail_password

def delete_quarantine():
    try:
        files = os.listdir('src/quarantine')
        for file in files:
            file_path = os.path.join('src/quarantine', file)
            if os.path.isfile(file_path):
                os.remove(file_path)
        os.rmdir('src/quarantine')
        print("All files deleted successfully.")
    except OSError:
     print("Error occurred while deleting files.")


IMAP_HOST = retrieve_mail_server()
IMAP_PORT = retrieve_mail_port()
USERNAME = retrieve_mail_username()
PASSWORD = retrieve_mail_password()


def main():
    while (emailListener.checker(IMAP_HOST, IMAP_PORT, USERNAME, PASSWORD) != True):
        time.sleep(60)
        continue
    emailRetrieval.controller(IMAP_HOST, IMAP_PORT, USERNAME, PASSWORD)

    threatAnalysis.controller()

    delete_quarantine()

    time.sleep(60)

    main()

    


if __name__ == "__main__":
    main()