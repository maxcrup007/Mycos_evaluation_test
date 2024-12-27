import imaplib
import email
from email.header import decode_header
import re

# Your email credentials
IMAP_SERVER = "imap.gmail.com" 
EMAIL = "bt.raoaengna04@gmail.com"
PASSWORD = "ektzcmahvjnrlcjw"

def connect_to_email():

    mail = imaplib.IMAP4_SSL("imap.gmail.com", 993)
    mail.login(EMAIL, PASSWORD)


def search_emails(mail, header_field):
    # mail.select("inbox")
    status = mail.search(None, f'{header_field}')
    messages = mail.search(None, f'{header_field}')
    if status != "OK":
        print("No messages found!")
        return []
    return messages[0].split()

# Fetch email content
def fetch_email(mail, email_id):
    status, msg_data = mail.fetch(email_id, "(RFC822)")
    if status != "OK":
        print(f"Failed to fetch email with ID {email_id}")
        return None

    for response_part in msg_data:
        if isinstance(response_part, tuple):
            msg = email.message_from_bytes(response_part[1])
            return msg
    return None

# Extract links from email body
def extract_links_from_email(msg):
    links = []
    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            if content_type == "text/html":  # Look for HTML content
                body = part.get_payload(decode=True).decode()
                # Extract all links using regex
                links.extend(re.findall(r'href="(http[s]?://.*?)"', body))
    else:
        # Non-multipart emails
        body = msg.get_payload(decode=True).decode()
        links.extend(re.findall(r'href="(http[s]?://.*?)"', body))
    return links

# Main script
def main():
    mail = connect_to_email()

    # Search for emails with a specific subject
    header_field = "Mycos Evaluation on 12-2024"
    email_ids = search_emails(mail, header_field)

    for email_id in email_ids:
        msg = fetch_email(mail, email_id)
        if msg:
            # Decode and print subject
            subject = decode_header(msg["Subject"])[0][0]
            if isinstance(subject, bytes):
                subject = subject.decode()
            print(f"Email Subject: {subject}")

            # Extract and print links
            links = extract_links_from_email(msg)
            if links:
                print("Links found in email:")
                for link in links:
                    print(link)
            else:
                print("No links found in email.")

    # Logout from the email server
    mail.logout()

if __name__ == "__main__":
    main()