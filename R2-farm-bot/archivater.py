import os
import time
import pyautogui


def main():
    source = [f'{os.getcwd()}'+'\\dist\\R2bot.exe']
    target_dir = os.getcwd()[:(len(os.getcwd())-12)]

    target = target_dir + os.sep + 'R2bot' + '.zip'
    zip_command = '7z a {0} {1}'.format(target, ' '.join(source))

    if os.system(zip_command) != 0:
        pyautogui.alert('Error from archivater!')


main()