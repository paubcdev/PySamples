# Given a number of passwords and maximum length by the user, this script generates a list of pseudo-random passwords,
# all of them the given length
import string as st
import random
# By using the string library constants, we create a string from which we extract the possible combinations
CHARS = st.ascii_lowercase + st.ascii_uppercase + st.digits + st.punctuation
list_of_passwords = []


def generator(length):
    password = " "
    for i in range(0, length):
        pass_index = random.randrange(0, len(CHARS))
        password += CHARS[pass_index]
    return password


numPasswords = int(input("How many passwords will you generate? "))

if numPasswords <= 0:
    raise TypeError("Must be a positive number")
else:
    print("Introduce the length of the password")
    pass_len = int(input("Minimum 3 characters: "))
    if pass_len >= 3:
        for number in range(0, numPasswords):
            list_of_passwords.append(generator(pass_len))

        for pass_ in list_of_passwords:
            print(pass_)
    else:
        raise TypeError("Must be more than 3 characters")
