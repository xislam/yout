# import os
# import smtplib
#
# EMAIL_ADDRESS = os.environ.get('EMAILL_USER')
# EMAIL_PASSWORD = os.environ.get('EMAILL_PASS')
#
# with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.ehlo()
#
#     smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
#
#     subject = 'Grad dinner this weekend?'
#     body = 'How adou dinner at 6pm this Saturday?'
#
#     msg = f'Subject: {subject}\n\n{body}'
#
#     smtp.sendmail(EMAIL_ADDRESS, 'testovichi07@gmail.com', msg)
import smtplib

gmail_user = "testovichi07@gmail.com"
password = "Z"
TO = 'orunbaev.io@gmail.com'
SUBJECT = "Testing sending using gmail"
TEXT = "Hi"
server = smtplib.SMTP('smtp.gmail.com', 587)
server = smtplib.SMTP_SSL('smtp.googlemail.com', 465)
server.login(gmail_user, password)

BODY = '\r\n'.join(['To: %s' % TO,
        'From: %s' % gmail_user,
        'Subject: %s' % SUBJECT,
        '', TEXT])
server.sendmail(gmail_user, TO, BODY)
print ('email sent')