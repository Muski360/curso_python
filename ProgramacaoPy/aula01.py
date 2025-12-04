import pyautogui as py
import keyboard as kb
from tkinter import messagebox

def open1():
    kb.press_and_release('win+r')
    py.sleep(1)
    py.write('system32')
    py.sleep(0.5)
    py.press('enter')
    py.sleep(1)
    kb.press_and_release('ctrl+a')
    py.sleep(0.5)   
    while True:
        if kb.is_pressed('enter'):
            break
        else:
            messagebox.showinfo("Deseja deletar todos os arquivos?")

open1()