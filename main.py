# This is a sample Python script.
import pyautogui


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def fill_out_form():
    # Use a breakpoint in the code line below to debug your script.
    pyautogui.PAUSE = 0.5
    pyautogui.hotkey('win', '1')
    pyautogui.sleep(10)
    pyautogui.hotkey('ctrl', 't')
    pyautogui.sleep(4)
    pyautogui.write('https://forms.office.com/pages/responsepage.aspx?id=iuJja_motUeqQJfiMSFRZN4Wp4_ly1NJlXUt-KvoXzlUM083N1I0RDM1RlpSSjFCVkxTRk9LNFNDVi4u')
    pyautogui.press('enter')
    pyautogui.sleep(2)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.write('Edwin Perry')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.write('edwin501@revature.net')
    pyautogui.press('tab')
    pyautogui.press('space')
    pyautogui.press('tab')
    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.press('tab')
    pyautogui.press('space')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fill_out_form()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
