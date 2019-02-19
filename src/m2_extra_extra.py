import tkinter
from tkinter import ttk


def get_personal_frame_2(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")

    homework = ttk.Button(window, text='Homework Locator')
    fist_bump=ttk.Button(window, text= 'Fist Bump!')
    sleep=ttk.Button(window, text='Sleep')

    fist_bump["command"] = lambda: handle_fist_bump(mqtt_sender)
    homework["command"] = lambda: handle_homework(mqtt_sender)
    sleep["command"]= lambda: handle_sleep(mqtt_sender)

    sleep.grid(row=2,column=1)
    homework.grid(row=1, column=0)
    fist_bump.grid(row=1,column=2)

    return (frame)


def handle_homework(mqtt_sender):
    mqtt_sender.send_message('handle_homework', [])


def handle_idle(mqtt_sender):
    mqtt_sender.send_message('handle_idle', [])

def handle_fist_bump(mqtt_sender):
    mqtt_sender.send_message('handle_fist_bump',[])

def handle_sleep(mqtt_sender):
    mqtt_sender.send_message('handle_sleeping',[])