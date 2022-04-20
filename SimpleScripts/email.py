# Given an email address as an input, slice it to get the username
# and the domain name as different strings

email = str(input("Enter complete email: ")).strip()  # the .strip method eliminates trailing whitespaces

user_name = email[:email.index('@')]
domain_name = email[email.index('@') + 1:]

print(f"Username is: {user_name} and domain name is: {domain_name}")
