#Binary search algorithm

def binarySearch(arr, x):
    high = len(arr) - 1
    low = 0
    mid = 0
    arr.sort()
    while low <= high:
        mid = (high + low)/2
        if arr[mid] < x: #if middle element of array is less than target, then check second half of array
            low = mid + 1 #move low pointer to one ahead of middle element
        elif arr[mid] > x: #if middle element of array is greater than target, then check first half of array
            high = mid - 1 #move high pointer to one behind middle element
        else:
            return mid #return index of element if found
        
    return -1 #if not found in array

def main():
    #sample array
    arr = [2, 3, 4, 10, 40]
    x = 10 #element to be searched
    result = binarySearch(arr, x)
    if result != -1:
        print(f"Element is present at index {result}")
    else:
        print("Element is not present in array")

main()