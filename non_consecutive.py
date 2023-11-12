def first_non_consecutive(arr):
    for i in arr:
        if arr[arr.index(i)] - arr[arr.index(i) + 1] != -1:
            return arr[arr.index(i) + 1]
