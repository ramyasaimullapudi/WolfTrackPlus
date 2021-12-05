import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def s_email(
    company_name,
    location,
    job_Profile,
    salary,
    # username,
    # password,
    email,
    # security_question,
    # security_answer,
    # notes,
    # date_applied,
    status,
):
    """
    Send an email to notify the user.

    :param company_name: Company name of the application
    :param location: location of the application
    :param Job_Profile: Application job profile
    :param email: email of the user
    :return: returns one if the email was sent successfully returns zero if it was failed
    """
    sender_email = "wolftrackproject@gmail.com"
    receiver_email = email
    password = "dlafyfekdkmdfjdi"

    subject = "WolfTrack++ - Job Application Added"
    body = (
        "WOLFTRACK++ APPLICATION \n\n"
        "You have applied to "
        + company_name
        + " for the job profile - "
        + job_Profile
        + ". \nPlease find the details below: \n"
        # "Date Applied: " + date_applied + "\n"
        "Location: " + location + "\n"
        "Salary: " + salary + "\n"
        # "User_name: " + username + "\n"
        # "Password: " + password + "\n"
        # "Security Question: " + security_question + "\n"
        # "Security Answer: " + security_answer + "\n"
        "Status: " + status + "\n"
        # "Notes: " + notes + "\n\n\n"
        "All the best for you Application!\n"
        "The WolfTrack++ Team."
    )
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email

    message.attach(MIMEText(body, "plain"))

    text = message.as_string()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)

    return True


def status_change_email(application_id, email, status):

    sender_email = "wolftrackproject@gmail.com"
    receiver_email = email
    password = "dlafyfekdkmdfjdi"

    subject = "WolfTrack++ - Status Update"
    body = (
        "WOLFTRACK++ APPLICATION UPDATE \n\n"
        "The status has been changed to "
        + status
        + " for the job id - "
        + application_id
        + "\n\n"
        "Please reply back to this mail if you have any queries!\n"
        "The WolfTrack++ Team."
    )
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email

    message.attach(MIMEText(body, "plain"))

    text = message.as_string()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)

    return True


if __name__ == "__main__":
    status_change_email("1", "swetha11895@gmail.com", "In Review")
