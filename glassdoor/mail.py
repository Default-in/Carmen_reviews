import imghdr
import smtplib
from email.message import EmailMessage


def shoot_mail(subject, body):
    msg = EmailMessage()
    msg['Subject'] = f'{subject}'
    msg['From'] = "sahilkanger27@gmail.com"
    msg['To'] = "sahil@getdefault.in"
    msg.set_content(f'{body}')
    with open("image.png", 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name

        msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    s.login("sahilkanger27@gmail.com", "Sahil@321")
    s.send_message(msg)
    # terminating the session
    s.quit()
    print("Success")