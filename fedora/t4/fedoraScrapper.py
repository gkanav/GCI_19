from fedora.client.fas2 import AccountSystem

input = raw_input('Please type the username:')
fas = AccountSystem(username="gkanav")
people = fas.person_by_username(str(input))
if len(people) == 0:
    print("Sorry, user does not exist.")
else:
    print("Email ID of user: " + people["bugzilla_email"])

