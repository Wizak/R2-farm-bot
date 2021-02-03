import os
import time
import pyautogui


def main():
    source = [f'{os.getcwd()}'+'\\dist\\R2bot.exe', f'{os.getcwd()}'+'\\dist\\Decrypter.exe']
    target_dir = os.getcwd()[:(len(os.getcwd())-12)]
    target_dir_key = target_dir+'\\Keys\\crypto_'+time.strftime('%Y%m%d%H%M%S')+'.key'

    target = target_dir + os.sep + 'R2bot' + '.zip'
    zip_command = '7z a {0} {1}'.format(target, ' '.join(source))

    with open(target_dir_key, 'w') as f:
        key = ''
        with open('crypto.key', 'r') as c:
            key = c.read()
        f.write(key)

    if os.system(zip_command) != 0:
        pyautogui.alert('Error from archivater!')