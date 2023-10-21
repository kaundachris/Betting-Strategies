import random

import pandas as pd


class BettingStrategies:
    """
    This is to limit the number of bets one can make. Everyone has to go home at some point.
    Odds are in the form of double or nothing.
    """
    maximum_bets = 50
    odds = [2, 0]
    number_of_bets_so_far = 0

    def __init__(self, wealth: int, fraction_to_bet: float):
        """

        :param wealth: How much the bettor ahs to bet.
        :param fraction_to_bet: How much of the wealth the bettor wants to stake.
        """
        self.wealth = wealth
        self.fraction_to_bet = fraction_to_bet

        BettingStrategies.number_of_bets_so_far += 1

    def toss(self):
        """
        :return: The outcome of a toss. Heads doubles your stake, tails loss your stake .
        """
        return random.choice(self.odds)

    def proportional_bets(self):
        """
        You bet a constant proportion of your total wealth.
        You can keep doing so, so long as your wealth has not hit zero, or you have not hit the bet limit.
        :return: list of the wealth sizes over the course of the betting.
        """
        i = 0
        change_wealth = []
        while self.wealth > 0 and i < self.number_of_bets_so_far:
            bet_size = self.wealth * self.fraction_to_bet
            self.wealth += -bet_size + round(bet_size * self.toss(), 2)
            change_wealth.append(self.wealth)
            i += 1
        dataframe = pd.DataFrame(change_wealth)
        return dataframe

    def martingale_bet(self):
        """
        You double the size of your stake every time you lose. Otherwise, you keep it constant.
        You can keep doing so, so long as your wealth has not hit zero, or you have not hit the bet limit.
        :return: list of the wealth sizes over the course of the betting
        """
        i = 0
        change_wealth = []
        bet_size = self.wealth * self.fraction_to_bet
        while self.wealth > 0 and i < self.number_of_bets_so_far:
            if self.toss() == 2:
                self.wealth += -bet_size + round(self.toss())
            else:
                self.wealth += -bet_size
                bet_size = bet_size * 2
            change_wealth.append(self.wealth)
        dataframe = pd.DataFrame(change_wealth)
        return dataframe


all_in = BettingStrategies(10000, 1).proportional_bets()
prop1 = BettingStrategies(10000, .1).proportional_bets()
prop2 = BettingStrategies(10000, .3).proportional_bets()
prop3 = BettingStrategies(10000, .6).proportional_bets()
prop4 = BettingStrategies(10000, .9).proportional_bets()
martingale = BettingStrategies(10000, .1).martingale_bet()
martingale2 = BettingStrategies(10000, .2).martingale_bet()
martingale3 = BettingStrategies(10000, .3).martingale_bet()
with pd.ExcelWriter('C:\\Users\\chris\\Documents\\Financial Independence\\exp.xlsx') as writer:
    all_in.to_excel(writer, 'all_in')
    prop1.to_excel(writer, 'prop1')
    prop2.to_excel(writer, 'prop2')
    prop3.to_excel(writer, 'prop3')
    prop4.to_excel(writer, 'prop4')
    martingale.to_excel(writer, 'martingale')
    martingale2.to_excel(writer, 'martingale2')
    martingale3.to_excel(writer, 'martingale3')
