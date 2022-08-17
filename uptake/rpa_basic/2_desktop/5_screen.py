import pyautogui

# 스크린샷 찍기
# img = pyautogui.screenshot()
# img.save("screenshot.png") # 파일로 저장

# pyautogui.mouseInfo()
# 2584,-228 20,155,231 #149BE7

pixel = pyautogui.pixel(2584, -228) # 설정된 좌표값의 RGB값을 가져옴
print(pixel)

print(pyautogui.pixelMatchesColor(2584, -228, pixel)) # pixel에 있는 값과 해당 값이 같은가(Ture, False)
print(pyautogui.pixelMatchesColor(2584, -228, (64, 170, 242))) # "