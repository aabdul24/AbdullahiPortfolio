# in the following line, replace hw3 with the name of your file,
# minus the .py
from homework3 import GasStation
from math import isclose

gs = GasStation()

assert isclose(gs.low_octane_tank, 2000), \
    "low_octane_tank has wrong initial value"
assert isclose(gs.money, 1000), "money has wrong initial value"
assert isclose(gs.wholesale_low, 1.91), "wholesale_low has wrong initial value"

print("1")

gs.sell_gas(100, "med")
assert isclose(gs.money, 1245.0), "amount earned from sale of gasoline is wrong"
assert isclose(gs.low_octane_tank, 1950.0), \
    "amount of gas from low octane tank for medium octane customer is wrong"

print("2")

gs.buy_gas("low")
assert isclose(gs.low_octane_tank, 2000), \
    "low octane tank was improperly refilled"
assert isclose(gs.money, 1149.5), \
    "cost to refill low octane tank was miscalculated"

print("3")

for i in range(30):
    # sell enough gas to deplete the high_octane tank enough to trigger refill
    gs.sell_gas(50, "high")
    assert gs.high_octane_tank >= 100

# this message only gets printed if all assertions were accurate
print("Passed all tests")