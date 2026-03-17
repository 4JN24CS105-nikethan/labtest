import streamlit as st
import smtplib
from email.message import EmailMessage
from datetime import datetime
from dateutil.relativedelta import relativedelta

# --- SETUP ---
# For Gmail, you'd use an "App Password," not your regular password.
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
SENDER_EMAIL = "your-email@gmail.com" 
SENDER_PASSWORD = "your-app-password" 

def send_reminder_email(target_email, reminder_date):
    msg = EmailMessage()
    msg.set_content(f"This is your monthly reminder for the date: {reminder_date}")
    msg["Subject"] = "📅 Monthly Reminder"
    msg["From"] = SENDER_EMAIL
    msg["To"] = target_email

    try:
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as smtp:
            smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
            smtp.send_message(msg)
        return True
    except Exception as e:
        return e

# --- UI ---
st.title("🚀 Automated Reminder App")

user_email = st.text_input("Enter your email for reminders:")
start_date = st.date_input("Start Date:", datetime.now())

if st.button("Schedule and Send Initial Test"):
    if user_email:
        # Generate the first reminder date
        first_reminder = start_date + relativedelta(months=1)
        
        # Send a test/confirmation email
        result = send_reminder_email(user_email, first_reminder.strftime('%B %d, %Y'))
        
        if result is True:
            st.success(f"Success! A test reminder for {first_reminder.strftime('%B %d')} was sent to {user_email}.")
        else:
            st.error(f"Error: {result}")
    else:
        st.warning("Please enter a valid email address.")
