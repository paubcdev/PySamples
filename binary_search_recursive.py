li = []


def binary_search(arr, number, low, high):
    if high >= low:
        mid = (high + low) // 2

        if arr[mid] == number:
            return mid

        elif arr[mid] > number:
            return binary_search(arr, number, low, mid-1)

        else:
            return binary_search(arr, number, mid+1, high)

    else:
        return -1


print("Number of elements in list: ")
num = int(input())

print("Elements in list:")
for i in range(0, num):
    elem = int(input())
    li.append(elem)

print("------------------")
print("Introduce the number to find within the list: ")
target = int(input())

result = binary_search(li, target, 0, len(li)-1)

if result != -1:
    print("Element is present at index %s within the list" % result)
else:
    print("Not found")
