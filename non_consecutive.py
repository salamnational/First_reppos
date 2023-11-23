def first_non_consecutive(arr):
    while i in arr:
        if arr[arr.index(i)] - arr[arr.index(i) + 1] != -1:
            return arr[arr.index(i) + 1]
arr = [1,2,3,4,5]
first_non_consecutive(arr)