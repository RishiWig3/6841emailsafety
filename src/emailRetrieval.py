import imaplib
import email
from email.header import decode_header
import os

# Account credentials and mail server details


def setup(IMAP_HOST, IMAP_PORT, USERNAME, PASSWORD):
    # Create a directory to save attachments
    if not os.path.exists("src/quarantine"):
        os.makedirs("src/quarantine")

    mail = imaplib.IMAP4(IMAP_HOST, IMAP_PORT)
    mail.starttls()  # Use STARTTLS for security
    mail.login(USERNAME, PASSWORD)
    
    mail.select("inbox")
    return mail

def shutdown(mail):
    mail.close()
    mail.logout()

def get_email_ids(mail):
    status, messages = mail.search(None, "ALL")
    if status != "OK":
        print("No messages found!")
        return

    email_ids = messages[0].split()
    return email_ids

def extract_message(mail, email_id):
    status, msg_data = mail.fetch(email_id, "(RFC822)")
    if status != "OK":
        print("Failed to fetch email with ID" + email_id)
    return msg_data


def download_attachments(mail, email_ids):
    for email_id in email_ids:
        msg_data = extract_message(mail, email_id)

    for response_part in msg_data:
        if isinstance(response_part, tuple): #checks if has (email_info, email_data) format and dilter for the email_data
            msg = email.message_from_bytes(response_part[1])
            
            for part in msg.walk():
                if part.get_content_disposition() == "attachment":
                    filename = part.get_filename()
                    if filename: 
                        filepath = os.path.join("src/quarantine", filename)
                        with open(filepath, "wb") as f:     #writes in the binaries
                            f.write(part.get_payload(decode=True))
                        print("Downloaded: " + filename)



def controller(IMAP_HOST, IMAP_PORT, USERNAME, PASSWORD):
    mail = setup(IMAP_HOST, IMAP_PORT, USERNAME, PASSWORD)
    email_ids = get_email_ids(mail)
    download_attachments(mail, email_ids)
    shutdown(mail)