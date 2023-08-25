import datetime
import os
import PySimpleGUI as sg
import playsound
import psutil

music = 'Battery-music-for-linux/Battery-music.mp3'
i = 'play'


def pop_up():
    global i
    sg.theme('DarkAmber')

    layout = [
        [sg.Text('Do you wish to stop the alarm?'),
         sg.Button('Ok'), sg.Button('Cancel')]
    ]

    # Create the Window
    window = sg.Window('Make your choice', layout)

    event = window.read(10000)

    if event[0] is None or event[0] == 'Ok':  # if user closes window or clicks cancel
        i = 'do not play'

    window.close()


def battery_check():
    global i
    global percent
    if percent >= 80 and plugged == "Not Plugged In":
        i = 'play'
    elif percent <= 30 and plugged == "Plugged In":
        i = 'play'



while True:
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = int(battery.percent)
    plugged = "Plugged In" if plugged else "Not Plugged In"
    now = datetime.datetime.now()
    hour = datetime.datetime.strftime(now, '%H')
    battery_check()
    if i == 'play':
        if percent >= 80 and plugged == "Plugged In":
            pop_up()
            if i == 'play':
                os.system("""notify-send -a "Battery Above 80%" -i "battery" "Remove the charger, your battery is above 80%" """)
                playsound.playsound(music)
        elif percent <= 30 and plugged == "Not Plugged In":
            pop_up()
            if i == 'play':
                os.system(
                    """notify-send -a "Battery below 30%" -i "battery" "Plug in the charger, your battery is below 30%" """)
                playsound.playsound(music)
       
