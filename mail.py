import smtplib, ssl

port = 465   					#For SSL
smtp_server = "smtp.gmail.com"
sender_email = "hkruprela@gmail.com"  		# Enter your address
password = 'ihefomnnemhvlwwp' 			# Enter password
receiver_email = "hirenruprela@gmail.com"  	# Enter receiver address

message = """\
Subject:  Model successfully trained
Congratulations accuracy achieved."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)