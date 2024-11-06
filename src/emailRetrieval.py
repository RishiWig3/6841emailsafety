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





# import email
# import imaplib
# import os

# class FetchEmail():

#     connection = None
#     error = None

#     def __init__(self, mail_server, username, password):
#         self.connection = imaplib.IMAP4_SSL(mail_server)
#         self.connection.login(username, password)
#         self.connection.select(readonly=False) # so we can mark mails as read

#     def close_connection(self):
#         """
#         Close the connection to the IMAP server
#         """
#         self.connection.close()

#     def save_attachment(self, msg, download_folder="/tmp"):
#         """
#         Given a message, save its attachments to the specified
#         download folder (default is /tmp)

#         return: file path to attachment
#         """
#         att_path = "No attachment found."
#         for part in msg.walk():
#             if part.get_content_maintype() == 'multipart':
#                 continue
#             if part.get('Content-Disposition') is None:
#                 continue
# https://stackoverflow.com/questions/6225763/downloading-multiple-attachments-using-imaplib