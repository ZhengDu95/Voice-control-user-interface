import smtplib
from email.mime.text import MIMEText

import conf


def send_email_func(to_email_id,subject,body):

    # login by provide email account and password
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.set_debuglevel(0)

        try:
            sender_email_id = conf.JSON_DATA['gmail_id']
            pwd = conf.JSON_DATA['gmail_password']
            code, message = server.login(sender_email_id, pwd) # log in to the server
            print(code)
            print(message)

        except Exception as e:
            print("Insert correct Email id or User name", e)


        # Sending email
        msg = MIMEText(body)
        msg['From'] = sender_email_id
        msg['To'] = to_email_id
        msg['Subject'] = subject
        text = msg.as_string()

        server.sendmail(sender_email_id, to_email_id, text)

    except Exception as e:
        raise Exception("Unexpected error. Plz try it again.")

    server.quit()
