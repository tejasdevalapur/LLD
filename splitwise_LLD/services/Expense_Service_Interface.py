import abc

class ExpenseServiceInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def addExpense(self,id,groupId,amount,contribution,paidby):
        pass

