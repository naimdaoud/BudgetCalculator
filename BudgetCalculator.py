class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        res = (self.name.center(30,"*")) + "\n"
        for k in self.ledger:
            res = res + (str(k["description"]).ljust(23)[:23] + str("{:.2f}".format(k["amount"])).rjust(7)[:7]) + "\n"
        res = res + ("Total: " + str("{:.2f}".format(self.get_balance())))
        return res

    def deposit (self, amount, description = None):
        dict = {}
        dict["amount"] = amount
        if description == None:
            description = ""
        dict["description"] = description
        self.ledger.append(dict)

    def withdraw (self, amount, description = None):
        if self.check_funds(amount):
            dict = {}
            dict["amount"] = -amount
            if description == None:
                description = ""
            dict["description"] = description
            self.ledger.append(dict)
            return True
        return False

    def get_balance (self):
        res = 0
        for sub in self.ledger:
            for key in sub:
                if key == "amount":
                    res += sub["amount"]
        return res

    def transfer (self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount,"Transfer to " + category.name)
            category.deposit(amount, "Transfer from " + self.name)
            return True
        return False

    def check_funds(self, amount):
        res = self.get_balance()

        if amount > res:
            return False
        return True

def create_spend_chart(categories):
    graph = "Percentage spent by category"
    res = 0
    l = []
    for cat in categories:
        for sub in cat.ledger:
            for key in sub:
                if key == "amount" and sub["amount"] < 0:
                    res += abs(sub["amount"])
        ratio = res / cat.get_balance() * 100
        res = 0
        l.append(round(ratio,-1))
    #add top part of graph
    for i in range(11):
        graph = graph + "\n" + (str(100-10*i)).rjust(3) +"|"
        for j in l:
            if j>=(100-10*i):
                graph = graph + " o "
            else:
                graph = graph + "   "
    graph = graph + " "
    graph = graph + "\n" +"    "+ len(categories)*3*"-" + "-" +"\n"

    #find longest word
    maxlen = ""
    for i in categories:
        if len(i.name) > len(maxlen): 
            maxlen = i.name
  
    #print the categories
    for j in range(len(maxlen)):
        graph  = graph + "     "
        for i in categories:
            try:
                graph = graph + i.name[j] + "  "
            except:
                graph = graph + "   "
        graph = graph + "\n"
    graph = graph[:-1]
  
    return graph  


food = Category("food")
entertainment = Category("entertainment")
business = Category("business")
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)

print(create_spend_chart([business, food, entertainment]))