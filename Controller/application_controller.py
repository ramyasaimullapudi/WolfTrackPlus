from flask import render_template, request
from flask_restful import Resource
from flask_login import login_required
from DAO.application_dao import application_dao


class Application(Resource):
    def __init__(self):
        self.headers = {"Content-Type": "text/html"}
        self.application = application_dao()

    # @login_required
    def get(self, email, application_category):
        return self.application.get_application(email, application_category)

    # @login_required
    def post(
        self,
        email,
        company_name,
        location,
        job_profile,
        salary,
        username,
        password,
        security_question,
        security_answer,
        notes,
        date_applied,
        status,
    ):
        return self.application.add_application(
            email,
            company_name,
            location,
            job_profile,
            salary,
            username,
            password,
            security_question,
            security_answer,
            notes,
            date_applied,
            status,
        )

    def change_status(self, status, application_id):
        return self.application.change_status(status, application_id)

    # @login_required
    def update(
        self,
        company_name,
        location,
        job_profile,
        salary,
        username,
        password,
        security_question,
        security_answer,
        notes,
        date_applied,
        status,
        application_id,
    ):
        return self.application.update_application(
            company_name,
            location,
            job_profile,
            salary,
            username,
            password,
            security_question,
            security_answer,
            notes,
            date_applied,
            status,
            application_id,
        )

    # @login_required
    def delete(self, application_id):
        return self.application.delete_application(application_id)
