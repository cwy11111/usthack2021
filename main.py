import csv
import time
from datetime import timedelta

def print2Dlist(thislist, spacing):        # print out the 2D line by line
    s = spacing * ' '
    for row in thislist:
        print(*row, sep=s)
            #print('{:<{length}}'.format(item, length= len(str(item))*2+1) , end='')               

def readdata():         # this function tidy up the list read from csv and return the whole list
  with open(r"data\usthackcsv.csv", newline='', encoding="utf-8") as csvfile:
    rows = csv.reader(csvfile)                  # read the csvfile as a 2D list
    #rowsDict = csv.DictReader(csvfile)          # read the csvfile as a Dictionary (on9)
    l0 = list(rows)       # make it a list first
    Menu = []             # 2D list storing all data without empty reduntant cell

    # strip off the empty cell and the first row (column title)
    for i in range(1, len(l0)):
        l2 = []             # temp 1D list for l1
        for j in range(len(l0[i])):
            if l0[i][j] != "":
                l2.append(l0[i][j])
        Menu.append(l2)

    del l2      # release the temp list

    # print the whole Menu out once
    print2Dlist(Menu,2)

    return Menu         

# customize setting
def customize():        
    global Max_WaitTime_EachDish    
    global Number_of_chef
    # ask about maximum waiting time of each dish
    answer = input("Enter the maximum waiting time of each unserved dish (in minutes): ")
    while not(answer.isdigit()) or int(answer) <0:           # validate the user input 
        answer = input("Please enter a valid number (in minutes): ")
    answer = int(answer)
    Max_WaitTime_EachDish = answer * 60         # change the unit of the value into seconds

    # ask about number of dish being prepared at the same time aka number of chef
    answer = input("Enter the number of dish(es) can be prepared at the same time: ")
    while not(answer.isdigit()) or int(answer) <1:           # validate the user input 
        answer = input("Please enter a valid number: ")
    answer = int(answer)
    Number_of_chef = answer
    print()

# this function define the dictionary that can access name of dishes by dish ID 
def defineDict(TodayMenu):
    theDict = {}
    for dish in TodayMenu:
        theDict[dish[0]] = dish[1]
    return theDict

# print the system selection menu and read the user input
def mainmenu():         
    print("***Main meun***\n1. Make order\n2. Food availible today\n3. Queue\n4. Show unserved dish\n5. Update unserved dish\n6. Order history\n7. Quit")      # print mainmenu
    answer = input("What do you want to do ? (Enter 1 to 7) ")               # seek user input
    
    while not(answer.isdigit()) or int(answer) < 1 or int(answer) > 7:       # validate the user input is a integer and check range
        answer = input("Invalid input.\nWhat do you want to do ? (Enter 1 to 7) ")
    return answer

# print Food availible today
def printFood_available(dish_dict):
    print("The food provided are following: ")
    for item in dish_dict.keys():
        print(item , ':', dish_dict[item] , end=' ', sep='' )
    print()

# search the target dish ID in the 2D list and return a boolean (return true if the target dish ID exists in the Menu)
def dishExists(targetID, TodayMenu):
    for dish in TodayMenu:
        if targetID == dish[0]:
            return True
    return False

# temp ordering function for queue
def order(orderedlist, OrderedHistory, TodayMenu, orderID):              # orderedlist and orderedHistory is passed by reference
    global System_start_time                    # use the global variables
    global ID_to_name
    templist = ["orderID", "dishID", "orderDishName" ,"orderTime", "remainTime"]     # "initialize" the temp list; structure of the ordered_list
    order_food_ID = input("Enter the dish ID you want to order: ")
    order_time = time.time()                    # record the ordering time
    while not(dishExists(order_food_ID, TodayMenu)):         # validate the input, i.e. check if the input ID exists in the Menu
        print("Wrong input, please check food available today one more time before ordering. ")
        printFood_available(ID_to_name)         # print the Today Menu one more time for the user to check
        order_food_ID = input("Enter the dish ID you want to order: ")
        order_time = time.time()
    
    templist[0] = orderID    
    templist[1] = order_food_ID
    templist[2] = ID_to_name[order_food_ID]
    templist[3] = timedelta(seconds = int(order_time - System_start_time))            # Trans to date time format, i.e. hour: minute: second
    #templist[3] = round((order_time - System_start_time) / 60, 2)              
    # search the required expected time as initial value of remainTime
    for dish in TodayMenu:
        if dish[0] == order_food_ID:
            templist[4] = int(dish[3]) * 60

    orderedlist.append(templist)                 
    OrderedHistory.append(templist[:4])                 # the orderedHistory does not need the field "remainTime"

    del templist        # release templist

