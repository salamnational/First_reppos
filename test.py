def count_positives_sum_negatives(arr):
    if arr == []:
        return arr
    else:
        pos = []
        neg = []
        for i in arr:
            if i > 0:
                pos.append(i)
            elif i < 0:
                neg.append(i)
        return [len(pos), sum(neg)]


