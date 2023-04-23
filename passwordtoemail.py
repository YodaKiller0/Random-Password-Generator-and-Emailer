import random
import time
import smtplib

# Email and password information
sender_email = 'Enter your email'
sender_password = 'Enter your app password'
receiver_email = 'Enter your email again'

while True:
    password = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#0123456789') for i in range(10))
    #(16) mean the password length. Change that to your preference
    
    # Print the current password
    print('Current Password:', password)
    
    # Send the password to your email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, 'Subject: Your New Password\n\n' + password)
    server.quit()
    
    # Wait for 10 seconds
    time.sleep(10)
