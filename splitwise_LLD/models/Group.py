class Group:

    def __init__(self):
        self.id=None
        self.name=None
        self.members=[]


    def setId(self,id):
        self.id=id

    def setName(self,name):
        self.name=name
    
    def setMembers(self,members):
        self.members=members
    
    def getId(self):
        return self.id
    
    def getName(self):
        return self.name
    
    def getMembers(self):
        return self.members