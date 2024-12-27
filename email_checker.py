from imap_tools import MailBox, AND
from email.header import decode_header
import re

# Your email credentials
IMAP_SERVER = "imap.gmail.com" 
EMAIL = "bt.raoaengna03@gmail.com"
PASSWORD = "rtqjgwallgtphkpu"


def extract_links_from_html(html):
    # Regex to find all href links
    links = re.findall(r'href="(http[s]?://.*?)"', html)
    return links
        
with MailBox("imap.gmail.com" ).login(EMAIL, PASSWORD, "Inbox") as mb:

    emails = mb.fetch(AND(subject="Mycos Evaluation"))

    for email in emails:
        print(f"From: {email.from_}")
        print(f"Subject: {email.subject}")
        print(f"Date: {email.date}")
        print(f"Body: {email.text}")

        links = extract_links_from_html(email.html)
        print("Links Found:")
        for link in links:
            with open("Collect_Text/link.text", "w") as file:
                file.write(link)
                print(link)