from fitting_functions import *
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

data = np.genfromtxt("tips.csv", delimiter=",", skip_header=1)
print("column names:", open("tips.csv").readline())

bill_col = 0
tip_col = 1
pcttip_col = 6

bill = data[:, bill_col]
tip = data[:, tip_col]
pcttip = data[:, pcttip_col]
print("PctTip values:", pcttip[:10])

# graph 1 : bill v tip
slope1, intercept1, r1, p1, stderr1 = stats.linregress(bill, tip)

plt.figure()
plt.scatter(bill, tip, label="Data")
plt.plot(bill, linear(slope1, bill, intercept1),
         color="red", label="Best-fit line")

plt.xlabel("Bill ($)")
plt.ylabel("Tip ($)")
plt.title("Bill vs Tip")
plt.legend()
plt.show()

# equation for graph 1
print("Bill vs Tip")

print_equation(slope1, intercept1, "dollars", "dollars")

# the equation of the line is: y = 0.1822147343931658 dollars/dollar x + -0.29226745918876684 dollars

# graph 2: bill v pcttip

slope2, intercept2, r2, p2, stderr2 = stats.linregress(bill, pcttip)

plt.figure()
plt.scatter(bill, pcttip, label="Data")
plt.plot(bill, linear(slope2, bill, intercept2), color ="red", label="best-fit line")
plt. xlabel("bill($)")
plt.ylabel("percent tip(%)")
plt.show()

print("bill v percent tip:")

print_equation(slope2, intercept2, "%", "dollars")

#  the equation of the line is: y = 0.04881243662941923 %/dollar x + 15.509648231754028 %

# litte conclusion
# people with higher bills tend to tip a slighty higher percentage
