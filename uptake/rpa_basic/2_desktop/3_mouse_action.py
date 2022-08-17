import pyautogui
# pyautogui.sleep(3) # 3초 대기
# print(pyautogui.position())

# 마우스 클릭
# pyautogui.click(2625, -225, duration=1) # (2625, -225) 좌표를 마우스 클릭 (duration 가능)

# pyautogui.mouseDown()
# pyautogui.mouseUp() # click() = mouseDown() + mouseUp()

# 마우스 더블클릭
# pyautogui.doubleClick()
# pyautogui.click(clicks=2) # 둘 다 같음

# pyautogui.moveTo(300, 300)
# pyautogui.mouseDown()
# pyautogui.moveTo(400, 500)
# pyautogui.mouseUp()

# 마우스 좌, 우, 휠 클릭
# pyautogui.rightClick()
# pyautogui.leftClick()
# pyautogui.middleClick()

# 마우스 드래그
# pyautogui.moveTo(442, 496)
# pyautogui.drag(100, 0) # 현재 위치 기준 x=100 만큼, y=0 만큼 드래그(즉 move와 같이 상대적인 위치 / duration 가능)
# pyautogui.drag(100, 0, duration=1) # 너무 빨라 동작이 수행되지 않을때는 duration 활용
# pyautogui.dragTo(642, 496, duration=1) # 절대 좌표 기준(즉 moveTo와 동일)

# 마우스 휠 스크롤
# pyautogui.scroll(300) # 위 방향으로 300만큼 스크롤
# pyautogui.scroll(-300) # 아래 방향으로 300만큼 스크롤