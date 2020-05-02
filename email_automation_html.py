import os
import smtplib
from data_analysis import max_expense
import imghdr
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText  # Added
from email.mime.image import MIMEImage
import datetime
from datetime import timedelta

EMAIL_ADDRESS = os.environ.get('EMAIL')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
app_password = os.environ.get('APP_PASSWORD')

today = datetime.date.today()
first = today.replace(day=1)
end_date = first - datetime.timedelta(days=1)
start = end_date.replace(day=1)
start = start.isoformat()
end = end_date.isoformat()

new_dir ='/Users/marvinchan/Documents/PythonProgramming/DatabaseforStatements/BudgetingProject/' + end + '/'

# Create the root message and fill in the from, to, and subject headers
msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = 'Monthly Budget Analysis'
msgRoot['From'] = EMAIL_ADDRESS
msgRoot['To'] = EMAIL_ADDRESS
msgRoot.preamble = 'This is a multi-part message in MIME format.'

# Encapsulate the plain and HTML versions of the message body in an
# 'alternative' part, so message agents can decide which they want to display.
msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

msgText = MIMEText('This is the alternative plain text message.')
msgAlternative.attach(msgText)

html = ("""<!DOCTYPE html>
	<html>
		<body>

			<center>
			<h2>Hi Marvin! </h2>
			<h3>Here is your monthly budget analysis!</h3> 
	
				<br><img src="cid:image2" max-width="800" height="500" ><br> 
			
			<b><p2>Your highest expense from the month was: %s</p2></b> 

			<br><p3>Below are your expenses by month: </p3> <br>
			
				<br><img src="cid:image1" width="800" height="500"><br> 
			
			<p4>Lastly this is your Expense to Income Ratio:</p4>
			
				<br><img src="cid:image3" width="550" height="400"><br>  
			</center>

		</body>	
	</html>""" )

# We reference the image in the IMG SRC attribute by the ID we give it below
msgText = MIMEText(html %(max_expense), 'html')
msgAlternative.attach(msgText)

# This example assumes the image is in the current directory
monthly = open(new_dir + 'monthly.png', 'rb')
msgImage = MIMEImage(monthly.read())
monthly.close()

msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)

# This example assumes the image is in the current directory
category = open(new_dir + 'category.png', 'rb')
msgImage = MIMEImage(category.read())
category.close()

# Define the image's ID as referenced above
msgImage.add_header('Content-ID', '<image2>')
msgRoot.attach(msgImage)

in_out = open(new_dir + 'in_out.png', 'rb')
msgImage = MIMEImage(in_out.read())
in_out.close()

msgImage.add_header('Content-ID', '<image3>')
msgRoot.attach(msgImage)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
# with smtplib.SMTP('localhost', 1025) as smtp:
	smtp.login(EMAIL_ADDRESS, app_password)
	smtp.send_message(msgRoot)
		



	