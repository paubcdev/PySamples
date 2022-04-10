from math import sqrt
n = 25
root = sqrt(abs(n))
if int(root + 0.5) ** 2 == n:
    print('True')
else:
    print('False')
