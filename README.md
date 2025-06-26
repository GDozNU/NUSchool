# NUSchool
For school

# AutoPatching - Windows Security Patch Script
# Overview
AutoPatching is a Python script that helps keep Windows systems secure by automatically checking for missing security updates, installing them if needed, logging the patch activity, and sending an email notification to the system administrator.
# Features
- Checks for available Windows security updates
- Installs updates automatically
- Logs update activity in a text file
- Sends email notifications with update results
# Requirements
- Windows 10/11 or Windows Server
- Python 3.8 or higher
- PowerShell module: PSWindowsUpdate
- Gmail account with App Password enabled
- Visual Studio Code (run as admin or it doesnt work)
# Setup Instructions
1. Install the PowerShell module (open PowerShell as Admin on LOCAL machine):
2. Clone or download the script into a folder.
3. In VS Code:
- Open the folder
- Create and activate a virtual environment:

  python -m venv venv
  .\venv\Scripts\activate

# How to Run
1. Open VS Code as Administrator
2. Run the script:
# Output
- `patch_log.txt`: This file is created in the same folder and stores log messages with timestamps.
- Email: An update summary is sent to the configured admin email address.
# Testing
- If the system is fully updated, it logs and emails "no updates."
- If updates are available, it installs them, logs the actions, and emails the update list.
- If there is an error, it logs the failure and emails an error message if possible.
