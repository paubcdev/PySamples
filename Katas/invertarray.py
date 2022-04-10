lst = [30, -50, 257, 458, -9851]
arr = []
for i in lst:
    if i >= 0:
        arr.append(-abs(i))
    elif i <= 0:
        arr.append(abs(i))
print(arr)
