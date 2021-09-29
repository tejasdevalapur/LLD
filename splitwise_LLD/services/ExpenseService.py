
from services.Expense_Service_Interface import ExpenseServiceInterface
from models.Expense import Expense


class ExpenseService(ExpenseServiceInterface):
    billDetails={}
    def addExpense(self,id,groupId,amount,contribution,paidby):
        exp=Expense()
        exp.setId(id)
        exp.setGroupId(groupId)
        exp.setAmount(amount)
        exp.setContribution(contribution)
        exp.setPaidBy(paidby)
        self.__class__.billDetails[id]=exp
        return exp




