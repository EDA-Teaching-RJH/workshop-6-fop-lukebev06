rover_status = {
    "Battery": 100,
    "Heater": "off",
    "Camera": "standby"
    
    }


print(rover_status["Battery"])

rover_status["Battery"] = 85
rover_status["Heater"] ="on"

rover_status["Speed"] = 5

print(rover_status)
