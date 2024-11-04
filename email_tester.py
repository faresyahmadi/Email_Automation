import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

file_path = r"C:\Users\xxxxxxxx\OneDrive\Desktop\students_websitescopy.csv"
  
data = pd.read_csv(file_path)


smtp_server = 'smtp.gmail.com'  
smtp_port = 587  
smtp_user = 'xxxxxxxx' 
smtp_password = 'xxxxxxxx' 


subject = "Your Website Looks Great!"
body_template = """
Hi {name},

I was browsing through your website, {website}, and it looks amazing! I was wondering if you would like to continue working on it and make it even better.

Let me know if you are interested!

Best regards,
[Your Name]
"""


with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_user, smtp_password)
    
    for index, row in data.iterrows():
        name = row['OwnerName']
        email = row['Email']
        website = row['Website']
        
       
        msg = MIMEMultipart()
        msg['From'] = smtp_user
        msg['To'] = 'yahmadifares2001@gmail.com'  
        msg['Subject'] = subject
        body = body_template.format(name=name, website=website)
        msg.attach(MIMEText(body, 'plain'))
        
        # Print the email content instead of sending it (for testing purposes)
        print(f"Test Email to {name} ({email}):\n{body}\n")

