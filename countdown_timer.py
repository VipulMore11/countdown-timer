import time 

def countdown(t):       # Function to calculate the countdown
    while t:
        minutes = t // 60
        seconds = t % 60
        print("Time Left : {:02d}:{:02d}".format(minutes, seconds))
        time.sleep(1)
        t -= 1 
    print("Time's Up!!!!!!!")
    start()

def start():            # Function to take input from the user and start the countdown
    t = input("Enter time in seconds :")
    if t.isnumeric():
        countdown(int(t))
    else:
        print("Invalid Time")
        start()

start()                 # Function calling