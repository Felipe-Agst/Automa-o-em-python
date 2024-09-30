import pyautogui as pa
import time 
import pyperclip

pa.PAUSE = 2



pa.press('win')
pa.write('chrome')
pa.press('enter')
pa.hotkey('CTRL', 'SHIFT', 'n')
pa.write('gmail.com')
pa.press('ENTER')
pa.write()### Colocar o seu E-mail
pa.press('ENTER')
time.sleep(6)
pa.write('')### colocar a senha do seu E-mail
pa.press('ENTER')


