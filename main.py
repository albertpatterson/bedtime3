from tkinter import *
import time
from bedtime_tracker import BedtimeTracker
from datetime import datetime
import screeninfo

now = datetime.now()


bedtime_hour = 0
bedtime_minute = 0
morning_hour = 8
morning_minute = 0

snooze_ms = 5 * 60 * 1000


def get_geometry_str(x):   
    return f'+{x}'

class BedtimeWindowManager:

    def __init__(self, bedtime_hour, bedtime_minute, morning_hour, morning_minute):
        self._snoozed = False

        self._tracker = BedtimeTracker(
            bedtime_hour=bedtime_hour,
            bedtime_minute=bedtime_minute,
            morning_hour=morning_hour,
            morning_minute=morning_minute,
        )

        primary_window_info, additional_windows_info = self._get_window_info()
        self._primary_window_info = primary_window_info
        self._additional_windows_info = additional_windows_info

        self._unsnooze()

        print(self._get_all_window_info())

        self._primary_window_info["window"].mainloop()

    def _get_all_window_info(self):
        return [self._primary_window_info, *self._additional_windows_info]
    
    def _is_state_normal(self):
        for window_info in self._get_all_window_info():
            window = window_info['window']
            
            current_state = window.wm_state()

            is_normal = "normal" in current_state or "zoomed" in current_state
            if not is_normal:
                return False
        
        return True

    def _update(self):
        print("update")

        if self._snoozed:
            print("pass update")
            return

        if self._tracker.is_bed_time():
            state_is_normal = self._is_state_normal()
            if not state_is_normal:
                self._snooze()
            else:
                message = self._get_bedtime_message()
                for window_info in self._get_all_window_info():
                    label = window_info['label']
                    label.config(text=message)
                    window_info['window'].attributes("-topmost", True)
                    
            self._schedule_update()
            
        else:
            snooze_ms = round(1000 * self._tracker.time_until_bed().total_seconds())
            self._snooze(snooze_ms)
    
    def _schedule_update(self):
        self._primary_window_info['window'].after(1000, lambda: self._update())
        
    def _snooze(self, snooze_time=snooze_ms):
        print(f"snooze for {snooze_time}")

        self._snoozed = True

        for window_info in self._get_all_window_info():
            window_info["window"].state("iconic")

        self._primary_window_info["window"].after(snooze_time, lambda: self._unsnooze())

    def _unsnooze(self):
        print('unsnooze')
    
        for window_info in self._get_all_window_info():
            window = window_info['window']
            window.state("zoomed")
            x_goemetry_str = get_geometry_str(window_info['x'])
            y_goemetry_str = get_geometry_str(window_info['y'])
            
            display_geometry = f"{window_info["width"]}x{window_info["height"]}{x_goemetry_str}{y_goemetry_str}"
            print(display_geometry)
            window.geometry(display_geometry)

        self._update()

    def _get_bedtime_message(self):
        current_time = time.strftime("%H:%M:%S")
        return f"It's time for bed: {current_time}"

    def _get_window_info(self):
        primary_monitor, additional_monitors = self._get_monitors()
        primary_window_info = self._create_window_with_info(
            True,
            primary_monitor.x,
            primary_monitor.y,
            primary_monitor.height,
            primary_monitor.width,
        )

        additional_windows_info = [
            self._create_window_with_info(
                False,
                m.x,
                m.y,
                m.height,
                m.width,
            )
            for m in additional_monitors
        ]

        return primary_window_info, additional_windows_info

    def _create_window_with_info(self, is_primary, x, y, height, width):
        window, label = self._create_window(is_primary)
        return dict(window=window, label=label, x=x, y=y, height=height, width=width)

    def _create_window(self, is_primary):
        if is_primary:
            window = Tk()
        else:
            window = Toplevel()

        window.title("Bedtime")
        label = Label(window, font=("Arial", 50), text=self._get_bedtime_message())
        label.pack()

        window.protocol("WM_DELETE_WINDOW", lambda: self._snooze())

        return window, label

    def _get_monitors(self):
        monitors = screeninfo.get_monitors()
        primary_monitor = None
        additional_monitors = []
        for monitor in monitors:
            if monitor.is_primary:
                if primary_monitor is not None:
                    raise Exception("found multiple primary monitors")

                primary_monitor = monitor
            else:
                additional_monitors.append(monitor)

        if primary_monitor is None:
            raise Exception("failed to find primary monitor")

        # screeninfo is relative to the bottom left corner, we need to use the top left corner with tkinter
        for monitor in additional_monitors:
            monitor.y -= monitor.height
            
        primary_monitor.y = 0
            
        return primary_monitor, additional_monitors


btwm = BedtimeWindowManager(bedtime_hour, bedtime_minute, morning_hour, morning_minute)
