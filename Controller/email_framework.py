import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def s_email(company_name,location, Job_Profile,email,sec_question,sec_answer,date_applied):
    """
    Send an email to notify the user.

    :param company_name: Company name of the application
    :param location: location of the application
    :param Job_Profile: Application job profile
    :param email: email of the user
    :param sec_question: Security question
    :param sec_answer: security answer
    :param date_applied: date of the application
    :return: returns one if the email was sent successfully returns zero if it was failed
    """
    sender_email = "wolftrackproject@gmail.com"
    receiver_email = email
    # App Password of Gmail Account
    password = "dlafyfekdkmdfjdi"

    subject = "WolfTrack - Job Added to List"
    body = "WOLFTRACK APPLICATION \n\n" \
       "You have applied to " + company_name + " for the job profile - " + Job_Profile + \
       ". \nPlease find the details below: \n" \
       "Date Applied: " + date_applied + "\n" "Location: " + location + "\n" \
                                                                        "Security Question: " + sec_question + "\n" \
                                                                                                               "Security Answer: " + sec_answer + "\n" \
                                                                                                                                                  "All the best for you Application!\n" \
                                                                                                                                                  "The WolfTrack Team."

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email

    message.attach(MIMEText(body, "plain"))

    text = message.as_string()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com",
                          465,
                          context=context) as server:
        server.login(sender_email,password)
        server.sendmail(sender_email,receiver_email,text)

    return True

if __name__ == "__main__":
    s_email('IBM','Raleigh','SDE','swetha11895@gmail.com','Favorite Sport','Badminton','11/25/2021')