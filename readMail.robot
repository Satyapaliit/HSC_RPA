*** Settings ***
Library    ImapLibrary2

*** Test Cases ***
Email Verification
    Open Mailbox    host=imap.domain.com    user=email@domain.com    password=secret
    ${LATEST} =    Wait For Email    sender=noreply@domain.com    timeout=300
    ${HTML} =    Open Link From Email    ${LATEST}
    Should Contain    ${HTML}    Your email address has been updated
    Close Mailbox

Multipart Email Verification
    Open Mailbox    host=imap.domain.com    user=email@domain.com    password=secret
    ${LATEST} =    Wait For Email    sender=noreply@domain.com    timeout=300
    ${parts} =    Walk Multipart Email    ${LATEST}
    :FOR    ${i}    IN RANGE    ${parts}
    \\    Walk Multipart Email    ${LATEST}
    \\    ${content-type} =    Get Multipart Content Type
    \\    Continue For Loop If    '${content-type}' != 'text/html'
    \\    ${payload} =    Get Multipart Payload    decode=True
    \\    Should Contain    ${payload}    your email
    \\    ${HTML} =    Open Link From Email    ${LATEST}
    \\    Should Contain    ${HTML}    Your email
    Close Mailbox