import pickle
import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from sklearn.preprocessing import StandardScaler

# Load the trained model
with open("xgb_churn_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Load new customer data (Assuming you have a CSV file with new customer records)
df = pd.read_csv("customers-clean.csv")  # Replace with your actual dataset
df = df.drop(columns=['Exited'])

# Predict churn probability
churn_predictions = model.predict_proba(df)[:,1]


# # Filter emails of customers predicted to churn
# churn_risk_customers = df[churn_predictions == 1]  # Select customers predicted to churn
# emails_to_notify = churn_risk_customers['Email'].tolist()

# # Email configuration
# SMTP_SERVER = "smtp.gmail.com"  # Change based on your email provider
# SMTP_PORT = 587
# SENDER_EMAIL = "your_email@gmail.com"  # Your email
# SENDER_PASSWORD = "your_email_password"  # Use app password if using Gmail

# # Email content
# subject = "Important: We Value Your Membership!"
# body = """
# Dear Valued Customer,

# We noticed you haven’t been as active with us recently. We’d love to understand how we can serve you better.

# If there’s anything we can do to improve your experience, please let us know.

# Best regards,  
# [Your Company Name]
# """

# # Send emails
# def send_email(receiver_email):
#     try:
#         msg = MIMEMultipart()
#         msg["From"] = SENDER_EMAIL
#         msg["To"] = receiver_email
#         msg["Subject"] = subject
#         msg.attach(MIMEText(body, "plain"))

#         server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
#         server.starttls()
#         server.login(SENDER_EMAIL, SENDER_PASSWORD)
#         server.sendmail(SENDER_EMAIL, receiver_email, msg.as_string())
#         server.quit()
#         print(f"Email sent to {receiver_email}")

#     except Exception as e:
#         print(f"Failed to send email to {receiver_email}: {e}")

# # Loop through all churn-risk customers and send emails
# for email in emails_to_notify:
#     send_email(email)

# print("All emails sent successfully!")
