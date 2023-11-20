from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

myMenu=Menu()
myCoffeMachine=CoffeeMaker()
myMoneyMachine=MoneyMachine()
machineRuns=True
while machineRuns:
    userChoice=input(f'What do you want to drink? {myMenu.get_items()} : ')
    if userChoice=="report":
        myCoffeMachine.report()
        myMoneyMachine.report()
    elif userChoice=="off":
        machineRuns=False
    else:
        if myMenu.find_drink(userChoice)!=None:
            userItem=myMenu.find_drink(userChoice)
            machineRuns=False
            itemList=userItem.ingredients
            if myCoffeMachine.is_resource_sufficient(userItem):
                if myMoneyMachine.make_payment(userItem.cost):
                    myCoffeMachine.make_coffee(userItem)
        machineRuns=True





