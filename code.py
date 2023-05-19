import ctypes
import struct
import psutil
import pygame
import time

pygame.init()

def flash_screen():
    # Define the FLASHWINFO structure
    info = struct.pack('IIII', 20, 0, 5, 0)
    ctypes.windll.user32.FlashWindowEx(ctypes.byref(ctypes.c_long(0)), 2, info, 0)

def play_sound():
    pygame.mixer.music.load('D:\Python\siren.mp3')
    pygame.mixer.music.play()

while True:
    battery = psutil.sensors_battery()
    if battery.percent == 95 and not battery.power_plugged:
        # Flash the screen
        flash_screen()
        
        # Play the sound
        play_sound()

        # Wait for a few seconds to prevent the sound from looping
        time.sleep(5)


