import os
from imbox import Imbox # pip install imbox
import traceback

host = "imap.proton.com"
username = "mevvieReceiver@proton.me"
password = 'yH,,sN^SF2c@8K2'
port = 993
# download_folder = "/path/to/download/folder"

# if not os.path.isdir(download_folder):
#     os.makedirs(download_folder, exist_ok=True)
    
mail = Imbox(host, username=username, password=password, ssl=True, ssl_context=None, starttls=False, port=port)
messages = mail.messages() # defaults to inbox

for (uid, message) in messages:
    mail.mark_seen(uid) # optional, mark message as read

    # for idx, attachment in enumerate(message.attachments):
    #     try:
    #         att_fn = attachment.get('filename')
    #         download_path = f"{download_folder}/{att_fn}"
    #         print(download_path)
    #         with open(download_path, "wb") as fp:
    #             fp.write(attachment.get('content').read())
    #     except:
    #         print(traceback.print_exc())

mail.logout()