# First of all I need to create a class that will initialize also a dictionay
# created using classe and PPO
class Budg_calculator :
    
    def __init__ (self, amount):
        self.available = amount # this is the initial amount
        self.budgets = {}
        self.expenditure = {}
        self.first_budget = amount  #added in order to offer a synthesis in the end
        
    def add_budget (self, name, amount):
        if name in  self.budgets : 
            raise ValueError("Already Existent Voice")
        if amount > self.available :
            raise ValueError("Non Sufficient Funds")
        self.budgets[name] = amount
        self.available -= amount
        self.expenditure[name] = 0 
        return self.available
     
    def spend (self, name, amount ):
        if name not in self.expenditure:
            print ("this voice is not admitted")
        self.expenditure[name] += amount 
        budgeted = self.budgets[name]
        spent = self.expenditure[name]
        return budgeted - spent 
        return self.expenditure # added 
    
    def print_summary (self): 
        print ("Budget" + " "*25 +        "Expected" + " "*25 +    "Spent" + " "*25 +    "Residual")
        print (" - - - - - - - - - - - - - - - - - - - - -")
        total_budgeted = 0
        total_spent = 0
        total_remaining = 0
        for name in self.budgets : 
            print (name + len("Budget")*" " + " "*(25-len(name))  + str((self.budgets[name]) )\
                   + len("Expected")*" " + 25 * " " + str(dispo.expenditure[name]) 
                   # here I have to calculate the residual as difference of
                   # budgets and expenditure 
                   + 25 * " " + str( self.budgets[name] - dispo.expenditure[name]  ))]
            
            total_spent += self.expenditure[name]
        print(" Initial budget: " +  str(self.first_budget ))
        print(" Effective expenses: " +  str(total_spent ) )
        print(" Savings: " + str(self.first_budget - total_spent) )