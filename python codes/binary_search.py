# This program implements Binary Search for a Sorted Array using the Iterative Approach 
# Displays the location of the element if present and prints message accordingly

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        #Ignoring left half if element is greater
        if arr[mid] < x:
            low = mid + 1
 
        #Ignoring right half if element is smaller
        elif arr[mid] > x:
            high = mid - 1
 
        #Returning location of element, if found
        else:
            return mid
 
    #Returns -1 if element is not present
    return -1
 
 
# Taking a test array
arr = [0, 1, 5, 15, 20, 60, 128, 240, 480]
x = 128
 
# Calling the function
result = binary_search(arr, x)
 
if result != -1:
    print("Element "+ str(x) + " is found at index", str(result))
else:
    print("Element is not present in array...")
