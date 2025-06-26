import subprocess
import logging
from datetime import datetime
import smtplib
from email.message import EmailMessage

# Setup logging to a file that is created in the same directory as the script
logging.basicConfig(
    filename='patch_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Check for the Windows Updates
def check_updates():
    try:
        result = subprocess.check_output([
            'powershell',
            '-Command',
            'Get-WindowsUpdate -MicrosoftUpdate -AcceptAll -IgnoreReboot'
        ], stderr=subprocess.STDOUT, text=True)
        logging.info("Checked for updates.")
        return result
    except subprocess.CalledProcessError as e:
        logging.error(f"Update check failed: {e.output}")
        return f"Error checking updates: {e.output}"

# Install the Windows Updates
def install_updates():
    try:
        result = subprocess.check_output([
            'powershell',
            '-Command',
            'Install-WindowsUpdate -MicrosoftUpdate -AcceptAll -IgnoreReboot -AutoReboot'
        ], stderr=subprocess.STDOUT, text=True)
        logging.info("Installed updates.")
        return result
    except subprocess.CalledProcessError as e:
        logging.error(f"Installation failed: {e.output}")
        return f"Error installing updates: {e.output}"

# Send email notification if able to
def send_email(subject, body, to_email):
    from email.message import EmailMessage
    import smtplib
    import logging

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = 'gregoryjr32@gmail.com'
    msg['To'] = to_email
    msg.set_content(body)

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login('gregoryjr32@gmail.com', 'jrfeyaacjmoldueq')  # Gmail app password
            smtp.send_message(msg)
        logging.info(f"Notification sent to {to_email}")
    except Exception as e:
        logging.error(f"Failed to send email: {str(e)}")

# Main Code
def autopatch():
    logging.info("==== AutoPatching Started ====")
    updates = check_updates()
    print(updates)

    if "No updates" not in updates:
        result = install_updates()
        print(result)
        send_email("AutoPatch: Updates Installed", result, "gregoryjr32@gmail.com")
    else:
        send_email("AutoPatch: No Updates", "System is up to date.", "gregoryjr32@gmail.com")

    logging.info("==== AutoPatching Complete ====")

if __name__ == "__main__":
    autopatch()
  
