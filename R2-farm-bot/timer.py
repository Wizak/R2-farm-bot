import datetime
import pyautogui
import crypto


def check():
    termin = 'day' #input data!
    start_date = '03/02/2021 15' #input data!
    format = '%d/%m/%Y %H'

    start = datetime.datetime.strptime(start_date, format)
    now = datetime.datetime.now()

    different = abs(start - now).days
    time_s = start.timetuple()[3]
    time_n = now.timetuple()[3]

    if termin == 'year' and 365 <= different and time_s <= time_n:
        pyautogui.alert('Бот заблокирован. Истекло время ключа!')
        crypto.encrypter()
        return 1
    elif termin == 'month' and 30 <= different and time_s <= time_n:
        pyautogui.alert('Бот заблокирован. Истекло время ключа!')
        crypto.encrypter()
        return 1
    elif termin == 'week' and 7 <= different and time_s <= time_n:
        pyautogui.alert('Бот заблокирован. Истекло время ключа!')
        crypto.encrypter()
        return 1
    elif termin == 'day' and 1 <= different and time_s <= time_n:
        pyautogui.alert('Бот заблокирован. Истекло время ключа!')
        crypto.encrypter()
        return 1
    elif termin == 'hour' and 0 <= different and time_s < time_n:
        pyautogui.alert('Бот заблокирован. Истекло время ключа!')
        crypto.encrypter()
        return 1
    else:
        return 0      