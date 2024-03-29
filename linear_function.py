import numpy as np

try:
    a, b = np.loadtxt("result.txt", unpack=True)
except IOError:
    a = b = 0
except ValueError:
    exit(1)
try:
    x = float(raw_input(
        "Please tell us the mileage of your car to get an estimation of the price: "))
    if (x < 0):
        print "The mileage can't be negative."
        exit(1)
    print "The estimated price of your car based on the analyzed data is {:.2f}$.".format(
        max(a * x + b, 0))
except ValueError:
    print "Invalid value received (should be a number)."
