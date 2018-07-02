# Assignment 4.6
# program to compute gross pay using input for hours and rate from user.
# Awards time-and-a_half for hourly rate where hours exceed 40 hours
def computepay(h,r):
    if h > 40:
        ot = (h - 40)*(r * 1.5)
        rp = 40 * r
        return rp + ot
    else:
        return h * r

hrs = input("Enter Hours: ")
rate = input("Enter Hourly Rate: ")
p = computepay(float(hrs),float(rate))

print("Calculated Pay is " + str(p))
