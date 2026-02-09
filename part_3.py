speed = input("enter a speed between 0 and 100: ")

try:
    print(f"Speed set to {speed}")

except ValueError:
    print("Error: Corrupted Signal. Maintaining current speed.")

def get_coordinate():
    while True:
        try:
            x = int(input("what is the x coordinate: "))
            
            if x > 100 or x < -100 :
                print("Coordinate out of range")
            else:
                print(x)
                break

        except ValueError:
            print("Invalid coordinate")

get_coordinate()

