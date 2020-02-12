# array is always sorted
# first value will always be 0

# linear 
def smallest_missing(arr):
    # loop through the array using their indices
    for i in range(len(arr)):
        # check that each element matches its index
        if arr[i] != i:
            # if it doesn't match, return i (because it's the smallest missing element)
            return i
    # otherwise nothing is missing, so add on the next integer which becomes the smallest missing 
    return len(arr)


print(smallest_missing([0,1,2,3,5,6,7]))
print(smallest_missing([]))


# binary search