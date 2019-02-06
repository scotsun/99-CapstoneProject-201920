# Put whatever you want in this module and do whatever you want with it.
# It exists here as a place where you can "try out" things without harm.

def main():
    import tkinter
    from tkinter import ttk
    import mqtt_remote_method_calls as com
    import time
    root=tkinter.Tk()
    name1 = input("Enter one name (subscriber): ")
    name2 = input("Enter another name (publisher): ")
    frame1=ttk.Frame(root,padding=10)
    frame1.grid()


    mqtt_client = com.MqttClient()
    mqtt_client.connect(name1, name2)

    go_forward_button=ttk.Button(frame1,text='Forward')
    go_forward_button.grid()
    go_forward_button['command']=(lambda: bly(entry_box,mqtt_client,entry_box2))

    frame2=ttk.Frame(root,padding=10)
    frame2.grid()

    entry_box=ttk.Entry(frame1)
    entry_box.grid()

    entry_box2=ttk.Entry(frame2)
    entry_box2.grid()


    time.sleep(1)  # Time to allow the MQTT setup.
    print()

    root.mainloop()

def bly(entry_box,mqtt_client,entry_box2):
    entry_box=entry_box.get()
    entry_box2=entry_box2.get()

    s=entry_box
    mqtt_client.send_message('forwardprint', [s,entry_box2])

