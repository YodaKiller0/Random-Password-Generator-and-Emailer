# Random-Password-Generator-and-Emailer

The goal of this project would be to create a Python script that generates a random password and sends it to your email address. The script could work as follows:

1. Generate a random password using Python's built-in random module.
2. Use an external library like PyEmail to send an email to your desired email address.
3. In the email body, include the generated password along with any other relevant information you'd like to include (e.g. a message indicating that this is a password reset or a new account creation).
4. Use the command line or a GUI interface to prompt the user to enter their email address and any other necessary information (e.g. email server credentials).
5. Once the user has provided all necessary information, run the script to generate the password and send the email.

This project could be a fun way to practice working with external libraries, as well as creating a command line or GUI interface for user input. Additionally, it could be a useful tool for generating secure, randomized passwords on the fly.

# Edit the Code first
1. Open the passwordtoemail.py file using VSCode or any other preferred editor.
2. Then edit these lines <br>
```python
# 1st line
sender_email = 'Enter your email'
```
Example ⬇️
```python
sender_email = 'example@gmail.com'
```
<hr>

# How to get the App password?

To generate an app password in Gmail, you can follow these steps:

1. Sign in to your Gmail account on your computer.
2. Click on your profile picture or initial in the top right corner and select "Google Account".
3. Click on the "Security" tab in the left sidebar.
4. Under "Signing in to Google," click on "App passwords." You may need to verify your identity by entering your password again.
5. Select the app and device you want to generate an app password for.
6. Click on "Generate" and follow the instructions to create a new app password.
7. Once you have generated the app password, make sure to copy it or save it somewhere secure, as you may not be able to view it again.

Note that you may need to enable two-factor authentication for your Gmail account before you can generate an app password. If you have not already done so, you can do this by going to the "Security" tab in your Google Account settings and clicking on "2-Step Verification."

* Now edit these lines

```python
# 2st line
sender_password = 'Enter your app password'
```
Example ⬇️
```python
sender_password = 'v7xhwiasyem6lgynx'
```

<hr>

```python
# 3rd line
receiver_email = 'example@gmail.com'
```
Example ⬇️
```python
receiver_email = 'example@gmail.com'
```
<hr>

# Extra steps are required if you would like to customize your password further (this is optional).

```python
# Generate a random password with a length of 16 characters
# To change the password length, simply change the value of 16 to your preferred length.
password = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#0123456789') for i in range(16))
```

<br>

```python
# Represents the time interval, in seconds, after which a new random password is generated.
# Change it if you like to
time.sleep(10)
```

<hr>

# To generate those random passwords and send it your email follow these steps:<br>

1. Open the python code with your favourite text editor or integrated development environment (IDE).
2.Then run the python code
