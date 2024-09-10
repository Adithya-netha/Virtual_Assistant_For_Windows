from  Automation.open_app import open_app
from Automation.open_wesite import openweb
import pyautogui as gui
from Text_to_speech import Braian_voice_tts
from Automation.play_music_yt import play_music_on_yt
from  Automation.playmusic_spotify import play_music_on_spotify

def close():
    gui.hotkey('alt','f4')

def opening_brain(text):
    if "website" in text or "open website" in text:
        text = text.replace("website","").strip()
        text = text.replace("open","").strip()
        text = text.replace("open website","").strip()
        openweb(text)
    else:
        text = text.replace("app","").strip()
        text = text.replace("open","").strip()
        open_app(text)


def Auto_main_brain(text):
    if text.startswith("open"):
        opening_brain(text)
    elif "close" in text:
        close()
    elif "play music" in text or "play music on youtube" in text:
        Braian_voice_tts.speak("which song do you want to play sir")
        x = input()
        play_music_on_yt(x)
    elif "play some music" in text or "play music on spotify" in text:
        Braian_voice_tts.speak("which song do you want to play sir")
        x = input()
        play_music_on_spotify(x)
    else:
        pass