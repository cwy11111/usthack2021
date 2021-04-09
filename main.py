import csv
import time

def print2Dlist(thislist):        # print out the 2D line by line
    for row in thislist:
        print(row)

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
    print2Dlist(Menu)

    return Menu         
    #print(set(l1) & set(l2))

# this function define the dictionary that can access name of dishes by dish ID 
def defineDict(TodayMenu):
    theDict = {}
    for dish in TodayMenu:
        theDict[dish[0]] = dish[1]
    return theDict

# print the system selection menu and read the user input
def mainmenu():         
    print("***Main meun***\n1. Ordering\n2. Food availible today\n3. Queue\n4. Ordering history\n5. Quit")      # print mainmenu
    answer = input("What do you want to do ? (Enter 1 to 5)")               # seek user input
    
    while not(answer.isdigit()) or int(answer) < 1 or int(answer) > 5:       # validate the user input is a integer and check range
        answer = input("Invalid input.\nWhat do you want to do ? (Enter 1 to 5)")
    return answer

# print Food availible today
def printFood_available(dish_dict):
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
def order(orderedlist, TodayMenu):              # orderedlist is passed by reference
    global System_start_time                    # use the global variables
    global ID_to_name
    templist = ["orderID", "orderDishName" ,"orderTime" ]        # "initialize" the temp list
    order_food_ID = input("Enter the dish ID you want to order: ")
    order_time = time.time()                    # record the ordering time
    while not(dishExists(order_food_ID, TodayMenu)):         # validate the input, i.e. check if the input ID exists in the Menu
        print("Wrong input, please check food available today one more time before ordering. ")
        printFood_available(ID_to_name)              # print the Today Menu one more time for the user to check
        order_food_ID = input("Enter the dish ID you want to order: ")
        order_time = time.time()
        
    templist[0] = order_food_ID
    templist[1] = ID_to_name[order_food_ID]
    templist[2] = round(order_time - System_start_time, 2)
    orderedlist.append(templist)

    del templist        # release templist

# TODO
def queue(orderedlist):       # orderedlist is passed by reference
    return

# declare variable
TodayMenu = []             # a 2D list storing the menu
System_start_time = time.time()     # storing the time the system open
ordered_list = []           # a 2D list storing the order record
ID_to_name = {}             # a dictionary storing the name of dishes corresponding to each dish ID

# main program start

TodayMenu = readdata()                  # TodayMenu is the 2D list storing all dishes
ID_to_name = defineDict(TodayMenu)      # define the dish ID to name dictionary
response = mainmenu()                   # get the user response
while (response != '5'):

    if (response == '1'):       # TODO ordering section
        order(ordered_list, TodayMenu)
        print()

    elif (response == '2'):
        printFood_available(ID_to_name)
        print()

    elif (response == '4'):     # TODO ordering history
        if not ordered_list:    # if the list is empty
            print("There is currently no ordered history. ")
            print()
        else:
            print2Dlist(ordered_list)
            print()

    response = mainmenu()       # get the user response again
   
    