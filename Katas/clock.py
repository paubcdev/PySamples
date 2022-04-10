h = 1
m = 0
s = 54

if (0 <= h <= 23):
    if (0 <= m <= 59):
        if (0 <= s <= 59):
            milis = 0
            milis = h * 3600000 + m * 60000 + s * 1000
print(milis)
