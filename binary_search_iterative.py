list = []


def binary_search(arr, number, low, high):

    while low <= high:
        mid = low + (high-low)//2

        if arr[mid] == number:
            return mid
        elif arr[mid] < number:
            low = mid + 1
        else:
            high = mid - 1

    return -1


print("Number of elements in list: ")
num = int(input())

print("Elements in list:")
for i in range(0, num):
    elem = int(input())
    list.append(elem)

print("------------------")
print("Introduce the number to find within the list: ")
target = int(input())

result = binary_search(list, target, 0, len(list)-1)

if result != -1:
    print("Element is present at index %s within the list" % result)
else:
    print("Not found")
