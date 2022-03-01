# Calculation of Rental Income

from typing_extensions import Self


class Rental():
    def __init__(self):
        self.cost= 0 #user input 
        self.rentalincome = 0#user input
        self.improvements = 0 #user input
        self.cashflow = 0
        self.mortgage = 0 #user input
        self.repairs=0
        self.downpayment =self.cost*0.2 
        self.closingcosts = self.cost*0.03
        self.taxes = 0
        self.insurance = 0
        self.propertymangement = self.rentalincome*0.05

        


    def income (self):
        totalincome = self.rentalincome
        return totalincome


    def expenses (self):
        totalexpenses = self.taxes + self.insurance + self.repairs + self. propertymangement
        return totalexpenses

    def investment (self):
        totalinvestment = self. downpayment + self.improvements + self.closingcosts
        return totalinvestment

    def cashFlow(self):
        cashflow= Rental.income(self) - Rental.expenses(self)
        return cashflow

    def output(self):
        print(f"your cashflow is: {Rental.cashFlow(self)}")
        print(f"your ROI is: {round(Rental.ROI(self), 2)}")

    

    def getinputs(self):
        print("Thank you for your interest, Lets get started.")
        self.cost = int(input("How much is the property?"))
        self.rentalincome = int(input("What's the rental income?"))
        self.mortgage = int(input("How much is it to upgrade the property?"))

        Rental.output(self)

run = Rental()
run.getinputs()







       



  

   
