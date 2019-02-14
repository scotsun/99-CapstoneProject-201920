import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk
import shared_gui


def main():
    mqtt_sender = com.MqttClient()
    mqtt_sender.connect_to_ev3()

    root2 = tkinter.Tk()
    root2.title("Personal Frame")

    personal_frame = ttk.Frame(root2, padding=10, borderwidth=5, relief="groove")
    personal_frame.grid()
    grid_frames(get_led_frame(personal_frame, mqtt_sender), get_leds_with_camera_frame(personal_frame, mqtt_sender))
    root2.mainloop()


def get_led_frame(personal_frame, mqtt_sender):
    frame = ttk.Frame(personal_frame, padding=10, borderwidth=10, relief="ridge")
    frame.grid()
    frame_title = ttk.Label(frame, text="LED Frame")
    initial_lable = ttk.Label(frame, text="Initial Value")
    initial_entry = ttk.Entry(frame, width=8)
    rate_of_increase_lable = ttk.Label(frame, text="Rate of Increase")
    rate_of_increase_entry = ttk.Entry(frame, width=8)
    led_button = ttk.Button(frame, text="LED")

    frame_title.grid(row=0, column=1)
    initial_lable.grid(row=1, column=0)
    initial_entry.grid(row=2, column=0)
    rate_of_increase_lable.grid(row=1, column=2)
    rate_of_increase_entry.grid(row=2, column=2)
    led_button.grid(row=3, column=1)

    led_button["command"] = lambda: handle_run_leds(mqtt_sender, rate_of_increase_entry)

    return frame


def get_leds_with_camera_frame(personal_frame, mqtt_sender):
    frame = ttk.Frame(personal_frame, padding=10, borderwidth=10, relief="ridge")
    frame.grid()
    frame_title = ttk.Label(frame, text="LED Camera Frame")
    run_button = ttk.Button(frame, text="Run Camera with LEDS")

    frame_title.grid(row=0, column=1)
    run_button.grid(row=1, column=2)

    run_button["command"] = lambda: handle_run_leds_with_camera(mqtt_sender)

    return frame


def grid_frames(led_frame, led_camera_frame):
    led_frame.grid(row=0, column=0)
    led_camera_frame.grid(row=1, column=1)


def handle_run_leds(mqtt_sender, rate_of_increase):
    rate_of_increase=rate_of_increase.get()
    mqtt_sender.send_message("run_leds", [rate_of_increase])


def handle_run_leds_with_camera(mqtt_sender):
    mqtt_sender.send_message("run_leds_with_camera")
main()
