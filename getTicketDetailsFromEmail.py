import re
import time
email_data = {
    'Sender': 'Manisha.Bhadoria@hsc.com',
    'To': [{'name': 'Satyapal Kumar', 'email': 'Satyapal.Kumar@hsc.com'}],
    'CC': [],
    'BCC': [],
    'Subject': 'FW: IT-189708 is Assigned',
    'Body': '''
        From: IT.Helpdesk@hsc.com <mailto:IT.Helpdesk@hsc.com> <IT.Helpdesk@hsc.com <mailto:IT.Helpdesk@hsc.com>>
        Sent: Monday, October 9, 2023 8:28 AM
        To: Jatin Rana <Jatin.Rana@hsc.com <mailto:Jatin.Rana@hsc.com>>
        Subject: IT-189708 is Assigned

        New Request Assigned

        A New Request is Assigned, and the details are indicated below:

        Requester Name
        MANUJ KUMAR

        Request Number
        IT-189708

        Request Description
        Please provide the access for below path, for all areas as I am the PM for this project: \\\\Hsc.com\\Engg\\Live_Projects_2\\Yatra_Mybooking <file://Hsc.com/Engg/Live_Projects_2/Yatra_Mybooking>

        Category
        Project Area Access

        Priority
        Normal

        This is a system-generated mail; please do not reply back to this mail.

        Regards,
        IT Helpdesk
    ''',
    'Attachments': [],
    'Size': 57787,
    'object': '<win32com.gen_py.Microsoft Outlook 16.0 Object Library._MailItem instance at 0x2138010128080>',
    'ReceivedTime': '2023-10-09T12:02:44.107000+00:00',
    'ReceivedTimestamp': 1696833164.0,
    'SentOn': '2023-10-09T12:02:41+00:00'
}

# Extract Requester Name, Request Number, Request Description, and Category
def getUserDetails(data):
    print("Scaning Email for User Details...");
    time.sleep(2);
    userDetils= {}
    patternForPath =r'file:(.*?)(?=>)';
    matcheForPath = re.search(patternForPath, data, re.DOTALL)
    if matcheForPath:
        project_path=matcheForPath.group(1).strip()
        #userDetils['projectPath'] = project_path

    #print("Project Path:", userDetils['projectPath'])
    pattern = r'Requester Name\s+(.*?)\s+Request Number\s+(.*?)\s+Request Description\s+(.*?)\s+Category\s+(.*?)\s+'
    matches = re.search(pattern, data, re.DOTALL)
   
    if matches:
        requester_name = matches.group(1).strip()
        userDetils['requesterName']=requester_name;
        request_number = matches.group(2).strip()
        userDetils['requestNumber']=request_number;
        request_description = matches.group(3).strip()
        userDetils['requestDescription']=request_description;
        category = matches.group(4).strip();
        userDetils['TicketCategory']=category;
        #path = matches.group(5).strip()

        print("Requester Name:", userDetils['requesterName'])
        time.sleep(2);
        print("Request Number:", userDetils['requestNumber'])
        time.sleep(2);
        print("Request Description:", userDetils['requestDescription'])
        time.sleep(2);
        print("Category:", userDetils['TicketCategory'])
        time.sleep(2);
        #print("Path:", path)
        return userDetils;
    else:
        print("Information not found in the email body.")
        return 0;
 
    

#getUserDetails(email_data);