""" This is a document similar to that of the shared gui that we used
for sprint one and two. It will be where I construct all my frames for the final
"""

import tkinter
from tkinter import ttk
import time

# Space for the frames


def frame_for_sleep(frame, mqtt_sender):
    frame_sleep = ttk.Frame(frame, padding=10, borderwidth=10, relief="ridge")
    frame_sleep_label = ttk.Label(frame_sleep, text="Sleep Frame")
    frame_sleep.grid()

    ask_to_sleep_button = ttk.Button(frame_sleep, text="Do you want to sleep baby?")
    how_long_label = ttk.Label(frame_sleep, text="How long do you want the baby to sleep for?")
    how_long_button = ttk.Entry(frame_sleep, width=8)

    ask_to_sleep_button.grid(row=1, column=0)
    frame_sleep_label.grid(row=0, column=1)
    how_long_label.grid(row=1, column=2)
    how_long_button.grid(row=2, column=2)

    ask_to_sleep_button["command"] = lambda: handle_sleep(how_long_button, mqtt_sender)

    return frame


def frame_for_crawl(frame, mqtt_sender):
    frame_crawl = ttk.Frame(frame, padding=10, borderwidth=10, relief="ridge")
    frame_crawl_label = ttk.Label(frame_crawl, text="Crawl Frame")
    frame_crawl.grid()

    crawl_button = ttk.Button(frame_crawl, text="Crawl")
    how_long_label = ttk.Label(frame_crawl, text="How long would you like to crawl?")
    how_long_entry = ttk.Entry(frame_crawl, width=8)

    frame_crawl_label.grid(row=0, column=1)
    crawl_button.grid(row=1, column=0)
    how_long_label.grid(row=1, column=2)
    how_long_entry.grid(row=2, column=2)

    crawl_button["command"] = lambda: handle_crawl(how_long_entry, mqtt_sender)

    return frame


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
# Handlers


def handle_sleep(how_long_button, mqtt_sender):
    value = int(how_long_button.get())
    print('I am sleeping')
    mqtt_sender.send_message("sleep", [value])


def handle_crawl(how_long_entry, mqtt_sender):
    value = int(how_long_entry.get())
    print('Crawl')
    mqtt_sender.send_message("crawl", [value])


def handle_cry(how_lonng_entry, mqtt_sender):
    value = int(how_lonng_entry.get())
    print('Cry')
    mqtt_sender.send_message("cry", [value])


def handle_food(mqtt_sender, speed, area):
    mqtt_sender.send_message("spin_clockwise_till_sees_object", [speed, area])


def handle_send_back(mqtt_sender):
    mqtt_sender.send_message("display_camera_data")

