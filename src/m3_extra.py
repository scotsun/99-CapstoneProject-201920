import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk
import m3_shared_gui

"""Main sets up the main frame and grids the frames"""
def main():
    mqtt_sender = com.MqttClient()
    mqtt_sender.connect_to_ev3()

    root = tkinter.Tk()
    root.title('Baby Robot')

    frame = ttk.Frame(root, padding=10, borderwidth=10, relief="ridge")
    frame.grid()

    sleep_frame, crawl_frame, cry_frame, food_frame, change_frame, scream_frame = shared_frames(frame, mqtt_sender)

    grid_frames(sleep_frame, crawl_frame, cry_frame, food_frame, change_frame, scream_frame)

    root.mainloop()


"""Takes frames for me_shared_gui and puts them here"""
def shared_frames(frame, mqtt_sender):
    sleep_frame = m3_shared_gui.frame_for_sleep(frame, mqtt_sender)
    crawl_frame = m3_shared_gui.frame_for_crawl(frame, mqtt_sender)
    cry_frame = m3_shared_gui.frame_for_cry(frame, mqtt_sender)
    food_frame = m3_shared_gui.frame_for_food(frame, mqtt_sender)
    change_frame = m3_shared_gui.frame_for_change(frame, mqtt_sender)
    scream_frame = m3_shared_gui.frame_for_scream(frame, mqtt_sender)
    return sleep_frame, crawl_frame, cry_frame, food_frame, change_frame, scream_frame


"""Grids the frames"""
def grid_frames(sleep_frame, crawl_frame, cry_frame, food_frame, change_frame, scream_frame):
    sleep_frame.grid(row=0, column=0)
    crawl_frame.grid(row=1, column=0)
    cry_frame.grid(row=2, column=0)
    food_frame.grid(row=3, column=0)
    change_frame.grid(row=4, column=0)
    scream_frame.grid(row=5, column=0)


main()
