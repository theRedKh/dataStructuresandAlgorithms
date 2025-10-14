#Implementation of quicksort algorithm done in class
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]  # Use the last element as the pivot value
    left = lessThanEqual(pivot, arr)  # Pass the pivot value
    right = greaterThan(pivot, arr)  # Pass the pivot value
    sortedLeft = quicksort(left)
    sortedRight = quicksort(right)
    final = []
    final.extend(sortedLeft)
    final.append(pivot)
    final.extend(sortedRight)
    return final

def lessThanEqual(pivot, arr):
    newArr = []
    for i in range(len(arr) - 1):  # Exclude the pivot itself
        if arr[i] <= pivot:
            newArr.append(arr[i])
    return newArr

def greaterThan(pivot, arr):
    newArr = []
    for i in range(len(arr) - 1):  # Exclude the pivot itself
        if arr[i] > pivot:
            newArr.append(arr[i])
    return newArr

def main():
    arr = [85, 24, 63, 45, 17, 31, 96, 50]
    newArr = quicksort(arr)
    print(newArr)

main()