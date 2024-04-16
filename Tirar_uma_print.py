import pyautogui
'''
#print da tela toda
im1 = pyautogui.screenshot()
im2 = pyautogui.screenshot('minha_print.png')
'''
#print de um pedaço da tela
import pyautogui
im = pyautogui.screenshot('print_da_area.png',region=(0,0, 300, 400))