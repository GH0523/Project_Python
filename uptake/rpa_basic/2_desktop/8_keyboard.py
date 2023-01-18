import pyautogui

w = pyautogui.getWindowsWithTitle("메모장")[0] # 메모장 1개 띄운 상태에서 메모장 정보를 가져옴
w.activate()

# pyautogui.write("12345")
# pyautogui.write("Coding", interval=1) # 글 사이마다 1초 간격으로 적음
# pyautogui.write("나도코딩")

# pyautogui.write(["t", "e", "s", "t", "left", "left", "right", "l", "a", "enter"], interval=0.25)
# t e s t 순서대로 적은 후 왼쪽 방향키 2번, 오른쪽 방향키 2번, l a 순서대로 적고 enter 입력
# 기타 다른 명령어는 automate the boring stuff with python 검색 후 chapter20 > keyboard attributes 검색

# 특수 문자
# shift + 4 > $
# pyautogui.keyDown("shift") # shift 키를 누른 상태에서
# pyautogui.press("4") # 숫자 4 입력 후
# pyautogui.keyUp("shift") # shift 키를 뗀다

# 조합키 (Hot Key)
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a") # press("a")
# pyautogui.keyUp("ctrl") # ctrl + a

# 간편한 조합키
# pyautogui.hotkey("ctrl", "alt", "shift", "a")
# Ctrl 누름 > Alt 누름 > Shift 누름 > A 누름 > A 뗌 > Shift 뗌 > Alt 뗌 > Ctrl 뗌
# pyautogui.hotkey("ctrl", "a")

import pyperclip # 문장을 클립보드에 집어넣음
pyperclip.copy("나도코딩") # "나도코딩" 글자를 클립보드에 저장
pyautogui.hotkey("ctrl", "v") # 클립보드에 있는 내용을 붙여넣기

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")

my_write("나도코딩")

# 자동화 프로그램 종료
# wind : ctrl + alt + del