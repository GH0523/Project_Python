import pyautogui

# file_menu = pyautogui.locateOnScreen("file_menu.png") # 제시된 이미지를 기반으로 좌표값 도출 ("""단수""")
# print(file_menu)
# pyautogui.click(file_menu)



# trash_icon = pyautogui.locateOnScreen("trash_icon.png")
# print(trash_icon)
# pyautogui.click(trash_icon)



# screenshot = pyautogui.locateOnScreen("screenshot.png")
# print(screenshot) # 찾지 못할 경우 None 출력



# for i in pyautogui.locateAllOnScreen("checkbox.png"): # 제시된 이미지를 기반으로 좌표값 도출 ("""복수""")
#     print(i)
#     pyautogui.click(i)

# checkbox = pyautogui.locateOnScreen("checkbox.png") # 만약 복수값이지만 단수 명령문을 실행할 경우 > 처음 발견하는 이미지에 대해서만 실행 후 종료
# pyautogui.click(checkbox)



# 속도 개선

# 1. GrayScale > 화면을 흑백으로 하여 비교(정확도 하락 우려)
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", grayscale=True)
# print(trash_icon)

# 2. 범위 지정
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", region=(2230, 832, 2555-2230, 924-832)) # 2230,832 / 2555,924
# print(trash_icon)

# 3.정확도 조정 > 정확도를 떨어뜨림(Ex.픽셀이 90% 이상 유사할 경우 똑같은 이미지로 인식)
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", confidence=0.9) # confidence의 기본값은 0.99
# print(trash_icon)



# 자동화 대상이 바로 보여지지 않는 경우

# 1. 계속 기다리기
# file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")

# 1-1
# if file_menu_notepad:
#     pyautogui.click(file_menu_notepad)
# else:
#     print("발견 실패")

# 1-2
# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     print("발견 실패")

# pyautogui.click(file_menu_notepad)

# 2. 일정 시간동안 기다리기 (TimeOut)
import time
import sys

# timeout = 10 # 10초 대기
# start = time.time() # 시작 시간 설정
# file_menu_notepad = None
# while file_menu_notepad == None:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     end = time.time() # 종료 시간 설정
#     if end - start > timeout: # 지정한 10초를 초과한 경우
#         print("시간 종료")
#         sys.exit()

# pyautogui.click(file_menu_notepad)

def find_target(img_file, timeout=30):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout:
            break
    return target

def my_click(img_file, timeout=30):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print(f"[Timeout {timeout}s] Target not found ({img_file}). Terminate program1")
        sys.exit()

my_click("file_menu_notepad.png", 10)