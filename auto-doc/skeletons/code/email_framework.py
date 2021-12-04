class s_email:
    """
    A class that defines the email parameters.An email is sent when a new account is created, new job application is submitted, or a status change in application. It takes in the company_name, location, job_Profile, salary, username, password,email, security_question, security_answer, notes, date_applied, status, In this format, the email is sent from

    :param sender: wolftrackproject@gmail.com
    :param receiver: The email address of the receiver(User)
    @return: true if the email sent successfully, false if not
    .. list-table::
        :header-rows: 1

        * - Content
          - Value
        * - company Name
          - Name of the company
        * - Date Applied
          - Today's date
        * - Location
          - Location you entered for job application
        * - Salary
          - Your salary expectation
        * - User_name
          - Username you want to create in job application portal
        * - Password
          - Password you wish to set for the job application portal
        * - Security Question
          - Any relevant question you want to set
        * - Security Answer
          - Corresponding answer for the previous question
        * - Status
          - "Applied"
        * - Notes
          - Any notes or information you would like to share with the company

    |
    """

def status_change_email(application_id, email, status):
    """
    Send email for any change in status of application

    :param application_id: an ID is created when you sent a job application. That is used here.
    :param email: Your email ID mentioned in the job application will be notified.
    :param status: The status of your application change to "In Review", "Interview", "Offered", "Rejected", "No Longer under consideration"
    """