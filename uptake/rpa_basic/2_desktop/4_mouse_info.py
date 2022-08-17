import pyautogui

# pyautogui.FAILSAFE = False
# ^^^ 마우스를 모서리로 이동 할 경우 프로그램은 자동 종료
# 위 명령문을 실행 함으로써 자동 종료를 사전 차단

# pyautogui.PAUSE = 1
#  ^^^ 모든 동작에 1초씩 sleep 적용

# pyautogui.mouseInfo()

for i in range(10):
    pyautogui.move(100,100)
    pyautogui.sleep(1)