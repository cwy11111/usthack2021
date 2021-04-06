import csv

def readdata():         # this function tidy up the list read from csv and return the whole list
  with open(r"data\usthackcsv.csv", newline='', encoding="utf-8") as csvfile:
    rows = csv.reader(csvfile)                  # read the csvfile as a 2D list
    #rowsDict = csv.DictReader(csvfile)          # read the csvfile as a Dictionary (on9)
    l0 = list(rows)       # make it a list first
    Menu = []             # 2D list storing all data without empty reduntant cell
    

    # strip off the empty cell
    for i in range(len(l0)):
        l2 = []             # temp 1D list for l1
        for j in range(len(l0[i])):
            if l0[i][j] != "":
                l2.append(l0[i][j])
        Menu.append(l2)

    # print the whole Menu out once
    for row in Menu:
        print(row)

    return Menu         
    #print(set(l1) & set(l2))

# print the system selection menu and read the user input
def mainmenu():         
    print("***Main meun***\n1. Ordering\n2. Food availible today\n3. Quene\n4. Ordering history\n5. Quit")      # print mainmenu
    answer = input("What do you want to do ? (Enter 1 to 5)")               # seek user input
    
    while not(answer.isdigit()) or int(answer) < 1 or int(answer) > 5:       # check if the user input is a integer and check range
        answer = input("Invalid input.\nWhat do you want to do ? (Enter 1 to 5)")
    return answer

# print Food availible today
def printFood_available(TodayMenu):
    for i in range(1, len(TodayMenu)):          # start printing out from second row (first row is the column label)
        print(TodayMenu[i][1] , end=' ')
    print()

# declare variable
TodayMenu = []             # a 2D list storing the menu

# main program start

TodayMenu = readdata()
response = mainmenu()       # get the user response
while (response != '5'):

    #if (response == '1'):       # TODO ordering section
        
    if (response == '2'):
        printFood_available(TodayMenu)

    response = mainmenu()       # get the user response again
   
    