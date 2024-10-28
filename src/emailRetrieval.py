from imapclient import IMAPClient
import email
import os

def notYet():
    server = IMAPClient('localhost', port=1143, ssl=False)  # Port configured by ProtonMail Bridge
    server.login('mevvieReceiver@proton.me', 'YziUP5FKGf1sryjvTOaDsQ')
    print("Connected to the server")

    server.select_folder('INBOX')
    messages = server.search(['UNSEEN'])

    for uid, message_data in server.fetch(messages, 'RFC822').items():
        email_message = email.message_from_bytes(message_data[b'RFC822'])
        for part in email_message.walk():
            if part.get_content_disposition() == 'attachment':
                filename = part.get_filename().strip()  # Clean the filename
                save_path = os.path.join(os.path.expanduser("~"), "Documents/Misc", filename)  # Correct path
                with open(save_path, 'wb') as f:
                    f.write(part.get_payload(decode=True))

