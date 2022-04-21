# Given a maximum length by the user, this script generates a pseudo-random password
import string as st
import random

password = " "
# By using the string library constants, we create a list from which we extract the possible combinations
chars = st.ascii_lowercase + st.ascii_uppercase + st.digits + st.punctuation

print("Introduce the length of the password")
pass_len = int(input("Minimum 3 characters: "))

for i in range(0, pass_len):
    pass_index = random.randrange(0, len(chars))
    password += chars[pass_index]

print(password)
