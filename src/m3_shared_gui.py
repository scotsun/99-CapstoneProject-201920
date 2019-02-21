""" This is a document similar to that of the shared gui that we used
for sprint one and two. It will be where I construct all my frames for the final
"""

import tkinter
from tkinter import ttk
import time

# Space for the frames

"""Frame for the sleep uses radio buttons to use a new type of button"""
def frame_for_sleep(frame, mqtt_sender):
    frame_sleep = ttk.Frame(frame, padding=10, borderwidth=10, relief="ridge")
    frame_sleep_label = ttk.Label(frame_sleep, text="Sleep Frame")
    frame_sleep.grid()

    ask_to_sleep_button = ttk.Button(frame_sleep, text="Do you want to sleep baby?")
    how_long_label = ttk.Label(frame_sleep, text="How long do you want the baby to sleep for?")
    radio_1 = ttk.Radiobutton(frame_sleep, text=0, value=0)
    radio_2 = ttk.Radiobutton(frame_sleep, text=3, value=3)
    radio_3 = ttk.Radiobutton(frame_sleep, text=6, value=6)
    radio_4 = ttk.Radiobutton(frame_sleep, text=9, value=9)
    radio_5 = ttk.Radiobutton(frame_sleep, text=12, value=12)

    ask_to_sleep_button.grid(row=1, column=0)
    frame_sleep_label.grid(row=0, column=1)
    how_long_label.grid(row=1, column=2)
    radio_1.grid(row=2, column=3)
    radio_2.grid(row=2, column=4)
    radio_3.grid(row=2, column=5)
    radio_4.grid(row=2, column=6)
    radio_5.grid(row=2, column=7)


    radio_observer = tkinter.StringVar()
    for radio in [radio_1, radio_2, radio_3, radio_4, radio_5]:
        radio['variable'] = radio_observer

    ask_to_sleep_button["command"] = lambda: handle_sleep(radio_observer, mqtt_sender)

    return frame


""""Frame for crawl using typical buttons"""


def frame_for_crawl(frame, mqtt_sender):
    frame_crawl = ttk.Frame(frame, padding=10, borderwidth=10, relief="ridge")
    frame_crawl_label = ttk.Label(frame_crawl, text="Crawl Frame")
    frame_crawl.grid()

    crawl_button = ttk.Button(frame_crawl, text="Crawl")
    speed_label = ttk.Label(frame_crawl, text="Speed")
    speed_entry = ttk.Entry(frame_crawl, width=8)
    color_label = ttk.Label(frame_crawl, text="Color")
    color_entry = ttk.Entry(frame_crawl, width=8)

    frame_crawl_label.grid(row=0, column=1)
    crawl_button.grid(row=1, column=0)
    speed_label.grid(row=3, column=0)
    speed_entry.grid(row=4, column=0)
    color_label.grid(row=3, column=2)
    color_entry.grid(row=4, column=2)

    crawl_button["command"] = lambda: handle_crawl(color_entry, speed_entry, mqtt_sender)

    return frame


"""Frame for cry using typical buttons"""
def frame_for_cry(frame, mqtt_sender):
    frame_cry = ttk.Frame(frame, padding=10, borderwidth=10, relief="ridge")
    frame_cry_label = ttk.Label(frame_cry, text="Cry Frame")
    frame_cry.grid()

    cry_button = ttk.Button(frame_cry, text="Cry")
    how_long_label = ttk.Label(frame_cry, text="Cry for ")
    how_long_entry = ttk.Entry(frame_cry, width=8)

    frame_cry_label.grid(row=0, column=1)
    cry_button.grid(row=1, column=0)
    how_long_label.grid(row=1, column=2)
    how_long_entry.grid(row=2, column=2)

    cry_button["command"] = lambda: handle_cry(how_long_entry, mqtt_sender)

    return frame


