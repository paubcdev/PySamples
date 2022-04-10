arr = []
if not arr:
    print("Empty")
else:
    arrpos = []
    arrneg = []
    sum = 0
    result = []
    for i in arr:
        if i > 0:
            arrpos.append(i)
        elif i < 0:
            arrneg.append(i)
    for a in range(0, len(arrneg)):
        sum = sum + arrneg[a]
    result.append(len(arrpos))
    result.append(sum)
    print(result)
