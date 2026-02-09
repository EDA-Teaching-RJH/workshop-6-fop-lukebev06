travel_log = []

while True:
    try:
        reading = int(input("Sensor reading (Slope Angle): "))

        if reading >45 :
            print("CRITICAL TILT! HALTING.")
            break
            
        else:
            travel_log.append(reading)
            print("Path stable. Moving forward.")


    except ValueError:
        print("Sensor Glitch")

print("Mission Terminated.")
print(f"Total steps taken: {len(travel_log)}")
print(travel_log)
