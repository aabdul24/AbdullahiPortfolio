class GasStation:
    '''This class serves as a calculator for money spent and gained from a gas 
    station, as well as the amount of gas left in two types of octane tanks, 
    high and low. It also calculates amounts of gas as well as money gained from
    selling to consumers.
    '''

    def __init__ (self):

        '''This function defines all the attributes to be used in this class,
        as well as setting values to the attributes.
        '''
        self.low_octane_tank = 2000
        self.high_octane_tank = 1000
        self.money = 1000
        self.wholesale_low = 1.91
        self.wholesale_high = 2.21
        self.retail_low = 2.31
        self.retail_med = 2.45
        self.retail_high = 2.59

    def buy_gas(self, buygas):

        ''' This function calculates the amount of money to fill up the gas station
        tanks, based on the wholesale gas prices and type of gas.

        Args:
            buygas: determines whether the gas will be high or low octane.
        '''

        if buygas == "low":
            gas_amount_low = 2000 - self.low_octane_tank
            self.money -= (gas_amount_low * self.wholesale_low)
            self.low_octane_tank = 2000
        elif buygas == "high":
            gas_amount_high = 2000 - self.high_octane_tank
            self.money -= (gas_amount_high * self.wholesale_high)
            self.high_octane_tank = 2000
    
    def sell_gas(self, gallons, sellgas):

        '''This function calculates amount of money made by the gas station after
        selling gas, as well as the remaining amount of gallons in the tank.

        Args
            gallons: amount of gallons bought by a customer at the station
            sellgas: the type of gas used by the customer, 'high', 'med/, or 'low'
        '''

        if sellgas == "low":
            self.low_octane_tank = self.low_octane_tank - gallons
            self.money += (gallons * self.retail_low)
        elif sellgas == "med":
            self.low_octane_tank = self.low_octane_tank - (gallons/2)
            self.high_octane_tank = self.high_octane_tank - (gallons/2)
            self.money += (gallons * self.retail_med)
        elif sellgas == "high":
            self.high_octane_tank = self.high_octane_tank - gallons
            self.money += (gallons * self.retail_high)
        if self.low_octane_tank < 100:
            self.buy_gas("low")
        elif self.high_octane_tank < 100:
            self.buy_gas("high")



    



