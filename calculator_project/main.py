import calculator

v1, v2 = 1
c1 = Calc(v1,v2)
main_menu = True

while True
    
    if main_menu:
        
        print("""Choose One
              * Add(1)
              * Multiply(2)
              * Subtract(3)
              * Division(4)
              * Exit(Q)
              """)
        main_menu = False
        
        selection = input("Select one: ")

        v1 = int(input("first value: "))
        v2 = int(input("second value: "))
        
    if selection == "1":
        add_result = c1.add()
        print("Add: {}". format(add_result))
        main_menu = True
        
    elif selection == "2":
        multiply_result = c1.multiply()
        print("Multiply: {}". format(multiply_result))
        main_menu = True
        
    elif selection == "3":
        subtract_result = c1.subtract()
        print("Subtract: {}". format(subtract_result))
        main_menu = True
        
    elif selection == "4":
        division_result = c1.division()
        print("Division: {}". format(division_result))
        main_menu = True
        
    elif selection == "Q" or selection == "q":
        break
    
    else:
        print("""
               Error there is no proper selection.
               Please Enter 1-4 or Q
               """)
        main_menu = True
        
        