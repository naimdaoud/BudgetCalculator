class Category:
    def __init__(self, name, ledger):
        self.name = name
        self.ledger = ledger

    def Deposit (self, amount, description = None):
        dict = {}
        dict["amount"] = amount
        dict["description"] = description
        self.ledger.append(dict)

    def Withdraw (self, amount, description):
        res = sum([sum(list(sub.values())) for sub in self.ledger])
        if sum > amount:
            dict = {}
            dict["amount"] = -amount
            dict["description"] = description
            self.ledger.append(dict)
            return True
        return False

    def Display (self):
        print(self.ledger)


#def create_spend_chart(categories):


ledger = []
c = Category("Category1", ledger)
c.Deposit(100, "Food") 
c.Deposit(200, "Haircut")
c.Deposit(500, "Drink")
c.Withdraw(200,"Ret")
c.Display()