def showOrderedList(orderedlist):          # print out all the dishes that are unserved
    if not orderedlist:                     # check if the unservedlist is empty
        print("There is currently no unserved dish. ")
    else:
        print("\nID " , "Dish-ID " ,"Dish-Name " , " Order-At " , "Pre-Time(second) ")
        print2Dlist(orderedlist,6)

def showOrderedHistory(orderedlist):          # print out all the dishes history
    if not orderedlist:                     # check if the list is empty
        print("There is currently no order history. ")
    else:
        print("\nID " , "Dish-ID " ,"Dish-Name " , " Order-At " )
        print2Dlist(orderedlist,6) 

def updateUnservedList_Manual(orderedlist):    # update the list manually
    if not orderedlist:
        print("There is currently no unserved dish. ")
        return          # return the function if the orderedlist is empty

    print2Dlist(orderedlist,5)
    target_ID = input("Which order do you want to remove? (Enter the order ID from 1 to {boundary}) ".format(boundary=len(orderedlist)) ) 
    while not(target_ID.isdigit()) or int(target_ID) < 1 or int(target_ID) > len(orderedlist):              # validate the user input
        target_ID = input(("Invalid input. Please input again with range 1 to {boundary} : ".format(boundary=len(orderedlist))))
        
    target_ID = int(target_ID)
    for order in orderedlist:
        if order[0] == target_ID:
            orderedlist.remove(order)
            print("Order" , target_ID ,"is successfully removed from the unserved order list. The list becomes: ")
            if not orderedlist:                         # if the list become empty after removal
                print("The list is currently empty. ")
            else:
                print2Dlist(orderedlist,5)

def findIndex(dish_name, TodayMenu):            # find the index of the dish in the TodayMenu list
    for i in range(len(TodayMenu)):
        if TodayMenu[i][1] == dish_name:
            return i

# queue the unserved list 
# Objective: Group the similar dish together in the unserved order list 
def queue(orderedlist,TodayMenu):       

    # add a new field to all order for the "similarity" scores counting
    for order in orderedlist:           
        order.append(0)             
    
    # calculate the similarity
    for orderToCal in orderedlist:               
        for eachOrder in orderedlist:
            if orderToCal != eachOrder:
                index_of_ToCal = findIndex(orderToCal[2], TodayMenu)
                index_of_Each = findIndex(eachOrder[2], TodayMenu)
                if TodayMenu[index_of_ToCal][2] == TodayMenu[index_of_Each][2]:             # increase the similarity by 3 if they have same cooking method
                    orderToCal[5] +=3
                # increase the similarity by 1 for each similar cooking ingredient
                orderToCal[5] += len(set(TodayMenu[index_of_ToCal][4:] ) & set(TodayMenu[index_of_Each][4:] ))
                
    orderedlist.sort( key = lambda l:l[5], reverse=True)            # sort the 2D order list by the similarity by descending order
    for order in orderedlist:           
        del order[5]    
    
    print("\nThe list is re-ordered as following: ")
    showOrderedList(orderedlist)

# declare variable
TodayMenu = []             # a 2D list storing the whole menu (with all informations)
System_start_time = time.time()     # storing the time the system open
ordered_list = []             # a 2D list storing the unserved dishes
ordered_history = []          # a 2D list storing the order record
ID_to_name = {}               # a dictionary storing the name of dishes corresponding to each dish ID
Max_WaitTime_EachDish = 900   # initialize the maximum waiting time of each dish as 15 mins (900s), ignore it if the preparation time is longer
Number_of_chef = 1            # initialize the number of dish being prepared at the same time  
orderNumber = 0                  # The number N : N-th order

# main program start

TodayMenu = readdata()                  # TodayMenu is the 2D list storing all dishes
ID_to_name = defineDict(TodayMenu)      # define the dish ID to name dictionary
#customize()                             # ask the user about some values of pre-load variables
response = mainmenu()                   # get the user response
while (response != '7'):

    if (response == '1'):       # ordering section
        orderNumber +=1
        order(ordered_list, ordered_history, TodayMenu, orderNumber)

    elif (response == '2'):     # show the food and ID 
        printFood_available(ID_to_name)

    elif (response == '3'):      # queue
        queue(ordered_list,TodayMenu)

    elif (response == '4'):     # show unserved order-list
        showOrderedList(ordered_list)

    elif (response == '5'):     # update the unserved order-list manually
        updateUnservedList_Manual(ordered_list)

    elif (response == '6'):     # ordering history
       showOrderedHistory(ordered_history)
    
    

    print()
    response = mainmenu()       # get the user response again
    