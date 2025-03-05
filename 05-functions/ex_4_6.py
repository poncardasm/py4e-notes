def computepay(h, r):
    if h > 40:
        reg = h * r
        oth = (h - 40.0) * (r * 0.5)
        otp = reg + otp

hr = input("Enter Hours: ")
rate = input("Enter Rate: ")
p = computepay(hr, rate)
print("Pay", p)