from DAO.sql_helper import sql_helper


class application_dao:
    def __init__(self):
        self.__db = sql_helper()

    def add_application(
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
        userId = self.__db.run_query(
            "SELECT user_id FROM user WHERE email='" + email + "'"
        )[0][0]

        self.__db.run_query(
            "INSERT into company (company_name) values ('" + company_name + "');"
        )
        companyId = self.__db.run_query(
            "SELECT company_id FROM company WHERE company_name='" + company_name + "'"
        )[0][0]

        self.__db.run_query("INSERT INTO roles (role) values ('" + job_profile + "');")
        roleId = self.__db.run_query(
            "SELECT role_id FROM roles WHERE role='" + job_profile + "'"
        )[0][0]

        return self.__db.run_query(
            "INSERT INTO application (user_id, company_id, role_id, application_date, job_description, salary, location, status, imortant_links) values ("
            + str(userId)
            + ", "
            + str(companyId)
            + ", "
            + str(roleId)
            + ", "
            + date_applied
            + ", '"
            + job_profile
            + "', "
            + str(salary)
            + ", '"
            + location
            + "', '"
            + status
            + "', '"
            + notes
            + "');"
        )

    def get_application(self, email, application_status):
        userId = self.__db.run_query(
            "SELECT user_id FROM user WHERE email='" + email + "'"
        )[0][0]

        sQuery = (
            "SELECT company_name, status, application_date, application_id, location, role, salary, imortant_links"
            + "  FROM application JOIN company ON company.company_id = application.company_id "
            + " JOIN roles ON roles.role_id = application.role_id "
            + "WHERE user_id="
            + str(userId)
        )

        if application_status != "":
            sQuery += f" and status = '{application_status}'"

        res = self.__db.run_query(sQuery)

        res = [list(i) for i in res]
        for i in res:
            i[2] = i[2][:10]

        print(res)
        return res

    def update_application(
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

        res = self.__db.run_query(
            "SELECT company_name,company.company_id, role, roles.role_id"
            + "  FROM application JOIN company ON company.company_id = application.company_id "
            + " JOIN roles ON roles.role_id = application.role_id "
            + "WHERE application_id="
            + str(application_id)
        )

        companyId = res[0][1]
        roleId = res[0][3]
        if res[0][0] != company_name:
            self.__db.run_query(
                "INSERT into company (company_name) values ('" + company_name + "');"
            )
            companyId = self.__db.run_query(
                "SELECT company_id FROM company WHERE company_name='"
                + company_name
                + "'"
            )[0][0]

        if res[0][2] != job_profile:
            self.__db.run_query(
                "INSERT INTO roles (role) values ('" + job_profile + "');"
            )
            roleId = self.__db.run_query(
                "SELECT role_id FROM roles WHERE role='" + job_profile + "'"
            )[0][0]

        sQuery = (
            f"Update application set company_id={companyId}, role_id={roleId}, job_description='{job_profile}', "
            + f"salary={salary}, location='{location}', status='{status}', imortant_links='{notes}' where application_id="
            + str(application_id)
        )
        return self.__db.run_query(sQuery)

    def change_status(self, application_id, status):
        res = self.__db.run_query(
            "UPDATE application SET status = '"
            + status
            + "' WHERE application_id="
            + str(application_id)
        )
        print(res)
        return res

    def delete_application(self, application_id):
        res = self.__db.run_query(
            "DELETE FROM application WHERE application_id=" + str(application_id)
        )
        return res