"""Frame for food and uses the typical buttons"""
def frame_for_food(frame, mqtt_sender):
    frame_food = ttk.Frame(frame, padding=10, borderwidth=10, relief="ridge")
    frame_food_label = ttk.Label(frame_food, text="Food Frame")
    frame_food.grid()

    go_to_food_button = ttk.Button(frame_food, text="Go to food")
    send_image_back_button = ttk.Button(frame_food, text="Send Image to Computer")
    speed_label = ttk.Label(frame_food, text="Speed")
    speed_entry = ttk.Entry(frame_food, width=8)
    area_label = ttk.Label(frame_food, text="Area")
    area_entry = ttk.Entry(frame_food, width=8)

    frame_food_label.grid(row=0, column=1)
    go_to_food_button.grid(row=1, column=0)
    send_image_back_button.grid(row=1, column=2)
    speed_label.grid(row=2, column=0)
    speed_entry.grid(row=3, column=0)
    area_label.grid(row=2, column=2)
    area_entry.grid(row=3, column=2)

    go_to_food_button["command"] = lambda: handle_food(mqtt_sender, speed_entry, area_entry)
    send_image_back_button["command"] = lambda: handle_send_back(mqtt_sender)

    return frame


"""Frame for changing the baby using the typical buttons"""
def frame_for_change(frame, mqtt_sender):
    frame_change = ttk.Frame(frame, padding=10, borderwidth=10, relief="ridge")
    frame_change_label = ttk.Label(frame_change, text="Signal To Be Changed Frame")
    frame_change.grid()

    change_button = ttk.Button(frame_change, text="Change Me!")
    speed_label = ttk.Label(frame_change, text="Speed")
    speed_entry = ttk.Entry(frame_change, width=8)
    distance_label = ttk.Label(frame_change, text="Distance")
    distance_entry = ttk.Entry(frame_change, width=8)

    frame_change_label.grid(row=0, column=1)
    change_button.grid(row=1, column=1)
    speed_label.grid(row=1, column=0)
    speed_entry.grid(row=2, column=0)
    distance_label.grid(row=1, column=2)
    distance_entry.grid(row=2, column=2)

    change_button["command"] = lambda: handle_change(speed_entry, distance_entry, mqtt_sender)

    return frame


"""Frame for screaming and uses the typical buttons"""


def frame_for_scream(frame, mqtt_sender):
    frame_scream = ttk.Frame(frame, padding=10, borderwidth=10, relief="ridge")
    frame_scream_label = ttk.Label(frame_scream, text="Scream Frame")
    frame_scream.grid()

    scream_button = ttk.Button(frame_scream, text="Scream")
    duration_label = ttk.Label(frame_scream, text="Duration")
    duration_entry = ttk.Entry(frame_scream, width=8)

    frame_scream_label.grid(row=0, column=1)
    scream_button.grid(row=1, column=0)
    duration_label.grid(row=1, column=2)
    duration_entry.grid(row=2, column=2)

    scream_button["command"] = lambda: handle_scream(duration_entry, mqtt_sender)

    return frame

# Handlers


"""Sets up the function to run the sleep"""
def handle_sleep(how_long_button, mqtt_sender):
    print(how_long_button.get())
    value = int(how_long_button.get())
    print('I am sleeping')
    mqtt_sender.send_message("sleep", [value])


"""Sets up function for crawl"""
def handle_crawl(color, speed, mqtt_sender):
    print('Crawl')
    print(color.get(), speed.get())
    color = color.get()
    speed = int(speed.get())
    mqtt_sender.send_message("go_straight_until_color_is_not", [color, speed])


"""Sets up functions for cry """
def handle_cry(how_lonng_entry, mqtt_sender):
    value = int(how_lonng_entry.get())
    print('Cry')
    mqtt_sender.send_message("cry", [value])


"""Sets up functions for food"""
def handle_food(mqtt_sender, speed, area):
    speed = int(speed.get())
    area = int(area.get())
    mqtt_sender.send_message("spin_clockwise_until_sees_object", [speed, area])


"""Sets up function to send info back to laptop"""
def handle_send_back(mqtt_sender):
    mqtt_sender.send_message("display_camera_data")


"""Sets up function for change"""
def handle_change(distance, speed, mqtt_sender):
    distance = int(distance.get())
    speed = int(speed.get())
    mqtt_sender.send_message("go_forward_with_ir", [distance, speed])


"""Sets up functions for scream"""
def handle_scream(duration, mqtt_sender):
    duration = int(duration.get())
    mqtt_sender.send_message("scream", [duration])

