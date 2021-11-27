from flask import Blueprint, flash, session
from flask import Flask, render_template, url_for, request
from flask_login import login_required, logout_user, login_manager
from werkzeug.utils import redirect
from Controller.user_controller import User
from Controller.application_controller import Application

home_route = Blueprint('home_route', __name__)

user = User()
application = Application()
# login = login_manager.LoginManager(application)

upcoming_events = [
    {"duedate": "10th Dec, 2021",
     "company": "Apple"
     },
    {"duedate": "12th Dec, 2021",
     "company": "Microsoft"
     },
    {"duedate": "15th Dec, 2021",
     "company": "Amazon"
     },
    {"duedate": "21st Dec, 2021",
     "company": "Amazon"
     },
    {"duedate": "21st Dec, 2021",
     "company": "Amazon"
     }
]


@home_route.route('/', methods=['GET'])
def home():
    return redirect("/auth")

@home_route.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html', loginError="")


@home_route.route('/auth', methods=['GET'])
def auth():
    data = user.get_auth_user_dao(session['email'])
    data["wishlist"] = application.get(session['email'], 1)
    return render_template('home.html', data=data, upcoming_events=upcoming_events)


@home_route.route('/loginUser', methods=['GET', 'POST'])
def loginUser():
    session['email'] = request.form["username"]
    password = request.form["password"]
    result = user.get(session['email'], password)
    # print(result)
    error = ""
    if (result == 0):
        error = "Email does not exits. Please enter a valid email."
        return render_template('login.html', loginError=error)
    elif (result == 2):
        error = "Password incorrect."
        return render_template('login.html', loginError=error)
    else:
        return render_template('home.html', data=result, upcoming_events=upcoming_events)


@home_route.route('/signup', methods=['POST'])
def signup():
    name = request.form["name"]
    session['email'] = request.form["email"]
    password = request.form["password"]
    # result = user.post(name, session['email'], password)
    print(name)
    gender = request.form["gender"]
    location = request.form["location"]
    result = user.post(name, session['email'], password, gender, location)
    if (result == 0):
        error = "This email already exists. Please try with different email"
        return render_template('login.html', emailError=error)
    data = {}
    data["full_name"] = name
    return render_template('home.html', data=data, upcoming_events=upcoming_events)


@home_route.route('/view', methods=['GET'])
# @login_required
def view():
    application_category = request.args.get('show')

    result_data = application.get(session["email"], application_category)

    print(result_data)

    return render_template('view_list.html', data=result_data, upcoming_events=upcoming_events)


@home_route.route("/add_new_application", methods=["GET", "POST"])
# @login_required
def add_new_application():
    company_name = request.form["companyName"]
    location = request.form["location"]
    job_profile = request.form["jobProfile"]
    salary = request.form["salary"]
    username = request.form["username"]
    password = request.form["password"]
    security_question = request.form["securityQuestion"]
    security_answer = request.form["securityAnswer"]
    notes = request.form["notes"]
    date_applied = request.form["dateApplied"]
    status = request.form["status"]
    print("status", status)
    result = application.post(session['email'], company_name, location, job_profile, salary, username, password,
                              security_question, security_answer, notes,
                              date_applied, status)
    if (result == 0):
        error = "This job application could not be stored in the database. Please try again."
        return render_template('home.html', jobAddError=error)
    data = {}
    return redirect("/auth")


@home_route.route("/change_status_application", methods=["POST"])
# @login_required
def change_status_application():
    status = request.form["status_change"]
    application_id = request.form["application_id"]
    print("status", status)
    result = application.change_status( application_id, status)
    if (result == 0):
        error = "This job application could not be stored in the database. Please try again."
        return render_template('home.html', jobAddError=error)
    data = {}
    return redirect("/auth")


@home_route.route("/delete_application", methods=["POST"])
# @login_required
def delete_application():
    application_id = request.form["application_id"]
    result = application.delete( application_id)
    if (result == 0):
        error = "This job application could not be stored in the database. Please try again."
        return render_template('home.html', jobAddError=error)
    data = {}
    return redirect("/auth")
    #return render_template('home.html', data=data, upcoming_events=upcoming_events)


@home_route.route("/edit_application", methods=["POST"])
# @login_required
def edit_application():
    company_name = request.form["companyName"]
    location = request.form["location"]
    job_profile = request.form["jobProfile"]
    salary = request.form["salary"]
    username = request.form["username"]
    password = request.form["password"]
    security_question = request.form["securityQuestion"]
    security_answer = request.form["securityAnswer"]
    notes = request.form["notes"]
    date_applied = request.form["dateApplied"]
    status = request.form["status"]
    application_id = request.form["application_id"]
    print("status", status)
    result = application.update(company_name, location, job_profile, salary, username, password,
                              security_question, security_answer, notes,
                              date_applied, status, application_id)
    if (result == 0):
        error = "This job application could not be stored in the database. Please try again."
        return render_template('home.html', jobAddError=error)
    data = {}
    return redirect("/auth")

@home_route.route('/logout', methods=['GET'])
# @login_required
def logout():
    # logout_user()
    return redirect("/login")

# if __name__ == '__main__':
#     app.run(debug=True)
