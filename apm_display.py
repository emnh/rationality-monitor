import pyautogui
import time
import tkinter as tk
import threading
from pynput import keyboard
from datetime import datetime

def get_stamp():
    return time.time()

last_alert = 0
# Assume recording started a minute ago?
buffer = [(time.time() - 60.0, None)]

def show_alert(message, timeout):
    root = tk.Tk()
    root.title("Alert")

    label = tk.Label(root, text=message)
    label.pack(padx=20, pady=20)

    # Close the window after the specified timeout
    root.after(timeout, root.destroy)

    root.mainloop()

def apm_check(key=None):
    global last_alert
    global buffer

    stamp = get_stamp()
    buffer.append((stamp, key))
    start_time = buffer[0][0]
    num_keys = 100
    window_len_s = 60
    keys_pressed = len([x for x in buffer if x[1] != None])
    # Calculate APM based on the number of keystrokes (customize this based on your needs)
    elapsed_time = stamp - start_time

    #if elapsed_time >= window_len_s:
    if elapsed_time > 0:
        apm = round(keys_pressed * 60 / elapsed_time)  # Calculate APM
        #start_time = time.time()  # Reset the start time

        first_not_2 = buffer[:-2]
        last_2 = buffer[-2:]
        new_buffer = [x for x in first_not_2 if stamp - x[0] <= window_len_s]
        new_buffer.extend(last_2)
        buffer = new_buffer
        #buffer = buffer[-num_keys:]

        try:
            # Print the key that was pressed
            pass
            #print(f'Key pressed: {key.char}')
        except AttributeError:
            # Handle special keys
            pass
            #print(f'Special key pressed: {key}')

        print("APM", apm, buffer[0], buffer[-1], len(buffer))
        dt_object = datetime.fromtimestamp(stamp)
        formatted_time = dt_object.strftime("%Y-%m-%d %H:%M:%S")
        logfile = open('log_of_apm.txt', 'a')
        logfile.write(str(formatted_time) + ", " + str(stamp) + ': ' + str(apm) + '\n')
        logfile.close()

        # Update the on-screen display
        #pyautogui.alert(text=f'APM: {apm}', title='APM Display', button='OK')

        alert_elapsed = time.time() - last_alert
        if alert_elapsed >= 5000:
            #show_alert("APM: " + str(apm), 1000)
            last_alert = time.time()

def on_press(key):
    apm_check(key)

def on_release(key):
    # If the key 'Esc' is pressed, stop the listener
    #if key == keyboard.Key.esc:
    #    return False
    pass

def regular():
    while True:
        #print('regular', buffer)
        apm_check()
        time.sleep(1)

threading.Thread(target=regular).start()

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
