import os
import time
import pandas as pd
import pyttsx3
from datetime import datetime

def set_alarm(alarm_times, medicine_names):
    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        print(current_time)
        for idx, alarm_time in enumerate(alarm_times):
            if current_time == alarm_time:
                engine = pyttsx3.init()
                engine.say(f"It's time for your {medicine_names[idx]}")
                engine.runAndWait()
                os.system(f'python new.py "{medicine_names[idx]}"')  # Pass medicine name to new.py
                alarm_times.remove(alarm_time)  # Remove the triggered alarm
                medicine_names.pop(idx)  # Remove the corresponding medicine name
                break  # Break the loop after triggering one alarm

        if not alarm_times:
            print("All alarms have been triggered.")
            break
        time.sleep(1)

def get_alarm_times():
    excel_file = 'medicine_data.xlsx'
    df = pd.read_excel(excel_file)

    # Assuming 'Time' is the column name containing time data
    time_column = df['Time']
    medicine_column = df['Medicine Name']  # Assuming 'Medicine' is the column name for medicine names
    time_strings = []

    for i in time_column:
        time_obj = datetime.strptime(i, "%H:%M")
        HH = time_obj.hour
        MM = time_obj.minute
        time_string = f"{HH:02d}:{MM:02d}:00"
        time_strings.append(time_string)

    return time_strings, list(medicine_column)


def main():
    engine = pyttsx3.init()
    engine.say("Alarm")
    engine.runAndWait()
    alarm_times, medicine_names = get_alarm_times()
    set_alarm(alarm_times, medicine_names)

if __name__ == "__main__":
    main()
