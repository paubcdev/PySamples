arr = [100, 40, 34, 57, 29, 72, 57, 88]
score = 0


# My solution:
def better_than_average1(class_points, your_points):
    sum = 0
    avg = 0
    for i in class_points:
        sum = sum + i
    avg = sum / len(class_points)
    if your_points >= avg:
        return True
    elif your_points < avg:
        return False


# Better solution:
def better_than_average2(class_points, your_points):
    return (sum(class_points)/len(class_points) < your_points)


print(better_than_average1(arr, score))
print(better_than_average2(arr, score))
