import imaplib
import myapp


def checker(IMAP_HOST, IMAP_PORT, USERNAME, PASSWORD):
    mail = imaplib.IMAP4(IMAP_HOST, IMAP_PORT)
    mail.starttls()
    mail.login(USERNAME, PASSWORD)
    mail.list()

    latest_email_uid = None

    mail.select("Inbox", readonly=True)
    result, data = mail.uid('search', None, "ALL")
    myapp.all_uids = data[0].split()  # List of email UIDs

    if myapp.all_uids:
        current_email_uid = myapp.all_uids[-1]  # Get the most recent UID

        if latest_email_uid != current_email_uid:
            print("New mail!")
            result, data = mail.uid('fetch', current_email_uid, '(RFC822)')     # New email found
            latest_email_uid = current_email_uid  # Update to the latest UID
            return True
        else:
            return False


