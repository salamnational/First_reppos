def positive_sum(arr):
    pos = []
    for i in arr:
        if i > 0 :
            pos.append(i)
    return sum(pos)
