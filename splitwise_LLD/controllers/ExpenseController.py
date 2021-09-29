


class ExpenseController:

    def __init__(self,expenseService):
        self.expenseService = expenseService

    
    def addExpense(self,id,group_id,amount,contribution,paidby):
        return self.expenseService.addExpense(id,group_id,amount,contribution,paidby)


    def getUserBalance(self,userId):
        balance=0

        for expId in self.expenseService.billDetails:
            bill=self.expenseService.billDetails.get(expId)

            if userId in bill.getContribution():
                balance-=bill.getContribution().get(userId)

            if userId in bill.getPaidBy():
                balance+=bill.getPaidBy().get(userId)

        return balance


        
			