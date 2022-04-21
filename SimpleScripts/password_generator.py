# Given a maximum length by the user, this script generates a pseudo-random password
import string as st
import random

# By using the string library constants, we create a list from which we extract the possible combinations
chars = list(st.ascii_lowercase + st.ascii_uppercase + st.digits + st.punctuation)

print(chars)

# ------------ in progress
