import random

import pandas as pd


class BettingStrategies:
    # This is to limit the number of bets one can make
    no_of_bets = 50
    # Odds are in the form of double or nothing
    odds = [2, 0]
    instances = 0

    def __init__(self, wealth: int, fraction_to_bet):
        self.wealth = wealth
        self.fraction_to_bet = fraction_to_bet

        BettingStrategies.instances += 1

    # Proportional bets are where you stake a certain percentage of your wealth for every bet

    def toss(self):
        return random.choice(self.odds)

    def proportional_bets(self):
        i = 0
        change_wealth = []
        # this runs as long as the wealth is not zero and the limit number of bets has not been reached
        while self.wealth > 0 and i < self.no_of_bets:
            bet_size = self.wealth * self.fraction_to_bet
            self.wealth += -bet_size + round(bet_size * self.toss(), 2)
            change_wealth.append(self.wealth)
            i += 1
        dataframe = pd.DataFrame(change_wealth)
        return dataframe

    def martingale_bet(self):
        i = 0
        change_wealth = []

        # For martingale, you double the bet size every time you lose a bet
        bet_size = self.wealth * self.fraction_to_bet

        # This runs as long as the wealth is not zero and the limit number of bets has not been reached
        while self.wealth > 0 and i < self.no_of_bets:
            if self.toss() == 2:
                self.wealth += -bet_size + round(self.toss())
            else:
                self.wealth += -bet_size
                bet_size = bet_size * 2
            change_wealth.append(self.wealth)
        dataframe = pd.DataFrame(change_wealth)
        return dataframe


all_in = BettingStrategies(100, 1).proportional_bets()
prop1 = BettingStrategies(100, .1).proportional_bets()
prop2 = BettingStrategies(100, .3).proportional_bets()
prop3 = BettingStrategies(100, .6).proportional_bets()
prop4 = BettingStrategies(100, .9).proportional_bets()
martingale = BettingStrategies(100, .1).martingale_bet()
with pd.ExcelWriter('C:\\Users\\chris\\Documents\\Financial Independence\\exp.xlsx') as writer:
    all_in.to_excel(writer, 'all_in')
    prop1.to_excel(writer, 'prop1')
    prop2.to_excel(writer, 'prop2')
    prop3.to_excel(writer, 'prop3')
    prop4.to_excel(writer, 'prop4')
    martingale.to_excel(writer, 'martingale')
