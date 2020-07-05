while 1:

    menu = "What would you like to do? \n 1. Enter your ID number \n 2. Exit \n Enter an option."

    x = int(input(menu))
    
    if x == 1:
    
        parkrun_id = float(input("Enter the numerical part of your parkrun id (excluding the A prefix) "))

        if parkrun_id >= 0 and isinstance(parkrun_id, int):


            print("Hello")


        else:
            print("Not a valid input. Please enter your id.")

    elif x == 2:
        print("Good bye!")
        break
        
    else:
        print("Not a valid input. Try again.")
        

    