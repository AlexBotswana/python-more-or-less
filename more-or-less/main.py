import random

# Selection Menu
menu_number = -1
print("More or Less Game\n")
while menu_number == -1:
    test_menu_number = input("Select your level: \n1 - Number between 0 and 10 \n2 - Number between 0 and 100 \n3 - Number between 0 and 1000 \n0 - Exit\nLevel: ")
    try:
        int(test_menu_number)
        menu_number = int(test_menu_number)
        # random number calculated by computer
        good_number = -1
        if menu_number == 1:
            good_number = random.randint(0, 10)
        elif menu_number == 2:
            good_number = random.randint(0, 100)
        elif menu_number == 3:
            good_number = random.randint(0, 1000)
        elif menu_number == 0:
            good_number = -1
        else:
            menu_number = -1
            print("\nPlease select 1, 2, 3 or 0\n")
    except ValueError:
            menu_number = -1
            print("\nPlease select 1, 2, 3 or 0\n")

test = -1
try_number = 0

# Wrong number (repeat until ok)
while test != good_number:

    # request the number
    test = int(input("Enter your number: "))

    # if to small answer more
    if test < good_number:
        print("The number is bigger than ",test)
    # if to big answer less
    if test > good_number:
        print("The number is smaller than ",test)
    
    # Number of try
    try_number = try_number + 1
# good number
if good_number != -1:
    print(test," is the good number! you succeed in ",try_number," times")
