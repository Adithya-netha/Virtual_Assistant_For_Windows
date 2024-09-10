import requests
from win10toast import ToastNotifier
import time
from Text_to_speech.Braian_voice_tts import speak
import threading
from DATA.dialouge_data import online_dlg
import random

random_dilauge = random.choice(online_dlg)

def alert(text):
    toaster = ToastNotifier()
    toaster.show_toast(
        "jarvis",
        text,
        duration=1,
        icon_path=r"C:\Users\Adhithya\Desktop\JARVIS\jarvis logo.ico",  # Path to the converted ICO file
        threaded=True
    )
  #  while toaster.notification_active():
   #     time.sleep(1)

def is_Online(url="https://www.google.com", timeout=5):
    try:
        response = requests.get(url, timeout=timeout)
        return response.status_code >= 200 and response.status_code < 300
    except requests.ConnectionError:
        return False

def internet_status():
    if is_Online():
        t1 = threading.Thread(target=speak,args=(random_dilauge,))
        t2 = threading.Thread(target=alert,args=(random_dilauge,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    else:

        alert("I am offline")

internet_status()
