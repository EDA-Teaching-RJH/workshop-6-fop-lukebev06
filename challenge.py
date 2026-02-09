status = {"Power": 100, "Samples": 0}
inventory = []

while True:
    print("---Menu---")
    print("1. Dig for sample")
    print("2. Report status")
    print("3. Emergency stop")
    option = int(input("menu button: "))

    if option == 1 :
        
        sample = input("what is the sample collected? ")
        inventory.append(sample)
        status["Power"] = status["Power"] - 10
        
    elif option == 2 :

        print(status)
        print(inventory)

    elif option == 3 :

        break

    else:
        print("That isnt a valid menu option")
