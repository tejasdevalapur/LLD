

from services.ExpenseService import ExpenseService
from services.GroupService import GroupService
from services.UserService import UserService
from controllers.UserController import UserController
from controllers.GroupController import GroupController
from controllers.ExpenseController import ExpenseController



userController=UserController(UserService())
groupController=GroupController(GroupService())
expenseController=ExpenseController(ExpenseService())


user1=userController.addUser('user1','Tom')
user2=userController.addUser('user2','John')
user3=userController.addUser('user3','Tim')
user4=userController.addUser('user4','Andrew')
user5=userController.addUser('user5','Ken')


members=[user1,user2,user3,user4,user5]
group1=groupController.addGroup('group1','avengers',members)

paidBy={'user1':200, 'user2':100, 'user3':50, 'user4':50,'user5':100}
contribution={'user1':100, 'user2':100, 'user3':100, 'user4':100,'user5':100}

expense=expenseController.addExpense('bill1','group1',500,contribution,paidBy)


balance=expenseController.getUserBalance('user1')

print(balance)