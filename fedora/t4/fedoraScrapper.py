from fedora.client.fas2 import AccountSystem

input = raw_input('Please type the username:')
fas = AccountSystem(username=input)
people = fas.person_by_username(str(input))
print(people)
print("Email ID of user: " + people["bugzilla_email"])

