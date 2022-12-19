import random

import pandas as pd


class BettingStrategies:
    no_bets = 50
    odds = [2, 0]
    instances = 0

    def __init__(self, wealth: int, fraction_to_bet):
        self.wealth = wealth
        self.fraction_to_bet = fraction_to_bet

        BettingStrategies.instances += 1

    def outcomes(self):
        i = 0
        change_wealth = []
        while self.wealth > 0 and i < self.no_bets:
            bet_size = self.wealth * self.fraction_to_bet
            self.wealth += -bet_size + round(bet_size * random.choice(BettingStrategies.odds), 2)
            change_wealth.append(self.wealth)
            i += 1
        return change_wealth

    def to_dataframe(self):
        to_dataframe = pd.DataFrame(self.outcomes())
        return to_dataframe
