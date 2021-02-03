import archivater
import pyautogui
import datetime
import os
import crypto


def main():
    cmd1 = 'pyinstaller bot.spec'
    cmd2 = 'pyinstaller decrypter.spec'

    os.system(cmd1)
    os.system(cmd2)

