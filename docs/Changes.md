# Changes in project 2
## Front End:
### Additions:
1) We have added the gender and location input in the the signup container as they were missing.
## API
### Additions:
1) API for signup: which checks if the email ID proved by the user is already existing or not. If exists API will prevent from creating with same email otherwise it will let the user to signup with the corresponding email.
2) API for login: which checks if the given email is already existing if exists then checks if user has entered right password or not. If both email and password matches then User will be allowed to login. Otherwise user will be prevented from logging in sucessfully.
## Database:
### Additions:
1) Added stored procedure to create an user when user signs up.
### Modifications
1) Removed redunacy in table colums so that tables are in first normal form, second normal form and third normal form.
2) Removed unnecessary columns from the tables which were not needed.
3) Removed uncessary tables.
4) Added the missing colums like gender and location in user table