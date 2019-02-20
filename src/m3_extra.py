import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk
import m3_shared_gui


def main():
    mqtt_sender = com.MqttClient()
    mqtt_sender.connect_to_ev3()

    root = tkinter.Tk()
    root.title('Baby Robot')

    frame = ttk.Frame(root, padding=10, borderwidth=10, relief="ridge")
    frame.grid()

    sleep_frame, crawl_frame, cry_frame, food_frame = shared_frames(frame, mqtt_sender)

    grid_frames(sleep_frame, crawl_frame, cry_frame, food_frame)

    root.mainloop()


def shared_frames(frame, mqtt_sender):
    sleep_frame = m3_shared_gui.frame_for_sleep(frame, mqtt_sender)
    crawl_frame = m3_shared_gui.frame_for_crawl(frame, mqtt_sender)
    cry_frame = m3_shared_gui.frame_for_cry(frame, mqtt_sender)
    food_frame = m3_shared_gui.frame_for_food(frame, mqtt_sender)
    return sleep_frame, crawl_frame, cry_frame, food_frame


def grid_frames(sleep_frame, crawl_frame, cry_frame, food_frame):
    sleep_frame.grid(row=0, column=0)
    crawl_frame.grid(row=1, column=0)
    cry_frame.grid(row=2, column=0)
    food_frame.grid(row=3, column=0)


main()
