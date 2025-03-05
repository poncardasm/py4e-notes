def computepay(h, r):
    if h > 40:
        reg = h * r
        oth = (h - 40.0) * (r * 0.5)
        return reg + oth
    else:
        return h * r

hr = input("Enter Hours: ")
rate = input("Enter Rate: ")
p = computepay(float(hr), float(rate))
print("Pay", p)