print('A:')
a = input()
print('B:')
b = input()
print('C:')
c = input()
ab = int(a) + int(b)  # c
bc = int(b) + int(c)  # a
ac = int(a) + int(c)  # b

if int(ab) > int(c):
    if int(ac) > int(b):
        if int(bc) > int(a):
            print("Yes")
