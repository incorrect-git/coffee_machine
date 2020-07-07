class PiggyBank:
    # create __init__ and add_money methods
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents
        self.added_dollars = 0

    def add_money(self, deposit_dollars, deposit_cents):
        # self.cents += deposit_cents if self.cents + deposit_dollars < 100 else self.cents + deposit_dollars - 100
        self.cents += deposit_cents
        self.added_dollars = 0
        if self.cents > 99:
            self.added_dollars = self.cents // 100
            self.cents %= 100

        self.dollars += deposit_dollars + self.added_dollars
