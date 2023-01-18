# 디스코드 자동 전송기(임시) - 키보드 관련 명령어를 모름

import pyautogui

index = 0

while True:
    pyautogui.moveTo(3051, 527)
    pyautogui.click()
    pyautogui.sleep(1)
    pyautogui.rightClick()
    pyautogui.moveTo(3085, 501)
    pyautogui.click()
    pyautogui.sleep(1)
    pyautogui.moveTo(3318,302)
    pyautogui.click()
    pyautogui.sleep(1)
    index += 1
    print(f"{index}회 반복")