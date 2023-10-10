import win32com.client
import re
import time
from robot.api import TestSuite
from robot import run
from getTicketDetailsFromEmail import getUserDetails

# Define the target subject
#r'\b(important|urgent)\b'
#target_subject = r'\b(IT|assigned)\b'  #"IT-189708 is Assigned"  # Replace with the subject you want to filter
#print("Looking for email with subject:",target_subject);

def watch_for_new_mails():
    print("\n******************************************************************************************************");
    print("Watching Inbox for New Mails...");

    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    inbox = outlook.GetDefaultFolder(6)  # 6 corresponds to the inbox folder
    #messages = inbox.Items
    #message = messages.GetLast()

    subject_pattern = r'(?i)(?=.*\bIT\b)(?=.*\bassigned\b)'

    while True:
        messages = inbox.Items
        for msg in messages:
            if(re.search(subject_pattern, msg.Subject) and msg.UnRead):
                print("Matching email received:")
                time.sleep(2);
                print("Subject:", msg.Subject)
                time.sleep(2);
                #print("Unread?:", msg.UnRead)
                print("Sender:", msg.SenderName)
                time.sleep(2);
                
                # Read the email body
                body = msg.Body
                #print("Email Body:")
                #print(body)
                
                result=getUserDetails(body);
                print("Extracted User Details:",result);



                # Actual Test flow goes here

                # Create a TestSuite instance and add the test suite file
                #suite = TestSuite('D:\HSC_RPA_POC\openFileExplorer.robot')

                if __name__ == '__main__':
                    result = run('D:\HSC_RPA_POC\openFileExplorer.robot')
                    print("Result:",result);
                

                # Mark all processed emails as read
                msg.UnRead = False;
                print("******************************************************************************************************");
        
                
        time.sleep(30)  # Check for new emails every 60 seconds
watch_for_new_mails();