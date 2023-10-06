from imapclient import IMAPClient

class EmailLibrary:
    def __init__(self, host, username, password):
        self.host = imap.gmail.com
        self.username = anilgupta761622@gmail.com
        self.password = 8287647616
        self.client = IMAPClient(self.host)
        self.client.login(self.username, self.password)
        self.client.select_folder("INBOX")

    def search_emails(self, search_criteria):
        return self.client.search(search_criteria)

    def fetch_email(self, email_id):
        return self.client.fetch(email_id, ["ENVELOPE", "BODY[TEXT]"])

    def close_connection(self):
        self.client.logout()
