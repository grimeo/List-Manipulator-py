# Write a python program that do the following:

# - display the initial content of the array
# - display a menu of options
# - allow user to select item in the menu (check if valid)
# - perform the selected option (you may prompt additional info to user when need)
# - display the resulting values of the array


# Note: 
# - The program has an array variable containing 10 random numbers
# - You may add other options and features
# - Your program should be uploaded to github before 9:00pm
# - Record a demo presenting your program
# - Send the demo directly to my messenger

# Example Output:

# Array: [1, 4, 3, 4, 4, 5, 6 ,2 ,56, 200]
# Menu:
#  1 -> Add an element
#  2 -> Insert an element
#  3 -> Modify an element
#  4 -> Delete an element
#  5 -> Arrange in ascending order
#  6 -> Arrange in descending order
# What do you want to do? (1-6): 4
# Enter the index you want to delete: 3
# The element has been deleted
# This is the new array: Array: [1, 4, 3, 4, 5, 6 ,2 ,56, 200]

import random
import sys

list1 = []
for x in range(10):
    list1.append(random.randint(0, 100))

def add(value):
    list1.append(value)
    print("The updated list: ")
    print(list1)

def insert(n, value):
    list1.insert(n, value)
    print("The updated list: ")
    print(list1)

def modify(n, value):
    list1[n] = value
    print(list1)

def delete(value):
    list1.remove(value)
    print("The updated list: ")
    print(list1)

def arrangeAsc():
    list1.sort()
    print("The updated list: ")
    print(list1)

def arrangeDesc():
    list1.sort()
    list1.reverse()
    print("The updated list: ")
    print(list1)


#-----------------MAIN-----------------#

print("\n\nThe content of the list :")
print(list1)
print("\nMenu: " 
    + "\n 1 -> Add an item"              ###################
    + "\n 2 -> Insert an item"           ###################
    + "\n 3 -> Change the item"           
    + "\n 4 -> Delete an item"           ###################
    + "\n 5 -> Arrange in ascending order"  ###################
    + "\n 6 -> Arrange in descending order" ###################
    + "\n Type 'x' or 'X' to exit"
    )
while(1==1):
    userInput = input("\nType the option: ")

    if(userInput == "1"):
        value = input("\nType the item to add: ")
        add(int(value))
        
    elif(userInput == "2"):
        ind = input("Type the index here: ")
        value = input("Type the item here: ")
        insert(int(ind), int(value))
        
    elif(userInput == "3"):
        itemtoChange = input("Type the item to change: ")
        newValue = input("Type the new item here: ")
        i = list1.index(int(itemtoChange))
        modify(i, int(newValue))
        
    elif(userInput == "4"):
        value = input("Type the item to remove: ")
        delete(int(value))
        
    elif(userInput == "5"):
        arrangeAsc()
        
    elif(userInput == "6"):
        arrangeDesc()
        
    elif(userInput == "x" or userInput == "X"):
        sys.exit("\nThank you for using the machine!\nGoodbye!\n")
        
    else:
        sys.exit("could not perform the operation. Please type the valid option.")
