import pyautogui as py
import keyboard as kb
import tkinter as tk
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
    messagebox.showinfo("Deseja deletar todos os arquivos?")

open1()