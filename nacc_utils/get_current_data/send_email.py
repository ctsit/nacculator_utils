import smtplib

import ConfigParser
from email.mime.multipart import MIMEMultipart


def read_config(config_path):
    config = ConfigParser.ConfigParser()
    config.read(config_path)
    return config


def send_email(recipient, subject, message):

    config = read_config("smtp_config_example.ini")
    my_address = config.get('credentials', 'my_address')
    password = config.get('credentials', 'password')

    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.ufl.edu', port=587)
    s.starttls()
    s.login(my_address, password)

    # For each contact, send the email:
    for r_email in recipient:
        msg = MIMEMultipart()       # create a message

        # setup the parameters of the message
        msg['From'] = my_address
        msg['To'] = r_email
        msg['Subject'] = subject

        # add in the message body
        msg.attach(message)

        # send the message via the server set up earlier.
        s.sendmail(my_address, recipient, msg.as_string())
        del msg

    # Terminate the SMTP session and close the connection
    s.quit()


