def fake_bin(x):
    binair = []
    for i in x:
        if int(i) < 5:
           binair.append("0")
        elif int(i) >= 5:
            binair.append("1")
    pntri("".join(binair))
