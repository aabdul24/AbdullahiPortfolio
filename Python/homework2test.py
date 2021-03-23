from math import isclose
# in the line below, replace homework2 with the name of your script
# minus the .py extension
import homework2 as hw2
print("1")
assert isclose(hw2.min_payment(100_000, 0.05), 536.821, rel_tol=0.01), \
    "unexpected result for min_payment(100000, 0.05)"
print("2")
assert isclose(hw2.min_payment(100_000, 0.05, 30, 12), 536.822, rel_tol=0.01), \
    "unexpected result for min_payment(100000, 0.05, 30, 12)"
print("3")
assert isclose(hw2.min_payment(200_000, 0.04, 15), 1479.376, rel_tol=0.01), \
    "unexpected result for min_payment(200000, 0.04, 15)"
print("4")
assert isclose(hw2.interest_due(100_000, 0.05), 416.667, rel_tol=0.01), \
    "unexpected result for interest_due(100000, 0.05)"
print("5")
assert isclose(hw2.interest_due(300_000, 0.04, 6), 2000, rel_tol=0.01), \
    "unexpected result for interest_due(300000, 0.04, 6)"
print("6")
assert hw2.remaining_payments(100_000, 0.05, 537) == 360, \
    "unexpected result for remaining_payments(100_000, 0.05, 537)"
print("7")
assert hw2.remaining_payments(250_000, 0.04, 4000) == 71, \
    "unexpected result for remaining_payments(250_000, 0.04, 4000) == 71"
print("8")

# if we get this far, all assertions were true
print("Passed all tests")