def find_multiples(integer, limit):
    ml=range(integer, limit)
    result=[integer]
    for i in ml:
        if ml[ml.index(i) + 1] == i*i:
            result.append(i)
    return sorted(result)
find_multiples(2,6)
print(ml)
