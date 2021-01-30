# dummy external payment service
from PremiumPaymentGateway import PremiumPaymentGateway
from ExpensivePaymentGateway import ExpensivePaymentGateway
from CheapPaymentGateway import CheapPaymentGateway


class PaymentGateway():

    # constructor
    def __init__(self, amount):
        self.amount = amount
    
    # method to process a transaction with logic
    def processPayment(self):
        if (amount>500):
            processPremiumPayment(self.amount,0)
        elif (amount>20):
            processExpensivePayment(self.amount,0)
        else:
            processCheapPayment(self.amount)

def processPremiumPayment(amount, retryCount):
    if(retryCount>2):
        PremiumPaymentGateway.process(amount)
    try:
        if(PremiumPaymentGateway.process(amount)): #returns true on successful payment otherwise throws error
            return
    except:
        processPremiumPayment(amount, retryCount+1)

def processExpensivePayment(amount, retryCount):
    if(retryCount>1):
        ExpensivePaymentGateway.process(amount)
    try:
        if(ExpensivePaymentGateway.process(amount)): #returns true on successful payment otherwise throws error
            return
    except:
        processExpensivePayment(amount, retryCount+1)

def processCheapPayment(amount):
    PremiumPaymentGateway.process(amount) #returns true on successful payment otherwise throws error
        
