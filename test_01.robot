*** Settings ***
Documentation    This is just for test
Library    RPA.Windows
Library    RPA.Email.ImapSmtp
Library    RPA.Outlook.Application


*** Variables ***
@{windows}
${emails}

*** Tasks ***
Open window application
    Windows Run    explorer
    Control Window    Home
    Maximize Window    Home 
    RPA.Windows.Click    This PC    
    Double Click    Windows (C:)
    Double Click    Users
    RPA.Windows.Right Click    satya 
    RPA.Windows.Click    Properties
    ${windows}=  List Windows
    FOR  ${window}  IN    @{windows}
        Log  Window title:${window}[title]
        Log  Window process name:${window}[name]
        Log  Window process id:${window}[pid]
        Log  Window process handle:${window}[handle]
    END
    Log    ${CURDIR}     
    Close Current Window


*** Tasks ***
Send message
    Open Application    visible:True 
    ${emails}=  Get Emails     account_name=Satyapal.Kumar@hsc.com    folder_name=Inbox    email_filter=[SenderEmailAddress]='HSC.IT@hsc.com'    save_attachments=True    attachment_folder=%{ROBOT_ROOT}${/}attachments    sort=True    sort_key=Received    sort_descending=False 
    Log    ${emails}
    FOR  ${email}  IN  @{emails}
        Mark Email As Read  ${email}
    END
    Move Emails    account_name=Satyapal.Kumar@hsc.com    target_folder=VerifiedTickets    source_folder=Inbox    email_filter=[Subject]='Instant Award - Rashi Kapoor'   