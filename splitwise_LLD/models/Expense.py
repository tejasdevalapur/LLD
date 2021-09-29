class Expense:

    def __init__(self):
        self.id=None
        self.groupId=None
        self.amount=None
        self.contribution={}
        self.paidby={}

    
    def setId(self,id):
        self.id=id
    
    def setGroupId(self,groupId):
        self.group_id=groupId

    def setAmount(self,amount):
        self.amount=amount
    
    def setContribution(self,contribution):
        self.contribution=contribution

    def setPaidBy(self,paidby):
        self.paidby=paidby
    
    def getid(self):
        return self.id
    
    def getAmount(self):
        return self.amount

    def getContribution(self):
        return self.contribution
    
    def getPaidBy(self):
        return self.paidby