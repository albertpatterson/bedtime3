from tkinter import *
import time
from bedtime_tracker import BedtimeTracker


bedtime_hour = 0
bedtime_minute = 0
morning_hour = 8
morning_minute = 0

snooze_ms = 5 * 60 * 1000

tracker = BedtimeTracker(
    bedtime_hour=bedtime_hour,
    bedtime_minute=bedtime_minute,
    morning_hour=morning_hour,
    morning_minute=morning_minute,
)


def get_bedtime_message():
    current_time = time.strftime("%H:%M:%S")
    return f"It's time for bed: {current_time}"


def is_state_normal(root):
    current_state = root.wm_state()
    return "normal" in current_state or "zoomed" in current_state


def update(root, label):
    if tracker.is_bed_time():
        message = get_bedtime_message()
        label.config(text=message)
        state_is_normal = is_state_normal(root)
        if not state_is_normal:
            snooze(root, label)
        else:
            schedule_update(root, label)
    else:
        snooze(root, label, round(1000 * tracker.time_until_bed().total_seconds()))


def schedule_update(root, label):
    root.after(1000, lambda: update(root, label))


def snooze(root, label, snooze_time=snooze_ms):
    root.geometry("0x0")
    root.after(snooze_time, lambda: unsnooze(root, label))


def unsnooze(root, label):
    root.state("normal")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    display_geometry = f"{screen_width}x{screen_height}+0+0"

    root.geometry(display_geometry)
    update(root, label)


def handle_close(root, label):
    snooze(root, label)


root = Tk()
root.title("Bedtime")
label = Label(root, font=("Arial", 50), text=get_bedtime_message())
label.pack()

root.protocol("WM_DELETE_WINDOW", lambda: handle_close(root, label))
unsnooze(root, label)

root.mainloop()
