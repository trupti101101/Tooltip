import time
import winsound

def countdown_timer(hours, minutes, seconds):
    total_seconds = hours * 3600 + minutes * 60 + seconds

    while total_seconds:
        mins, secs = divmod(total_seconds, 60)
        hours, mins = divmod(mins, 60)
        timer = f'{hours:02d}:{mins:02d}:{secs:02d}'
        print(timer, end="\r")
        time.sleep(1)
        total_seconds -= 1

    print("\nTime's up!")
    # Play sound when the timer ends
    winsound.Beep(1000, 1000)  # Beep at 1000 Hz for 1000 ms (1 second)
    print("Thank you for using the timer.")

if __name__ == "__main__":
    print("\n==| Welcome To The 'Timer App' |==")
    try:
        hours = int(input("Enter the number of hours: "))
        minutes = int(input("Enter the number of minutes: "))
        seconds = int(input("Enter the number of seconds: "))
        
        countdown_timer(hours, minutes, seconds)
    except ValueError:
        print("Invalid input. Please enter an integer value.")
