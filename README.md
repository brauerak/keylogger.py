Keylogger Project
--------------------------------------------------

This is a Python-based keylogger project created for educational purposes only. The program listens to keyboard events, logs the pressed keys, and sends the captured data to a specified email address.

Features
 --------------------------------------------
	•	Captures all keystrokes, including special keys (e.g., Enter, Space).
	•	Logs keystrokes into a local text file (keylog.txt).
	•	Sends the log file to an email address after stopping the program. (IN PROGRESS...)
	•	Simple and customizable implementation.
 
How It Works
 --------------------------------------------
	1.	The program starts listening to keyboard events when executed.
	2.	Every key press is logged into the keylog.txt file.
	3.	Pressing the Esc key stops the program, triggers the email functionality, and sends the log file to the specified email.

 Installation
 --------------------------------------------
	1.	Clone the repository:
  		https://github.com/brauerak/keylogger.py.git
    
    	2.	Set up a virtual environment (optional but recommended):
     		* python3 -m venv .venv
		* source .venv/bin/activate  # On Windows: .venv\Scripts\activate

  	3.	Install the required dependencies:
   		pip install pynput

Configuration
--------------------------------------------
	1.	Open the keylogger.py file in a text editor.
	2.	Update the email credentials in the following section with your email address and app-specific password:
			EMAIL_ADDRESS = 'your_email@gmail.com'
			EMAIL_PASSWORD = 'your_app_password'
			EMAIL_RECEIVER = 'receiver_email@gmail.com'

Usage
--------------------------------------------
	1.	Run the script:
 			python3 keylogger.py
    		2.	The program will start listening to keystrokes.
	3.	Press the Esc key to:
	•		Stop the logger.
	•		Automatically send the keylog.txt file to the specified email. (IN PROGRESS...)

 Troubleshooting
 --------------------------------------------
	•	Error: ModuleNotFoundError: No module named 'pynput'
	•	Make sure the pynput library is installed. Run pip install pynput.
	•	Error: 5.7.8 Username and Password not accepted
	•	Ensure you are using an App Password for Gmail.
	•	Log file not sent after pressing Esc
	•	Verify the internet connection and email configuration.

 Disclaimer
 --------------------------------------------
This program is strictly for educational purposes. Unauthorized use of this software may violate privacy laws and ethical guidelines. Ensure you have explicit permission before using it in any environment.



 
