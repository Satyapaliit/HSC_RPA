*** Settings ***
Documentation    This is just for test
Library        RPA.Windows
Library    RPA.Desktop
Library    RPA.Robocorp.WorkItems
Library    OperatingSystem
Library    

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
      
    Close Current Window