from collections import Counter
seq = [1, 2, 5, 2, 1]

# My answer
ke = Counter(seq).keys()
val = Counter(seq).values()
dictio = dict(zip(val, ke))

for i in dictio:
    if i % 2 != 0:
        print(dictio[i])

# Long answer
for i in seq:
    if seq.count(i) % 2 != 0:
        print(i)
