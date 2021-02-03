import crypto
import pyautogui


def main():
    while True:
        key = pyautogui.prompt('Вышел срок использования.\n\nВведите ключ:')
        if key != None:
            try:
                crypto.decrypter(key)
            except:
                pyautogui.alert('Неверный ключ!')
                continue
            pyautogui.alert('Бот успешно разблокировано!')
            break
        else:
            break