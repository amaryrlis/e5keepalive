import time
import winsound

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer_display = f'{mins:02d}:{secs:02d}'
        print(timer_display, end='\r')
        time.sleep(1)
        seconds -= 1
    
    print("Time's up!")
    winsound.Beep(1000, 1000)  # Beep sound to signal the end of the timer

if __name__ == "__main__":
    try:
        minutes = int(input("Enter the focus time in minutes: "))
        print(f"Focus timer set for {minutes} minutes.")
        focus_timer(minutes)
    except ValueError:
        print("Invalid input. Please enter a valid number of minutes.")
