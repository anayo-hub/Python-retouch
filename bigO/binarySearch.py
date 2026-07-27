# sorted array is what goes with binary search in other to get the index
arr = [2, 5, 8, 12, 16, 23, 38, 45, 56, 61, 72, 84, 91, 99]


def binarySearch(arr, x):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == x:  
            return mid
        elif arr[mid] < x:
            low =  mid + 1
        else:
            low = mid - 1
    return - 1


print(binarySearch(arr, 99))