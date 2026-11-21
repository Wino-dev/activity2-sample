class Wallet:
    def __init__(self, name, money, logs: list = []):
        self.name = name
        self.money = money
        self.logs = logs
        
    def add_money(self, source, amount):
        self.logs.append((source, amount))
        self.money += amount
        
    def spend_money(self, reason, amount):
        self.logs.append((reason, amount)),
        self.money -= amount