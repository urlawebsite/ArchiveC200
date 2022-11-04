def binarySearch(array, x, low, high):
    while low <= high:
        mid = low + (high - low) // 2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1


array = [3, 4, 5, 6, 7, 8, 9]
x = 4
result = binarySearch(array, x, 0, len(array) - 1)
if result != -1:
    print("Target found", str(result))
else:
    print("Target not found")


def binarySearch2(array, x, low, high):
    if high >= low:
        mid = low + (high - low) // 2
        if array[mid] == x:
            return mid
        elif array[mid] > x:
            return binarySearch2(array, x, low, mid - 1)
        else:
            return binarySearch2(array, x, mid + 1, high)
    else:
        return -1


array = [3, 4, 5, 6, 7, 8, 9]
x = 4
result = binarySearch2(array, x, 0, len(array) - 1)

if result != -1:
    print("Target found", str(result))
else:
    print("Target not found")


def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array)-1, -1):
            if array[j] > array[j-1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array


data = [-2, 45, 0, 11, -9]

bubbleSort(data)
print(bubbleSort(data))


def insertionSort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data


data = [-2, 45, 0, 11, -9]
print(insertionSort(data))
