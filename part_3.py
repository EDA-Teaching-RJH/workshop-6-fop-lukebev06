speed = input("enter a speed between 0 and 100")

try:
    print(f"Speed set to {speed}")
except ValueError:
    print("Error: Corrupted Signal. Maintaining current speed.")
