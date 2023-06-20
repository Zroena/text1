import time

def start_focus_timer(minutes):
    seconds = minutes * 60
    end_time = time.time() + seconds

    print(f"Focus timer set for {minutes} minutes.")

    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        minutes = remaining_time // 60
        seconds = remaining_time % 60
        print(f"Time remaining: {minutes:02d}:{seconds:02d}", end="\r")
        time.sleep(1)

    print("Focus timer complete!")

# 设置专注时钟为25分钟
start_focus_timer(25)
