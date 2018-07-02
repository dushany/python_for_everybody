hrs = input("Enter Hours:")
h = float(hrs)

rte = input("Enter Rate per Hour:")
r = float(rte)

if h > 40:
    ot = (h - 40) * (r * 1.5)
    print((40 * r) + ot)
else:
    print(h * r)
