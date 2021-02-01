import pyautogui
import time
import threading
import tkinter as tk
import tkinter.messagebox as tm
import sys

from PIL import Image


def main():
    def use_key(k):
        nonlocal dtime
        if k != 'q':
            pyautogui.keyDown(k)
            pyautogui.keyUp(k)
            time.sleep(dtime)
        else:
            check_hp(k)

    def check_hp(k):
        nonlocal mark_hp, mark_screen, death, dtime
        x, y = pyautogui.locateOnScreen(mark_hp)[:2]
        x, y = int(x+eps[0]), int(y+eps[1])
        pyautogui.screenshot(mark_screen)
        im = Image.open(mark_screen)
        pix = im.load()
        curent = pix[x, y]
        if curent == death:
            pyautogui.keyDown(k)
            pyautogui.keyUp(k)
            time.sleep(dtime)

    def selection_box():
        nonlocal action, vars, conformity
        values = sorted(list(set(v.get() for v in vars)))[1:]
        key_press = [(use_key, (str(conformity_numbers[i]), )) for i in values]
        action = key_press
        
    def btn_on():
        nonlocal main_process      
        main_process = True

    def btn_off():
        nonlocal main_process
        main_process = False

    def info():
        tm.showinfo(title='Info', message='Версия 1.0.\n\nСырая версия, если есть вопросы или вы нашли ошибку - обратитесь сюда: wizakwork@gmail.com.')

    def bot():
        nonlocal STATUS
        while STATUS:
            nonlocal main_process, need_title, action, dtime
            if main_process:
                try:
                    focus_title = str(pyautogui.getActiveWindowTitle()).lower()
                except:
                    pass
                if focus_title == need_title or 'r2online' in focus_title or 'r2 online' in focus_title:
                    threads = [threading.Thread(target=target, name=str(args), args=args) for target, args in action]
                    [t.start() for t in threads]
                    [t.join() for t in threads]
                time.sleep(dtime)
            time.sleep(dtime)

    STATUS = True      
    main_process = False
    need_title = '??'
    mark_hp = 'Mark/Hp.png'
    mark_screen = 'Mark/Screenshot.png'
    eps = [50, -24]
    dtime = 0.15
    death = (10, 10, 10)
    action = []
    window = tk.Tk()
    window.iconbitmap('Interface/R2-Logo.ico')
    window.title('Farm bot')
    window.geometry('550x300')
    main_text = 'Спасибо за пользования, работаю над обновлениями!\nЕсли не жалко копейку:\n\t\t\t5375414116847889 - bank card'
    numbers = list(range(1, 9))
    leters = ['e', 'q']
    symbols = numbers + leters
    conformity_numbers = {k:str(n) for k, n in zip(range(1, len(numbers)+1), numbers)}
    conformity_leters = {k:l for k, l in zip(range(len(numbers)+1, len(symbols)+1), leters)}
    conformity = conformity_numbers.update(conformity_leters)
    nums = range(1, len(symbols)+1)
    textsl = [' ' for _ in symbols]
    textsb = ['Включить', 'Выключить']
    rell = [(i/10, 0.3) for i in range(len(symbols))]
    relc = [(i/10, 0.4) for i in range(len(symbols))]
    relb = [(.7, .6), (.7, .8)]
    vars = [tk.IntVar() for _ in symbols]
    label0 = tk.Label(window, bg='pink', text='Привет, выбери те кнопки на передней панеле р2, что будут задействованы ботом!', justify='left')
    label0.place(relx=.07, rely=.1)
    label1 = tk.Label(window, bg='pink', text=main_text, justify='left')
    label1.place(relx=.05, rely=.6)
    button = tk.Button(text='Дополнительная информация', width=33, background="pink", foreground="blue", font="16", command=info)
    button.place(relx=.05, rely=.8)
    labels = [tk.Label(window, bg='gray', width=5, text=symbol) for symbol in symbols]
    [label.place(relx=xy[0], rely=xy[1]) for label, xy in zip(labels, rell)]
    boxs = [tk.Checkbutton(window, text=text, variable=var, onvalue=var_num, offvalue=0, command=selection_box) for text, var, var_num in zip(textsl, vars, nums)]
    [box.place(relx=xy[0], rely=xy[1], width=50) for box, xy in zip(boxs, relc)]
    btns = [tk.Button(text=text, width=16, background="pink", foreground="blue", font="16", command=cmd) for text, cmd in zip(textsb, [btn_on, btn_off])]
    [btn.place(relx=xy[0], rely=xy[1]) for btn, xy in zip(btns, relb)]
    thread_bot = threading.Thread(target=bot)
    thread_bot.start()
    window.mainloop()
    STATUS = False
    thread_bot.join()


if __name__ == '__main__':
    main()